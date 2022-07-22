import time


class LudoGame:
    """
    This represents the Ludo game being currently played.  It contains an array which represents the board.
    """

    def __init__(self):
        self._players = []      # array of player objects
        self._turns = None      # array of turns
        self._board = []        # board created in init function

        home_rows_player_A = ["", "", "", "", "", "", ""]  # pos 56
        home_rows_player_B = ["", "", "", "", "", "", ""]  # pos 57
        home_rows_player_C = ["", "", "", "", "", "", ""]  # pos 58
        home_rows_player_D = ["", "", "", "", "", "", ""]  # pos 59

        """
        Create the board which is an array.  The last four elements of the array are subarrays, for the home rows of 
        players A-D.
        """
        for i in range(1, 57):
            self._board.append("")
        self._board.append(home_rows_player_A)
        self._board.append(home_rows_player_B)
        self._board.append(home_rows_player_C)
        self._board.append(home_rows_player_D)

    def play_game(self, players_list, turns_list):

        self.create_player_list(players_list)       # add player objects to LudoGame object as an array of objects

        for turn in turns_list:
            current_player = self.get_player_by_position(turn[0])
            current_roll = turn[1]

            player_token_p = current_player.get_token_p_step_count()
            player_token_q = current_player.get_token_q_step_count()

            token_choice = self.choose_token_algorithm(current_player, current_roll, player_token_p, player_token_q)

            if token_choice == "Can't move any tokens!  Skipping Turn.":
                break   # go to next turn in for loop

            self.move_token(current_player, token_choice, current_roll)

            self.print_game_board()

    def choose_token_algorithm(self, player, current_roll, p_steps, q_steps):
        """
        This function implements the algorithm to decide which of the player's two tokens they should move.  Or if the
        tokens will be stacked.

        :param player:          Player object by reference
        :param current_roll:    Int of how far each token could move based on the die roll
        :param p_steps:         How many steps the player's p token has moved so far in the game
        :param q_steps:         How many steps the player's q token has moved so far in the game
        :return:                A string.  Will return the "P" token, the "Q" token, or "P and Q" for stacked tokens.
        """

        """
        Step 0) If the tokens are already stacked then the algorithm has no choice but to move both.
        """
        if p_steps == q_steps:
            if p_steps != 57:                            # edge case if both tokens are in E
                if p_steps != -1 and p_steps != 0:       # if tokens are not both in ready or home space.
                    return ["P", "Q"]                    # tokens are stacked so move both

        """
        Step 1) If the die roll is 6, if a token is in the home yard, return that token to move.  Checks P first so if
        both are in the home yard, P will be chosen as the token.

        Also incorporates step 2 of the algorithm.  If one token is in the home square, and the other is exactly 6 steps
        away from the end, let the one closest to the end move and finish.
        """
        if current_roll == 6:
            if p_steps == -1:
                if q_steps + current_roll == 57:
                    return ["Q"]
                else:
                    return ["P"]
            elif q_steps == -1:
                if p_steps + current_roll == 57:
                    return ["P"]
                else:
                    return ["Q"]

        """
        Step 3)  If one token can move and kick out an opponent token, then move that token.  Tests P first so 
        will choose P if both tokens can kick out an opponent's token.
        
        First, we must determine where the token will be on the game board, to test if an opponent's token will
        be there.  If the token is in the "ready to go" position, then this is a special case, as the future position
        will be impacted by the start position, which is different for each player "A", "B" have different start
        positions for example.
        """

        player_start_space = player.get_start_space()-1

        # Test whether token p is in home yard.  Get p token's steps
        if p_steps == 0:
            future_board_pos_p = self.get_board_position_space(player_start_space + current_roll)
        else:
            future_board_pos_p = self.get_board_position_space(p_steps + current_roll)

        # Test whether q is in home yard.  Get q token's steps
        if q_steps == 0:
            future_board_pos_q = self.get_board_position_space(player_start_space + current_roll)
        else:
            future_board_pos_q = self.get_board_position_space(q_steps + current_roll)

        # if future board pos token p is not empty, and it contains an enemy token
        if future_board_pos_p != "":
            if future_board_pos_p[0] != player.get_position():
                return ["P"]

        # if future board pos token q is not empty, and it contains an enemy token
        if future_board_pos_q != "":
            if future_board_pos_q[0] != player.get_position():
                return ["Q"]

        """Step 4)  Move the token that is furthest from the finishing square.  Don't move if at end step."""
        if p_steps > q_steps:
            if q_steps != -1 or q_steps != 57:
                return ["Q"]
        else:
            if p_steps != -1 or p_steps != 57:
                return ["P"]

        """
        This will be the case where both tokens are in the home yard and the player hasn't rolled a six, or perhaps
        they have won the game, but were still fed a turn into the LudoGame object for some reason.
        """
        return "Player " + str(player.get_position()) + " can't move any tokens!  Skipping Turn."

    def move_token(self, player_obj, token_name, board_steps):
        """
        Moves one a player's tokens across the game board a specified number of steps.  It will then update the
        token's total steps and kick out other opponent's tokens as needed.

        If a player's two tokens land on the same space on the board, the player will stack the two tokens, and move
        them as one piece until they reach the finishing square.  The tokens are not stacked if both at home.

        If a player's token lands on a space occupied by an opponent's token, the opponent token will be returned
        or kicked back to its home yard, and can only re-enter into play when the owner rolls a 6.


        :param token_name:      list token name ['P'], ['Q'], or [P, Q] if choose_token algorithm decides tokens are
                                stacked

        :param board_steps:     steps the token will take across the board as an int
        :return:                none
        :param player_obj:      player object
        """

        """Set up the variables that will be used in this function."""
        player_pos_char = player_obj.get_position()
        player_start_space = player_obj.get_start_space()-1
        player_end_space = player_obj.get_end_space()-1

        token_string = []
        for token in token_name:
            token_string.append(token.lower() + player_pos_char)

        """
        Get the steps the token has already traversed on the board.  The token will be a list of [P], [Q], or 
        [P, Q] as the choose_token_algorithm will determine whether the tokens are stacked.
           
        If the first item in the list is [P], get the P step count, as that will be the same if only P or if stacked.
           
        Else, return the Q token steps. 
           
        The past steps of the token is used to determine where the token will be moved to the board.            
        """
        if token_name[0] == "P":
            step_count = player_obj.get_token_p_step_count()
        else:
            step_count = player_obj.get_token_q_step_count()

        """
        If token in home yard, move to ready space and return.  Don't edit board as technically not on board array
        yet.
        """
        if step_count == -1:
            player_obj.set_token_position(token_name[0], "R")
            return

        """
        If token in home yard, set steps as the player start space plus board steps to move.
          
        If not in home yard, set steps as the step_count, which has the start space now already built in, 
        and the steps to move.
           
        This variable, future_board_pos, will be used to determine if the board space is occupied.
        """
        if step_count == 0:
            future_board_pos = player_start_space + board_steps - 1     # if in home yard set steps plus start pos
        else:
            future_board_pos = step_count + board_steps - 1  # else add steps to board_count where start pos already in

        """
        This determines whether the future board position will be in the player's home rows.  It adds backtracking if
        the die roll is not the exact roll needed to enter the end "E" space of the game board.
        """
        home_row_spaces = None

        if future_board_pos > player_end_space:
            home_row_spaces = future_board_pos - player_end_space
            if home_row_spaces > 6:
                steps_to_backtrack = home_row_spaces - 6
                home_row_spaces = home_row_spaces - steps_to_backtrack

        """
        This determines whether the future board position has an opponent's token in it already to be kicked out.
        It will skip if in the home_row_spaces as it would be impossible for an opponent's token to be there.
        
        If an opponent token exists, it will be kicked out of the space.
        """
        if home_row_spaces is None:
            future_board_position_space = self.get_board_position_space(future_board_pos)

            if future_board_position_space != "" and future_board_position_space[-1] != player_pos_char:
                self.kick_out_opponent_tokens(future_board_pos, future_board_position_space)

        """
        This determines moves the token to the home row spaces (using a function move_to_home_rows to determine what
        home row based on the player char letter) if the home_row_spaces is not empty.
        
        If the home row spaces variables is empty, then we don't need a helper function to decide which home row array
        to enter, and can directly place the token in the board array.  
        
        Uses for loops to handle the possibility that the tokens are stacked.
        
        Previous lines in this function should have kicked out an opponent's token if it was present.
        """
        if home_row_spaces is not None:
            self.move_to_home_rows(player_pos_char, player_obj, token_name, home_row_spaces)
        else:
            for token in token_name:
                i = 0
                player_obj.set_token_position(token, future_board_pos)  # set token info in player object
                self.set_board_pos_space(token_string[i], future_board_pos)
                i += 1

    def kick_out_opponent_tokens(self, future_board_pos, future_board_position_space):

        # TODO:  have to find player object token belongs to and edit that too somehow
        future_board_position_space = self.get_board_position_space(future_board_pos)
        self.set_board_pos_space("", future_board_pos)

    def move_to_home_rows(self, player_pos_char, player_obj, token_name, future_board_pos, home_row_spaces):

        # home_rows_player_A = pos 56
        # home_rows_player_B = pos 57
        # home_rows_player_C = pos 58
        # home_rows_player_D = pos 59

        for token in token_name:
            if player_pos_char == "A":
                player_obj.set_token_position(token_name, future_board_pos)
                self.set_board_pos_space(token_name, 56, home_row_spaces)
            elif player_pos_char == "B":
                player_obj.set_token_position(token_name, future_board_pos)
                self.set_board_pos_space(token_name, 57, home_row_spaces)
            elif player_pos_char == "C":
                player_obj.set_token_position(token_name, future_board_pos)
                self.set_board_pos_space(token_name, 58, home_row_spaces)
            elif player_pos_char == "D":
                player_obj.set_token_position(token_name, future_board_pos)
                self.set_board_pos_space(token_name, 59, home_row_spaces)

    def set_board_pos_space(self, token, board_pos, board_pos2=None):

        # board_pops2 = home rows before end space
        if board_pos2 is not None:
            self._board[board_pos][board_pos2] = token
        else:
            self._board[board_pos] = token

    def get_board_position_space(self, board_pos):
        return self._board[board_pos]

    def create_player_list(self, players_list):

        for position in players_list:
            self._players.append(Player(position))

    def print_game_board(self):
        """
        This prints the array and 4 sub-arrays to the console in a form that actually looks like a Ludo board.
        :return:
        """

        for i in range(0, 15):
            if self._board[i] == '':
                print("[  ]", end="")
            else:
                print("[" + self._board[i] + "]", end="")

        for j in range(0, 13):
            print("")
            for i in range(0, 13):

                if i == 0:
                    if self._board[55 - j] == '':
                        print("[  ]", end="")
                    else:
                        print("[" + self._board[55 - j] + "]", end="")

                if j == 6:
                    if i > 6:
                        if self._board[58][-2-(i-7)] == '':
                            print("[  ]", end="")
                        else:
                            print("[" + self._board[58][-2-(i-7)] + "]", end="")

                    if i == 6:
                        print("[E ]", end="")

                    if 6 > i >= 0:
                        if self._board[56][i] == '':
                            print("[  ]", end="")
                        else:
                            print("[" + self._board[56][i] + "]", end="")

                if i == 6 and j < 6:
                    if self._board[57][j] == '':
                        print("[  ]", end="")
                    else:
                        print("[" + self._board[57][j] + "]", end="")

                if i == 6 and j > 6:
                    if self._board[59][-2-(j-7)] == '':
                        print("[  ]", end="")
                    else:
                        print("[" + self._board[59][-2-(j-7)] + "]", end="")

                if i == 12:
                    if self._board[15 + j] == '':
                        print("[  ]", end="")
                    else:
                        print("[" + self._board[15 + j] + "]", end="")

                else:
                    if j != 6:
                        print("    ", end="")

        print("")
        for i in range(42, 27, -1):
            if self._board[i] == '':
                print("[  ]", end="")
            else:
                print("[" + self._board[i] + "]", end="")

        print("")

    def get_player_by_position(self, player_position):
        """takes as a parameter the player's position as a string and returns the player object, or a string
        indicating that player was not found."""
        for player in self._players:
            if player.get_position() == player_position:
                return player

        return "Player not found!"


