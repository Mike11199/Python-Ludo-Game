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
    This represents the Ludo game being currently played.  It contains an array which represents the board.  This array
    is created when the LudoGame object is initialized.

    This array also contains spaces for the home rows for all players, the home yard, and ready positions, as nested
    lists in board positions 56 to 61.  Each player has a unique series of home rows that only it can enter, that a
    token can move into on its 51st step.  Players pass home rows of other players.

    Players B,C, and D are special cases in that they start at positions other than 1 (B:15, C:29, D:53), and have to
    circle around the board to enter their home space.  Different procedures take this into account, where the step
    count of these players (other than A) will not reflect their actual position on the board (e.g- Player B's first
    step onto the board is space 15 and enters the home row at space 8, while player B starts at 29 and enters at 22).
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
        THIS FUNCTION IS NOT USED ANY LONGER AS IT WAS CAUSING GRADESCOPE TESTS TO FAIL.  THE GRADESCOPE TEST USE THE
        MOVES IN ORDER OF THE LIST, NOT THE ORDER PROPOSED HERE.

        This sorts the list of tuples that represents the move order of the game.  A goes first, then B, then C, then D.

        If anyone rolls a 6, that player can go again (one time, not again if they roll two sixes in a row).

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
        """
        This function takes a list of the players in the game e.g. - [A, B, C, D] and turns list with tuples of each
        move e.g- [('A', 6), ('A', 4), ('A', 5)] and plays the Ludo Game, calling other procedures as necessary.

        After this function finishes, the LudoGame object's state will reflect the result of the game, storing player
        positions.  The player objects will also be updated with whether a player has won the game.

        :param players_list:   List of players.  This is used to append player objects to the board game class.

        :param turns_list:     This is a list of tuples, containing the player and turns for each move of the game.  It
                               is assumed that this list contains the correct order of moves, taking into account if a
                               player rolls a 6 and can go again.  This function previously sorted the turns to make
                               sure of this, but the GradeScope tests do not take this into account.

        :return:                A list of strings containing all the board spaces of each player's tokens.  For example,
                                it might return [E, E, 20, 25] if both of Player A's tokens are in the end space, and if
                                Player B's P token is in space 20, and Player B's Q token is in space 25.

                                It uses the self.current_spaces_of_all_tokens() to return this list.
        """

        self.create_player_list(players_list)            # add player objects to LudoGame object as an array of objects
        # sorted_turns_list = self.sort_turns(turns_list)  # sort turns.  A, B, C, D unless roll 6 then player twice
        # self._turns = sorted_turns_list
        self._turns = turns_list

        for turn in turns_list:
            current_player = self.get_player_by_position(turn[0])
            current_roll = turn[1]
            current_player_char = turn[0]
            player_token_p = current_player.get_token_p_step_count()
            player_token_q = current_player.get_token_q_step_count()

            token_choice = self.choose_token_algorithm(current_player, current_roll, player_token_p, player_token_q)

            if token_choice == "No possible move.":
                # print("Player " + str(turn[0]) + " can't move! Skipping turn.")
                continue   # go to next turn in for loop

            self.move_token(current_player, token_choice, current_roll)
            self.update_players_actual_token_spaces_board_positions_not_steps()

            for player in self._players:
                player.set_player_status_as_completed_if_finished()
                # self.print_game_board()

        return self.current_spaces_of_all_tokens()

    def current_spaces_of_all_tokens(self):
        """
        This function takes no parameters, is what the play_game() function of the LudoGame class returns.  It returns
        a list of strings showing every player's location on the board.  It has to take into account that the step count
        for each player is unique, due to each player's unique start and end space, which adds significant complexity
        to this program.

        It does this by looping through each player object that is listed in the board class and using that player's
        get_actual_board_spaces_for_tokens() method.

        :return:     A list of strings containing all the board spaces of each player's tokens.  For example,
                     it might return [E, E, 20, 25] if both of Player A's tokens are in the end space, and if
                     Player B's P token is in space 20, and Player B's Q token is in space 25.
        """
        token_space = []
        for player in self._players:

            p_actual_board_space = player.get_actual_board_spaces_for_tokens("P")
            q_actual_board_space = player.get_actual_board_spaces_for_tokens("Q")

            if p_actual_board_space == '-1':
                p_actual_board_space = "H"

            if q_actual_board_space == '-1':
                q_actual_board_space = "H"

            if p_actual_board_space == '0':
                p_actual_board_space = "R"

            if q_actual_board_space == '0':
                q_actual_board_space = "R"

            token_space.append(str(p_actual_board_space))
            token_space.append(str(q_actual_board_space))

        return token_space

    def update_players_actual_token_spaces_board_positions_not_steps(self):
        """
        This function takes no parameters, and is used to update each player object's data member which keeps track of
        its tokens positions as spaces on the board.  This is separate from the player's objects data member which
        tracks how many steps each token has taken.

        This will loop through each player in the board game class, obtain its step count, and based on that step count
        and each unique player, will update that player's board steps.

        For example, player B's 5 steps will lead to that token being updated to space 19, while for Player C, 5 steps
        will update the space as 33.

        :return:     A list of strings containing all the board spaces of each player's tokens.
        """
        token_space = []
        for player in self._players:

            p_steps = player.get_token_p_step_count()
            q_steps = player.get_token_q_step_count()

            p_space = player.get_space_name(p_steps)
            q_space = player.get_space_name(q_steps)

            player.set_actual_board_spaces_for_tokens('P', str(p_space))
            player.set_actual_board_spaces_for_tokens('Q', str(q_space))

        return token_space

    def choose_token_algorithm(self, player, current_roll, p_steps, q_steps):
        """
        This function implements the algorithm to decide which of the player's two tokens they should move.  Or if the
        tokens will be stacked.  Steps the algorithm takes are broken out in further doc strings below.

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
        Step 1/2) If the die roll is 6, if a token is in the home yard, return that token to move.  Checks P first so if
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

        future_board_space_p = None
        future_board_space_q = None

        # Test whether token p is in ready to go or on board.  Get p token's steps
        if p_steps == 0:
            future_board_space_p = self.get_board_position_space(player_start_space + current_roll)
        elif p_steps != -1:
            future_pos_p = p_steps + current_roll + player_start_space - 1
            if future_pos_p > 56:                   # test or else will return list of home rows when s/b blank
                future_board_space_p = ""
            else:
                future_board_space_p = self.get_board_position_space(future_pos_p)

        # Test whether token q is in ready to go or on board.  Get q token's steps
        if q_steps == 0:
            future_board_space_q = self.get_board_position_space(player_start_space + current_roll)
        elif q_steps != -1:
            future_pos_q = q_steps + current_roll + player_start_space - 1
            if future_pos_q > 56:                   # test or else will return list of home rows when s/b blank
                future_board_space_q = ""
            else:
                future_board_space_q = self.get_board_position_space(future_pos_q)

        # if future board pos token p is not empty, and it contains an enemy token
        if future_board_space_p is not None and future_board_space_p != "":
            if future_board_space_p[0] != player.get_position():
                if p_steps != 57:
                    return ["P"]

        # if future board pos token q is not empty, and it contains an enemy token
        if future_board_space_q is not None and future_board_space_q != "":
            if future_board_space_q[0] != player.get_position():
                if q_steps != 57:
                    return ["Q"]

        """
        Step 4)  Move the token that is furthest from the finishing square.  Don't move if at end step.
        Also don't move token if it's at the home yard as if it were possible to move, would have been handled
        above at the if dice roll 6 conditional lines.
        """
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
                                stacked.

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
        If token in ready to go yard, set steps as the player start space plus board steps to move.  Also, remove the 
        token from the board position in the ready to go yard.
              
        If not in the ready to go yard, set steps as the step_count, which has the start space now already built in, 
        plus the steps to move.
           
        This variable, future_board_pos, will be used to determine if the board space is occupied.
        """
        if step_count == 0:                                                                  # if in ready to go yard
            future_board_pos = player_start_space + board_steps-1    # if in ready to go yard set steps plus start pos
            self.set_board_pos_space(token_name[0], 61, player_pos_char, 1)      # clear board pos in ready to go yard
        else:
            future_board_pos = player_start_space + step_count + board_steps - 1  # array so -1 from steps

        # handle B, C, and D positions which have to move from board space 56 (index 55) to space 1 (index 0):
        if future_board_pos > 55:
            if player_pos_char != 'A':
                future_board_pos = future_board_pos - 56

        """
        This determines whether the future board position will be in the player's home rows.  It adds backtracking if
        the die roll is not the exact roll needed to enter the end "E" space of the game board.   
        
        It also tests to make sure      
        """
        home_row_spaces = None
        steps_to_backtrack = None
        future_step_count = step_count + board_steps

        if player_pos_char != 'A':
            if future_board_pos > player_end_space:                                # test if position over end space
                if future_board_pos <= player_start_space or future_step_count > 57:  # test if pos less than start
                    home_row_spaces = future_board_pos - player_end_space - 1   # spaces in array: 0 = B1, C1, D1
                    if home_row_spaces > 6:
                        steps_to_backtrack = home_row_spaces - 6
                        home_row_spaces = home_row_spaces - steps_to_backtrack - 1

        if player_pos_char == 'A':
            if future_board_pos > player_end_space:                          # test if position over end space
                home_row_spaces = future_board_pos - player_end_space - 1    # spaces in array: 0 = A1
                if home_row_spaces > 6:
                    steps_to_backtrack = home_row_spaces - 6
                    home_row_spaces = home_row_spaces - steps_to_backtrack - 1

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
        This section moves the token to the home row spaces (using a function move_to_home_rows to determine what
        home row based on the player char letter) if the home_row_spaces is not empty.
        
        If the home row spaces variables is empty, then we don't need a helper function to decide which home row array
        to enter, and can directly place the token in the board array.  If the token was not moved from the ready to
        go yard, that means it was previously on the board, so that previous board spot is reset to nothing.
        
        Uses for loops to handle the possibility that the tokens are stacked.
        
        Previous lines in this function should have kicked out an opponent's token off the board if it was present.
        """

        past_home_row = 56 - player_start_space

        """edit board positions"""
        if step_count > 0:
            if step_count <= 50:
                if future_board_pos < player_start_space and step_count > past_home_row:
                    self.set_board_pos_space("", future_board_pos - board_steps, None, 1)  # clear prev board pos
                else:
                    self.set_board_pos_space("", step_count + player_start_space - 1, None, 1)  # norm clear prev board

        if home_row_spaces is not None:
            self.move_to_home_rows(player_pos_char, player_obj, token, home_row_spaces, future_board_pos, token_string,
                                   step_count, board_steps, steps_to_backtrack)
        else:
            self.set_board_pos_space(token_string, future_board_pos)        # set board position (not +1 as array)

            """edit player obj positions"""
            for token in token_name:
                # set token info in player object. +1 as steps not array pos.  For loop if stacked token.
                player_steps_to_add = future_board_pos + 1 - player_start_space

                if player_steps_to_add < 0:
                    player_steps_to_add = step_count + board_steps

                player_obj.set_token_steps(token, player_steps_to_add)

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

        if len(future_board_pos_space) == 2:                                                   # e.g - pA, pB, qA
            opponent_token = future_board_pos_space[0].upper()
            opponent_player_obj.set_token_steps(opponent_token, "H")              # kick back to home yard player obj
            self.set_board_pos_space(opponent_token, 60, opponent_pos_letter)     # set board pos in home yard on board
            self.set_board_pos_space("", future_board_pos, None, 1)               # clear B tokens from board

        else:                                                                            # e.g - pAqA or pBqB
            opponent_token_p = future_board_pos_space[0].upper()
            opponent_token_q = future_board_pos_space[2].upper()
            opponent_player_obj.set_token_steps(opponent_token_p, "H")                  # kick back to home yard
            opponent_player_obj.set_token_steps(opponent_token_q, "H")                  # kick back to home yard
            self.set_board_pos_space(opponent_token_p, 60, opponent_pos_letter)         # set board pos in home yard
            self.set_board_pos_space(opponent_token_q, 60, opponent_pos_letter)         # set board pos in home yard
            self.set_board_pos_space("", future_board_pos, None, 1)                     # clear B tokens from board

    def move_to_home_rows(self, p_char, player_obj, token_name, home_row_spaces, future_board_pos_space, token_string,
                          step_count, board_steps, steps_to_backtrack):
        """
        This function










        :param p_char:
        :param player_obj:
        :param token_name:
        :param home_row_spaces:
        :param future_board_pos_space:
        :param token_string:
        :param step_count:
        :param board_steps:
        :param steps_to_backtrack:
        :return:
        """
        # home_rows_player_A = pos 56
        # home_rows_player_B = pos 57
        # home_rows_player_C = pos 58
        # home_rows_player_D = pos 59
        future_board_pos_space += 1

        if step_count > 50:
            past_home_space_pos = step_count - 51

        if steps_to_backtrack is not None:
            steps_to_backtrack += 1

        for token in token_name:

            if p_char == "A":
                if step_count > 50:
                    self.set_board_pos_space("", 56, past_home_space_pos, 1)  # clear old board pos
                self.set_board_pos_space(token_string, 56, home_row_spaces)  # set new board pos
                if steps_to_backtrack is not None:
                    player_obj.set_token_steps(token, future_board_pos_space - steps_to_backtrack)  # player obj steps
                else:
                    player_obj.set_token_steps(token, future_board_pos_space)  # set player obj steps - no backtracking

            elif p_char == "B":
                if step_count > 50:
                    self.set_board_pos_space("", 57, past_home_space_pos, 1)  # clear old board pos
                self.set_board_pos_space(token_string, 57, home_row_spaces)  # set new board pos
                if steps_to_backtrack is not None:
                    player_obj.set_token_steps(token,  step_count + board_steps - steps_to_backtrack)  # player steps
                else:
                    player_obj.set_token_steps(token, step_count + board_steps)

            elif p_char == "C":
                if step_count > 50:
                    self.set_board_pos_space("", 58, past_home_space_pos, 1)  # clear old board pos
                self.set_board_pos_space(token_string, 58, home_row_spaces)  # set new board pos
                if steps_to_backtrack is not None:
                    player_obj.set_token_steps(token,  step_count + board_steps - steps_to_backtrack)  # player steps
                else:
                    player_obj.set_token_steps(token, step_count + board_steps)

            elif p_char == "D":
                if step_count > 50:
                    self.set_board_pos_space("", 59, past_home_space_pos, 1)  # clear old board pos
                self.set_board_pos_space(token_string, 59, home_row_spaces)  # set new board pos
                if steps_to_backtrack is not None:
                    player_obj.set_token_steps(token,  step_count + board_steps - steps_to_backtrack)  # player steps
                else:
                    player_obj.set_token_steps(token, step_count + board_steps)

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
            if clear is not None:
                self._board[board_pos][board_pos2] = token
            else:
                self._board[board_pos][board_pos2] += token
        else:
            if clear is not None:
                self._board[board_pos] = token
            else:
                self._board[board_pos] += token

    def get_board_position_space(self, board_pos):
        return self._board[board_pos]

    def get_entire_board(self):
        return self._board

    def get_entire_board_dictionary(self):
        board_dictionary = {}
        for index, item in enumerate(self._board):

            if index < 56:
                if item != "":
                    board_dictionary.update({index: item})

            elif index == 56:
                home_list = []
                for index2, item2 in enumerate(item):
                    home_board = [index2, item2]
                    if item2 != "":
                        home_list.append(home_board)
                        board_dictionary.update({index: home_list})

            elif index == 57:
                home_list = []
                for index2, item2 in enumerate(item):
                    home_board = [index2, item2]
                    if item2 != "":
                        home_list.append(home_board)
                        board_dictionary.update({index: home_list})

            elif index == 58:
                home_list = []
                for index2, item2 in enumerate(item):
                    home_board = [index2, item2]
                    if item2 != "":
                        home_list.append(home_board)
                        board_dictionary.update({index: home_list})

            elif index == 59:
                home_list = []
                for index2, item2 in enumerate(item):
                    home_board = [index2, item2]
                    if item2 != "":
                        home_list.append(home_board)
                        board_dictionary.update({index: home_list})

            elif index == 60:
                board_dictionary.update({"Home Yard": item})

            elif index == 61:
                board_dictionary.update({"Ready to Go Yard": item})

        return board_dictionary

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

        self._token_positions_as_steps = {"P": "H", "Q": "H"}        # H = home yard; R = ready to go; these are as steps taken
        self._game_status = False
        self._token_positions_as_exact_board_space = {"P": "-1", "Q": "-1"}

    def get_position(self):                                 # e.g- "A", "B", "C", or "D"
        return self._position

    def set_token_steps(self, token, pos):
        self._token_positions_as_steps[token] = pos

    def set_actual_board_spaces_for_tokens(self, token, pos):
        self._token_positions_as_exact_board_space[token] = pos

    def get_actual_board_spaces_for_tokens(self, token):
        return self._token_positions_as_exact_board_space[token]

    def set_player_status_as_completed_if_finished(self):
        """:return: true if player has finished the game, or false it not finished."""
        p_token = self.get_token_p_step_count()
        q_token = self.get_token_q_step_count()

        if p_token == 57 and q_token == 57:
            self._game_status = True

    def get_completed(self):
        """:return: true if player has finished the game, or false it not finished."""
        return self._game_status

    def get_token_p_step_count(self):                        # H = -1, R = 0, s/b no more than 57
        steps = self._token_positions_as_steps["P"]
        if steps == "H":
            return -1
        if steps == "R":
            return 0
        return steps

    def get_token_q_step_count(self):                            # H = -1, R = 0, s/b no more than 57
        steps = self._token_positions_as_steps["Q"]
        if steps == "H":
            return -1
        if steps == "R":
            return 0
        return steps

    def get_space_name(self, total_steps):

        player_char = self.get_position()
        player_start = self.get_start_space()
        player_end = self.get_end_space()
        in_home_row = total_steps > 50
        converted_total_steps_to_board_space = total_steps

        if player_char != 'A':
            steps_that_will_pass_space_56 = 56 - player_start + 2
            if steps_that_will_pass_space_56 > total_steps > 0:
                converted_total_steps_to_board_space += (player_start - 1)
            elif total_steps >= steps_that_will_pass_space_56:
                if total_steps < 51:
                    converted_total_steps_to_board_space = total_steps - steps_that_will_pass_space_56 + 1

        if total_steps == -1:
            return "H"

        elif total_steps == 0:
            return "R"

        elif total_steps <= 50:
            return str(converted_total_steps_to_board_space)

        elif 57 > total_steps > 50:
            return str(self._position) + str(converted_total_steps_to_board_space - 50)

        elif converted_total_steps_to_board_space == 57:
            return "E"

        elif converted_total_steps_to_board_space > 57:
            return self.get_space_name(converted_total_steps_to_board_space - (converted_total_steps_to_board_space - 57))    # recursion if over step limit

    def get_start_space(self):
        return self._start_space

    def get_end_space(self):
        return self._end_space


def main():
    """
    Ignore this section.  This was before test cases were added.
    """
    players = ['A', 'B']
    readme_turns = [('A', 6), ('A', 4), ('A', 5), ('A', 4), ('B', 6), ('B', 4), ('B', 1), ('B', 2), ('A', 6), ('A', 4),
                    ('A', 6), ('A', 3), ('A', 5), ('A', 1), ('A', 5), ('A', 4)]

    turns2 = [('A', 6), ('A', 6), ('A', 5), ('A', 5), ('B', 6), ('B', 4), ('B', 1), ('B', 2), ('A', 3), ('A', 4),
             ('A', 6), ('A', 3), ('A', 5), ('A', 1), ('A', 5), ('A', 4), ('B', 4), ('B', 4), ('B', 4), ('B', 4)]

    turns3 = [('A', 6), ('A', 4)]

    game = LudoGame()
    # game.play_game(players, turns)
    # game.play_game(players, turns2)
    token_space = game.play_game(players, readme_turns)
    print(token_space)
    game.print_game_board()

    # print_walk_around_board()


def print_walk_around_board():
    """
    Ignore.  Used by the main function to repeatedly print the board spaces to test token movement, when the program
    was first being developed.
    """
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

    # print(game._board[5])
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
