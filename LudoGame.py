class LudoGame:
    """

    """

    def __init__(self):
        self._players = []
        self._turns = None
        self._board = []

        home_rows_player_A = ["A1", "A2", "A3", "A4", "A5", "A6", "E"]
        home_rows_player_B = ["B1", "B2", "B3", "B4", "B5", "B6", "E"]
        home_rows_player_C = ["C1", "C2", "C3", "C4", "C5", "C6", "E"]
        home_rows_player_D = ["D1", "D2", "D3", "D4", "D5", "D6", "E"]

        for i in range(1, 57):
            self._board.append("")
        self._board.append(home_rows_player_A)
        self._board.append(home_rows_player_B)
        self._board.append(home_rows_player_C)
        self._board.append(home_rows_player_D)

    def play_game(self, players_list, turns_list):
        self.create_player_list(players_list)

    def create_player_list(self, players_list):

        for position in players_list:
            self._players.append(Player(position))

    def print_game_board(self):

        for i in range(0, 15):
            if self._board[i] == '':
                print("[  ]", end="")
            else:
                print(self._board[i], end="")

        for j in range(0, 13):
            print("")
            for i in range(0, 13):

                if i == 0:
                    if self._board[55 - i] == '':
                        print("[  ]", end="")
                    else:
                        print("[" + self._board[55 - i] + "]", end="")

                if j == 6:
                    if i > 6:
                        if self._board[58][-2-(i-7)] == '':
                            print("[  ]", end="")
                        else:
                            print("[" + self._board[58][-2-(i-7)] + "]", end="")

                    if i == 6:
                        print("[E ]", end="")

                    if i < 6:
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
                    if self._board[29 - i] == '':
                        print("[  ]", end="")
                    else:
                        print("[" + self._board[29 - i] + "]", end="")

                else:
                    if j != 6:
                        print("    ", end="")

        print("")
        for i in range(44, 29, -1):
            if self._board[i] == '':
                print("[  ]", end="")
            else:
                print(self._board[i], end="")
        print("")

    def get_player_by_position(self, player_position):
        """takes as a parameter the player's position as a string and returns the player object, or not found"""
        pass

    def move_token(self, player_object, token_name, board_steps):
        """
        Moves one a player's tokens across the game board a specified number of steps.  It will then update the
        token's total steps and kick out other opponent's tokens as needed.

        If a player's two tokens land on the same space on the board, the player will stack the two tokens, and move
        them as one piece until they reach the finishing square.  The tokens are not stacked if both at home.

        If a player's token lands on a space occupied by an opponent's token, the opponent token will be returned
        or kicked back to its home yard, and can only re-enter into play when the owner rolls a 6.

        :param player_object:   player
        :param token_name:      token name ('p' or 'q') as each player has two tokens
        :param board_steps:     steps the token will take across the board as an int
        :return:                none;
        """
        pass


class Player:

    def __init__(self, position):

        self._position = position

        if self._position == 'A':
            self._start_space = 1
        elif self._position == 'B':
            self._start_space = 15
        elif self._position == 'C':
            self._start_space = 29
        elif self._position == 'D':
            self._start_space = 43

        if self._position == 'A':
            self._end_space = 50
        elif self._position == 'B':
            self._end_space = 8
        elif self._position == 'C':
            self._end_space = 22
        elif self._position == 'D':
            self._end_space = 36

        self._token_positions = {"P": "H", "Q": "H"}
        self._game_status = False

    def get_completed(self):
        """:return: true if player has finished the game, or false it not finished."""
        return self._game_status

    def get_token_p_step_count(self):
        pass

    def get_token_q_step_count(self):
        pass

    def get_space_name(self):
        pass


def main():
    players = ['A', 'B']
    turns = [('A', 6), ('A', 4), ('A', 5), ('A', 4), ('B', 6), ('B', 4), ('B', 1), ('B', 2), ('A', 6), ('A', 4),
             ('A', 6), ('A', 3), ('A', 5), ('A', 1), ('A', 5), ('A', 4)]

    game = LudoGame()
    game.print_game_board()
    game._board[5] = "P-A"
    print(game._board[5])

    # current_tokens_space = game.play_game(players, turns)

    # player_A = game.get_player_by_position('A')

    # print(player_A.get_completed())
    # print(player_A.get_token_p_step_count())
    # print(current_tokens_space)

    # player_B = game.get_player_by_position('B')

    # print(player_B.get_space_name(55))


if __name__ == '__main__':
    main()
