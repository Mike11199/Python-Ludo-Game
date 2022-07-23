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


"""Statement so that file only runs main if ran as a script, not when imported."""
if __name__ == '__main__':
    unittest.main()
