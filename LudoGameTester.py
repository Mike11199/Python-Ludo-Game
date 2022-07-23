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
from LudoGame import LudoGame, Player


class TestLinkedList(unittest.TestCase):

    def test_token_initialization(self):
        players = ['A', 'B']
        turns = [('A', 6), ('A', 4)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        self.assertEqual(token_space, ['4', 'H', 'H', 'H'])


"""Statement so that file only runs main if ran as a script, not when imported."""
if __name__ == '__main__':
    unittest.main()
