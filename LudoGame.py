import time

class LudoGame:
    """

    """

    def __init__(self):
        self._players = []
        self._turns = None
        self._board = []

        home_rows_player_A = ["", "", "", "", "", "", ""] # pos 56
        home_rows_player_B = ["", "", "", "", "", "", ""] # pos 57
        home_rows_player_C = ["", "", "", "", "", "", ""] # pos 58
        home_rows_player_D = ["", "", "", "", "", "", ""] # pos 59

        for i in range(1, 57):
            self._board.append("")
        self._board.append(home_rows_player_A)
        self._board.append(home_rows_player_B)
        self._board.append(home_rows_player_C)
        self._board.append(home_rows_player_D)

    def play_game(self, players_list, turns_list):
        self.create_player_list(players_list)

        for turn in turns_list:
            current_player = self.get_player_by_position(turn[0])
            current_roll = turn[1]

            player_token_p = current_player.get_token_p_step_count()
            player_token_q = current_player.get_token_q_step_count()

            token_choice = self.choose_token_algorithm(current_player, current_roll, player_token_p, player_token_q)

            if token_choice == "Can't move any tokens!  Skipping Turn.":
                break

            self.move_token(current_player, token_choice, current_roll)

            self.print_game_board()










    def choose_token_algorithm(self, player, current_roll, p_steps, q_steps):
        """
        This function implements the algorithm to decide which of the two player's tokens they should move.

        :param player:          Player object by reference
        :param current_roll:    Int of how far each token could move based on the die roll
        :param p_steps:         How many steps the player's p token has moved so far in the game
        :param q_steps:         How many steps the player's q token has moved so far in the game
        :return:                A string.  Will return the "P" token, the "Q" token, or "P and Q" for stacked tokens.
        """

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

        """Step 3)  If one token can move and kick out an opponent token, then move that token.  Tests P first so 
        will choose P if both tokens can kick out an opponent's token."""
        player_start_space = player.get_start_space()-1

        if p_steps == 0:
            future_board_pos_p = self.get_board_position_space(player_start_space + current_roll)
        else:
            future_board_pos_p = self.get_board_position_space(p_steps + current_roll)

        if q_steps == 0:
            future_board_pos_q = self.get_board_position_space(player_start_space + current_roll)
        else:
            future_board_pos_q = self.get_board_position_space(q_steps + current_roll)

        if future_board_pos_p != "":
            if future_board_pos_p[0] != player.get_position():
                return ["P"]

        if future_board_pos_q != "":
            if future_board_pos_q[0] != player.get_position():
                return ["P"]

        """Step 4)  Move the token that is furthest from the finishing square"""
        if p_steps > q_steps:
            return ["Q"]
        elif q_steps > p_steps:
            return ["P"]
        elif p_steps == q_steps:
            if p_steps != -1 and p_steps != 0:
                return ["P", "Q"]        # special case to stack tokens
            else:
                return ["P"]

        return "Can't move any tokens!  Skipping Turn."

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

        for token in token_name:
            token_string = token.lower() + player_pos_char

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
            pass


        future_board_position_space = self.get_board_position_space(future_board_pos)


        self.kick_out_opponent_tokens(future_board_pos, future_board_position_space)


        #player_obj.set_token_position(token_name, "H")
       # future_board_position_space


        # home_rows_player_A = pos 56
        # home_rows_player_B = pos 57
        # home_rows_player_C = pos 58
        # home_rows_player_D = pos 59

        if future_board_pos > player_end_space:
            steps_over_end_space = future_board_pos - player_end_space
            if steps_over_end_space > 7:
                steps_to_backtrack = future_board_pos - steps_over_end_space
                player_obj.set_token_position(token_name, future_board_pos)
                self.set_board_pos_space(token_name, 56, steps_over_end_space)
            else:
                self.move_to_home_rows(player_pos_char, player_obj, token_name, future_board_pos, steps_over_end_space)

        if future_board_pos <= player_end_space:
            for token in token_name:
                player_obj.set_token_position(token, future_board_pos)      # set token info in player object
                self.set_board_pos_space(token_string, future_board_pos)    # place token on board as string "e.g pA"

        # TODO:  add if other player has occupied space




    def kick_out_opponent_tokens(self, future_board_pos, future_board_position_space):




    def move_to_home_rows(self, player_pos_char, player_obj, token_name, future_board_pos, steps_over_end_space):

        for token in token_name:
            if player_pos_char == "A":
                player_obj.set_token_position(token_name, future_board_pos)
                self.set_board_pos_space(token_name, 56, steps_over_end_space)
            elif player_pos_char == "B":
                player_obj.set_token_position(token_name, future_board_pos)
                self.set_board_pos_space(token_name, 57, steps_over_end_space)
            elif player_pos_char == "C":
                player_obj.set_token_position(token_name, future_board_pos)
                self.set_board_pos_space(token_name, 58, steps_over_end_space)
            elif player_pos_char == "D":
                player_obj.set_token_position(token_name, future_board_pos)
                self.set_board_pos_space(token_name, 59, steps_over_end_space)

    def set_board_pos_space(self, token, board_pos, board_pos2=None):

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