class Player:

    def __init__(self, position):

        self._position = position.upper()

        if self._position == 'A':
            self._start_space = 1
            self._end_space = 50

        elif self._position == 'B':
            self._start_space = 15
            self._end_space = 8

        elif self._position == 'C':
            self._start_space = 29
            self._end_space = 22

        elif self._position == 'D':
            self._start_space = 43
            self._end_space = 36

        self._token_positions = {"P": "H", "Q": "H"}        # H = home yard; R = ready to go;
        self._game_status = False

    def get_position(self):                                 # e.g- "A", "B", "C", or "D"
        return self._position

    def set_token_position(self, token, pos):
        self._token_positions[token] = pos

    def get_completed(self):
        """:return: true if player has finished the game, or false it not finished."""
        return self._game_status

    def get_token_p_step_count(self):                        # H = -1, R = 0, s/b no more than 57
        steps = self._token_positions["P"]
        if steps == "H":
            return -1
        if steps == "R":
            return 0
        return steps

    def get_token_q_step_count(self):                            # H = -1, R = 0, s/b no more than 57
        steps = self._token_positions["Q"]
        if steps == "H":
            return -1
        if steps == "R":
            return 0
        return steps

    def get_space_name(self, total_steps):

        if total_steps == -1:
            return "H"

        elif total_steps == 0:
            return "R"

        elif total_steps <= 50:
            return total_steps

        elif 57 > total_steps > 50:
            return str(self._position) + str(total_steps - 50)

        elif total_steps == 57:
            return "E"

        elif total_steps > 57:
            return self.get_space_name(total_steps - (total_steps - 57))    # recursion if over step limit

    def get_start_space(self):
        return self._start_space

    def get_end_space(self):
        return self._end_space


