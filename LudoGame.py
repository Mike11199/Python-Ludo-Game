class LudoGame:

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

    def play_game(self, players_list, turns_list):
        pass


class Player:

    def get_completed(self):
        """:return: true if player has finished the game, or false it not finished."""
        pass

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

    current_tokens_space = game.play_game(players, turns)
    player_A = game.get_player_by_position('A')

    print(player_A.get_completed())
    print(player_A.get_token_p_step_count())
    print(current_tokens_space)

    player_B = game.get_player_by_position('B')

    print(player_B.get_space_name(55))


if __name__ == '__main__':
    main()