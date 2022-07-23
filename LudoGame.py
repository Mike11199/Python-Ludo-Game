"""
Name:               Michael Iwanek
GitHub:             https://github.com/osu-cs162-u22/portfolio-Mike11199
GitHub Username:    Mike11199
Assignment:         Portfolio Project
Description:        Ludo Game
Date:               08/11/2022
Class:              CS_162_400_U2022
"""

import time


class LudoGame:
    """
    This represents the Ludo game being currently played.  It contains an array which represents the board.
    """

    def __init__(self):
        self._players = []      # array of player objects
        self._turns = None      # array of turns
        self._board = []        # board created in init function

        home_rows_player_A = ["", "", "", "", "", "", ""]                   # pos 56
        home_rows_player_B = ["", "", "", "", "", "", ""]                   # pos 57
        home_rows_player_C = ["", "", "", "", "", "", ""]                   # pos 58
        home_rows_player_D = ["", "", "", "", "", "", ""]                   # pos 59
        board_home_yard_positions = {"A": ["", ""], "B": ["", ""], "C": ["", ""], "D": ["", ""]}    # pos 60
        board_ready_positions = {"A": ["", ""], "B": ["", ""], "C": ["", ""], "D": ["", ""]}        # pos 61

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
        self._board.append(board_home_yard_positions)
        self._board.append(board_ready_positions)

    def sort_turns(self, turns_list):
        """
        This sorts the list of tuples that represents the move order of the game.  A goes first, then B, then C, then D.

        If anyone rolls a 6, that player can go again (one time).
        :param turns_list:
        :return:
        """

        A_turns = []
        B_turns = []
        C_turns = []
        D_turns = []
        sorted_turns_list = []

        for i in range(0, len(turns_list)):
            current_player = turns_list[i][0]
            if current_player == 'A':
                A_turns.append(turns_list[i])
            elif current_player == 'B':
                B_turns.append(turns_list[i])
            elif current_player == 'C':
                C_turns.append(turns_list[i])
            elif current_player == 'D':
                D_turns.append(turns_list[i])

        """
        This sorts the turn list in order of A, B, C, D.  If any die rolls are 6, the player can go one (and only one)
        additional turn, before resuming the A, B, C, D order.
        """
        for i in range(0, len(turns_list)):

            first_roll_a = ""
            first_roll_b = ""
            first_roll_c = ""
            first_roll_d = ""

            if A_turns:
                first_roll_a = A_turns[0][1]
                sorted_turns_list.append(A_turns[0])
                A_turns.pop(0)

                # If the first roll was 6, and A is not out of moves, then A can go again.
                if A_turns:
                    if first_roll_a == 6:
                        sorted_turns_list.append(A_turns[0])
                        A_turns.pop(0)

            if B_turns:
                first_roll_b = B_turns[0][1]
                sorted_turns_list.append(B_turns[0])
                B_turns.pop(0)

                # If the first roll was 6, and B is not out of moves, then B can go again.
                if B_turns:
                    if first_roll_b == 6:
                        sorted_turns_list.append(B_turns[0])
                        B_turns.pop(0)

            if C_turns:
                first_roll_c = C_turns[0][1]
                sorted_turns_list.append(C_turns[0])
                C_turns.pop(0)

                # If the first roll was 6, and C is not out of moves, then C can go again.
                if C_turns:
                    if first_roll_c == 6:
                        sorted_turns_list.append(C_turns[0])
                        C_turns.pop(0)

            if D_turns:
                first_roll_d = D_turns[0][1]
                sorted_turns_list.append(D_turns[0])
                D_turns.pop(0)

                # If the first roll was 6, and D is not out of moves, then D can go again.
                if D_turns:
                    if first_roll_d == 6:
                        sorted_turns_list.append(D_turns[0])
                        D_turns.pop(0)

        # print(sorted_turns_list)
        return sorted_turns_list

    def play_game(self, players_list, turns_list):

        self.create_player_list(players_list)            # add player objects to LudoGame object as an array of objects
        sorted_turns_list = self.sort_turns(turns_list)  # sort turns.  A, B, C, D unless roll 6 then player goes twice
        self._turns = sorted_turns_list

        for turn in sorted_turns_list:
            current_player = self.get_player_by_position(turn[0])
            current_roll = turn[1]
            current_player_char = turn[0]
            player_token_p = current_player.get_token_p_step_count()
            player_token_q = current_player.get_token_q_step_count()

            token_choice = self.choose_token_algorithm(current_player, current_roll, player_token_p, player_token_q)

            if token_choice == "No possible move.":
                print("Player " + str(turn[0]) + " can't move! Skipping turn.")
                break   # go to next turn in for loop

            self.move_token(current_player, token_choice, current_roll)

            # self.print_game_board()

        return self.current_spaces_of_all_tokens()

    def current_spaces_of_all_tokens(self):
        token_space = []
        for player in self._players:
            p_steps = player.get_token_p_step_count()
            q_steps = player.get_token_q_step_count()
            p_space = player.get_space_name(p_steps)
            q_space = player.get_space_name(q_steps)
            token_space.append(str(p_space))
            token_space.append(str(q_space))
            #  token_space.append("Player " + str(player.get_position()) +
            #                     " steps [P: " + str(p_space) + "], [Q: " + str(q_space) + "]")


        return token_space

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
                if p_steps != -1:
                    if p_steps != 0:                     # if tokens are not both in ready or home space.
                        return ["P", "Q"]                # tokens are stacked so move both

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

        player_start_space = player.get_start_space()-1  # subtract 1 for pos on board array

        future_board_pos_p = None
        future_board_pos_q = None

        # Test whether token p is in ready to go yard.  Get p token's steps
        if p_steps == 0:
            future_board_pos_p = self.get_board_position_space(player_start_space + current_roll)
        elif p_steps != -1:
            future_board_pos_p = self.get_board_position_space(p_steps + current_roll)

        # Test whether q is in ready to go yard.  Get q token's steps
        if q_steps == 0:
            future_board_pos_q = self.get_board_position_space(player_start_space + current_roll)
        elif q_steps != -1:
            future_board_pos_q = self.get_board_position_space(q_steps + current_roll)

        # if future board pos token p is not empty, and it contains an enemy token
        if future_board_pos_p is not None and future_board_pos_p != "":
            if future_board_pos_p[0] != player.get_position():
                return ["P"]

        # if future board pos token q is not empty, and it contains an enemy token
        if future_board_pos_q is not None and future_board_pos_q != "":
            if future_board_pos_q[0] != player.get_position():
                return ["Q"]

        """Step 4)  Move the token that is furthest from the finishing square.  Don't move if at end step.
           Also don't move token if it's at the home yard as if it were possible to move, would have been handled
           above at the if dice roll 6 conditional lines."""
        if p_steps > q_steps:
            if q_steps != -1:       # debugger breaks if attempting one line:  if q_steps != -1 and q_steps != 57
                if q_steps != 57:
                    return ["Q"]
            if p_steps != -1:
                if p_steps != 57:
                    return ["P"]

        if p_steps < q_steps:
            if p_steps != -1:
                if p_steps != 57:
                    return ["P"]
            if q_steps != -1:
                if q_steps != 57:
                    return ["Q"]

        if p_steps == q_steps:   # if both tokens are in the ready position, and we've already tested for opponents
            if p_steps != 57:
                if p_steps != -1:
                    return ["P"]

        """
        This will be the case where both tokens are in the home yard and the player hasn't rolled a six, or perhaps
        they have won the game, but were still fed a turn into the LudoGame object for some reason.
        """
        return "No possible move."

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
        player_start_space = player_obj.get_start_space()-1     # -1 for pos in board array
        player_end_space = player_obj.get_end_space()-1         # -1 for pos in board array

        token_string = ""
        for token in token_name:
            token_string += (token.lower() + player_pos_char)  # e.g - pA, pB, qA, pAqA

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
            player_obj.set_token_steps(token_name[0], "R")                     # edit player object
            self.set_board_pos_space(token_name[0], 60, player_pos_char, 1)    # clear board pos in home yard
            self.set_board_pos_space(token_name[0], 61, player_pos_char)       # set board pos in ready yard
            return

        """
        If token in home yard, set steps as the player start space plus board steps to move.
          
        If not in home yard, set steps as the step_count, which has the start space now already built in, 
        and the steps to move.
           
        This variable, future_board_pos, will be used to determine if the board space is occupied.
        """
        if step_count == 0:
            future_board_pos = player_start_space + board_steps-1  # if in home yard set steps plus start pos
        else:
            future_board_pos = step_count + board_steps      # else add steps to board_count where start pos already in

        # handle B, C, and D positions which have to move from board space 56 (index 55) to space 1 (index 0):
        if future_board_pos > 55:
            if player_pos_char != 'A':
                future_board_pos = future_board_pos - 55

        """
        This determines whether the future board position will be in the player's home rows.  It adds backtracking if
        the die roll is not the exact roll needed to enter the end "E" space of the game board.   
        
        It also tests to make sure      
        """
        home_row_spaces = None

        if player_pos_char != 'A':
            if future_board_pos > player_end_space:                      # test if position over end space
                if future_board_pos < player_start_space:                # test if position also less than start space
                    home_row_spaces = future_board_pos - player_end_space
                    if home_row_spaces > 6:
                        steps_to_backtrack = home_row_spaces - 6
                        home_row_spaces = home_row_spaces - steps_to_backtrack

        if player_pos_char == 'A':
            if future_board_pos > player_end_space:                      # test if position over end space
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
            future_board_pos_space = self.get_board_position_space(future_board_pos)

            if future_board_pos_space != "" and future_board_pos_space[-1] != player_pos_char:
                self.kick_out_opponent_tokens(future_board_pos, future_board_pos_space)

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
            self.set_board_pos_space(token_string, future_board_pos)  # set board position (not +1 as array)
            for token in token_name:
                player_obj.set_token_steps(token, future_board_pos + 1 - player_start_space)      # set token info in player object. +1

    def kick_out_opponent_tokens(self, future_board_pos, future_board_pos_space):

        """
        This function kicks an opponent's token or stacked tokens back to that opponent's home yard, or position -1.

        It edits both the board data variable of the LudoGame object, and the token information of the player object.

        If the tokens are stacked, it kicks back both.  Or kicks back one if not stacked.

        To do this, it scrapes the text on the board space to determine what player object and token/tokens to edit.

        :param      future_board_pos:         steps on the board where the enemy token is
        :param      future_board_pos_space:   the token that is actually on that board space.
        :return:    none
        """

        opponent_pos_letter = future_board_pos_space[-1]
        opponent_player_obj = self.get_player_by_position(opponent_pos_letter)

        if len(future_board_pos) == 2:                                                   # e.g - pA, pB, qA
            opponent_token = future_board_pos_space[0]
            opponent_player_obj.set_token_steps(opponent_token.upper(), "H")             # kick back to home yard
            self.set_board_pos_space(opponent_token, 60, opponent_pos_letter)            # set board pos in home yard
        else:                                                                            # e.g - pAqA or pBqB
            opponent_token_p = future_board_pos_space[0]
            opponent_token_q = future_board_pos_space[2]
            opponent_player_obj.set_token_steps(opponent_token_p.upper(), "H")           # kick back to home yard
            opponent_player_obj.set_token_steps(opponent_token_q.upper(), "H")           # kick back to home yard
            self.set_board_pos_space(opponent_token_p, 60, opponent_pos_letter)          # set board pos in home yard
            self.set_board_pos_space(opponent_token_q, 60, opponent_pos_letter)          # set board pos in home yard

        self.set_board_pos_space("", future_board_pos)          # clear opponent token or tokens from board space

    def move_to_home_rows(self, player_pos_char, player_obj, token_name, future_board_pos, home_row_spaces):

        # home_rows_player_A = pos 56
        # home_rows_player_B = pos 57
        # home_rows_player_C = pos 58
        # home_rows_player_D = pos 59

        for token in token_name:
            if player_pos_char == "A":
                player_obj.set_token_steps(token, str(player_pos_char + home_row_spaces))
                self.set_board_pos_space(token_name, 56, home_row_spaces)
            elif player_pos_char == "B":
                player_obj.set_token_steps(token, str(player_pos_char + home_row_spaces))
                self.set_board_pos_space(token_name, 57, home_row_spaces)
            elif player_pos_char == "C":
                player_obj.set_token_steps(token, str(player_pos_char + home_row_spaces))
                self.set_board_pos_space(token_name, 58, home_row_spaces)
            elif player_pos_char == "D":
                player_obj.set_token_steps(token, str(player_pos_char + home_row_spaces))
                self.set_board_pos_space(token_name, 59, home_row_spaces)

    def set_board_pos_space(self, token, board_pos, board_pos2=None, clear=None):

        # board_pops2 = home rows before end space
        if board_pos == 60:
            if clear is not None:
                if token == 'P':
                    self._board[board_pos][board_pos2][0] = ""
                if token == 'Q':
                    self._board[board_pos][board_pos2][1] = ""
            else:
                if token == 'P':
                    self._board[board_pos][board_pos2][0] = "P"
                if token == 'Q':
                    self._board[board_pos][board_pos2][1] = "Q"
            return

        if board_pos == 61:
            if clear is not None:
                if token == 'P':
                    self._board[board_pos][board_pos2][0] = ""
                if token == 'Q':
                    self._board[board_pos][board_pos2][1] = ""
            else:
                if token == 'P':
                    self._board[board_pos][board_pos2][0] = "P"
                if token == 'Q':
                    self._board[board_pos][board_pos2][1] = "Q"
            return

        if board_pos2 is not None:
            self._board[board_pos][board_pos2] += token
        else:
            self._board[board_pos] += token

    def get_board_position_space(self, board_pos):
        return self._board[board_pos]

    def create_player_list(self, players_list):

        for position in players_list:
            self._players.append(Player(position))
            self.set_board_pos_space("P", 60, position)
            self.set_board_pos_space("Q", 60, position)

    def print_game_board(self):
        """
        This prints the array and 4 sub-arrays to the console in a form that actually looks like a Ludo board.
        :return:
        """

        print("Home Yard Spaces:  " + str(self._board[60]))
        print("Ready Yard Spaces:  " + str(self._board[61]))
        print("")

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
                        print("[  ]", end="")

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

    def set_token_steps(self, token, pos):
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

    turns2 = [('A', 6), ('A', 6), ('A', 5), ('A', 5), ('B', 6), ('B', 4), ('B', 1), ('B', 2), ('A', 3), ('A', 4),
             ('A', 6), ('A', 3), ('A', 5), ('A', 1), ('A', 5), ('A', 4), ('B', 4), ('B', 4), ('B', 4), ('B', 4)]

    turns3 = [('A', 6), ('A', 4)]

    game = LudoGame()
    # game.play_game(players, turns)
    # game.play_game(players, turns2)
    token_space = game.play_game(players, turns3)
    print(token_space)
    game.print_game_board()

    # print_walk_around_board()

def print_walk_around_board():
    game = LudoGame()
    # game.print_game_board()
    # game._board[28] = "A_P"
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