def main():
    players = ['A', 'B']
    turns = [('A', 6), ('A', 4), ('A', 5), ('A', 4), ('B', 6), ('B', 4), ('B', 1), ('B', 2), ('A', 6), ('A', 4),
             ('A', 6), ('A', 3), ('A', 5), ('A', 1), ('A', 5), ('A', 4)]

    game = LudoGame()
    game.play_game(players, turns)
    player_B = Player("A")
    print(player_B.get_space_name(55))


    print_walk_around_board()




    # current_tokens_space = game.play_game(players, turns)

    # player_A = game.get_player_by_position('A')

    # print(player_A.get_completed())
    # print(player_A.get_token_p_step_count())
    # print(current_tokens_space)

    # player_B = game.get_player_by_position('B')

    # print(player_B.get_space_name(55))


def print_walk_around_board():
    game = LudoGame()
    #game.print_game_board()
    #game._board[28] = "A_P"
    # game._board[12] = "A_Q"
    # game._board[2] = "B_P"
    # game._board[39] = "B_Q"
    game.print_game_board()

    for i in range(0, 56):

        print("\r")
        print("\r")
        print("\r")
        game._board[i] = "Ap"

        if i >0:
            game._board[i-1] = ""
        time.sleep(.5)
        game.print_game_board()

    #print(game._board[5])
    game.print_game_board()

    game._board[55] = ""
    game._board[56][0] = "Ap"
    time.sleep(1)
    game.print_game_board()

    game._board[56][0] = "A1"
    game._board[56][1] = "Ap"
    time.sleep(1)
    game.print_game_board()

    game._board[56][1] = "A2"
    game._board[57][0] = "Ap"
    time.sleep(1)
    game.print_game_board()

    game._board[57][0] = "B1"
    game._board[58][0] = "Ap"
    time.sleep(1)
    game.print_game_board()

    game._board[58][0] = "C1"
    game._board[59][0] = "Ap"
    time.sleep(1)
    game.print_game_board()

    game._board[59][0] = "D1"
    game._board[59][1] = "Ap"
    time.sleep(1)
    game.print_game_board()


if __name__ == '__main__':
    main()
