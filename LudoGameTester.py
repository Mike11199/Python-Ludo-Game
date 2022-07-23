"""
Name:               Michael Iwanek
GitHub:             https://github.com/osu-cs162-u22/portfolio-Mike11199
GitHub Username:    Mike11199
Assignment:         Portfolio Project
Description:        Ludo Game Unit Tester
Date:               08/11/2022
Class:              CS_162_400_U2022
"""

import unittest
from LudoGame import LudoGame


class TestLinkedList(unittest.TestCase):

    def test_token_player_A_move_P_twice(self):
        players = ['A', 'B']
        turns = [('A', 6), ('A', 4)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        self.assertEqual(['4', 'H', 'H', 'H'], token_space)

    def test_token_player_A_move_all_out_of_home_rows(self):
        players = ['A', 'B']
        turns = [('A', 6), ('A', 6)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        self.assertEqual(['R', 'R', 'H', 'H'], token_space)

    def test_token_player_A_move_all_out_of_home_rows_and_one_token_B(self):
        players = ['A', 'B']
        turns = [('A', 6), ('A', 5), ('B', 6)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        self.assertEqual(['5', 'H', 'R', 'H'], token_space)  # expected, actual

    def test_move_player_A_token_P_to_row_50(self):
        players = ['A', 'B', 'C', 'D']
        turns = [('A', 6), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5),
                 ('A', 5), ('A', 5), ('A', 5), ('A', 5)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        expected = ['50', 'H', 'H', 'H', 'H', 'H', 'H', 'H']
        self.assertEqual(expected, token_space)  # expected, actual

    def test_move_player_A_token_P_to_home_row_A5(self):
        players = ['A', 'B', 'C', 'D']
        turns = [('A', 6), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5),
                 ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        expected = ['A5', 'H', 'H', 'H', 'H', 'H', 'H', 'H']
        self.assertEqual(expected, token_space)  # expected, actual

    def test_move_player_A_token_between_home_rows(self):
        players = ['A', 'B', 'C', 'D']
        turns = [('A', 6), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5),
                 ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 1)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        expected = ['A6', 'H', 'H', 'H', 'H', 'H', 'H', 'H']
        self.assertEqual(expected, token_space)  # expected, actual

    def test_move_player_A_token_between_home_rows_to_end_row(self):
        players = ['A', 'B', 'C', 'D']
        turns = [('A', 6), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5),
                 ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 1), ('A', 1)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        expected = ['E', 'H', 'H', 'H', 'H', 'H', 'H', 'H']
        self.assertEqual(expected, token_space)  # expected, actual

    def test_game_does_not_move_token_in_end_space(self):
        players = ['A', 'B', 'C', 'D']
        turns = [('A', 6), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5),
                 ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 1), ('A', 1), ('A', 1)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        expected = ['E', 'H', 'H', 'H', 'H', 'H', 'H', 'H']
        self.assertEqual(expected, token_space)  # expected, actual

    def test_move_token_q_ready_yard_if_p_at_end_space(self):
        players = ['A', 'B', 'C', 'D']
        turns = [('A', 6), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5),
                 ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 1), ('A', 1),
                 ('A', 1), ('A', 6)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        expected = ['E', 'R', 'H', 'H', 'H', 'H', 'H', 'H']
        self.assertEqual(expected, token_space)  # expected, actual

    def test_moving_both_A_tokens_to_end_space(self):
        players = ['A', 'B', 'C', 'D']
        turns = [('A', 6), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5),
                 ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 1), ('A', 1),  # end space here
                 ('A', 6), ('A', 6), ('A', 6), ('A', 6), ('A', 6), ('A', 6), ('A', 6),   # these lines moves token q
                 ('A', 6),  ('A', 6),  ('A', 6), ('A', 3)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        expected = ['E', 'E', 'H', 'H', 'H', 'H', 'H', 'H']
        self.assertEqual(expected, token_space)  # expected, actual

    def test_A_will_not_move_again_if_both_tokens_in_end_space(self):
        players = ['A', 'B', 'C', 'D']
        turns = [('A', 6), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5),
                 ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 1), ('A', 1),  # end space here
                 ('A', 6), ('A', 6), ('A', 6), ('A', 6), ('A', 6), ('A', 6), ('A', 6),   # these lines moves token q
                 ('A', 6),  ('A', 6),  ('A', 6), ('A', 3), ('A', 1)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        expected = ['E', 'E', 'H', 'H', 'H', 'H', 'H', 'H']
        self.assertEqual(expected, token_space)  # expected, actual

    def test_A_will_not_move_again_if_both_tokens_in_end_space_and_test_B_ready_space(self):
        players = ['A', 'B', 'C', 'D']
        turns = [('A', 6), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5),
                 ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 1), ('A', 1),  # end space here
                 ('A', 6), ('A', 6), ('A', 6), ('A', 6), ('A', 6), ('A', 6), ('A', 6),   # these lines moves token q
                 ('A', 6),  ('A', 6),  ('A', 6), ('A', 3), ('B', 6)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        expected = ['E', 'E', 'R', 'H', 'H', 'H', 'H', 'H']
        self.assertEqual(expected, token_space)  # expected, actual

    def test_B_on_board_being_kicked_off_and_both_A_in_home_space(self):
        players = ['A', 'B', 'C', 'D']
        turns = [('A', 6), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5),
                 ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 1), ('A', 1),  # end space here
                 ('A', 6), ('A', 6), ('A', 6), ('A', 6), ('A', 6), ('A', 6), ('A', 6),  # these lines moves token q
                 ('A', 6), ('A', 6), ('A', 6), ('A', 3), ('B', 6), ('B', 6), ('B', 6)]
        game = LudoGame()
        token_space = game.play_game(players, turns)

        expected = ['E', 'E', 'H', 'R', 'H', 'H', 'H', 'H']
        self.assertEqual(expected, token_space)  # expected, actual

        board_dictionary = game.get_entire_board_dictionary()
        self.assertEqual({56: [6, 'pAqA']}, board_dictionary)  # expected, actual


"""Statement so that file only runs main if ran as a script, not when imported."""
if __name__ == '__main__':
    unittest.main()
