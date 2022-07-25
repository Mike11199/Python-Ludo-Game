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

    def test_player_A_moves_P_token_twice_to_board_space_4(self):
        # Test the function returns correct list of all the tokens
        players = ['A', 'B']
        turns = [('A', 6), ('A', 4)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        self.assertEqual(['4', 'H', 'H', 'H'], token_space)

        # Test the board spaces and home/ready-to-go yards
        board_dictionary = game.get_entire_board_dictionary()
        expected = {3: 'pA',
                    'Home Yard':
                        {'A': ['', 'Q'],
                         'B': ['P', 'Q'],
                         'C': ['', ''],
                         'D': ['', '']},
                    'Ready to Go Yard':
                        {'A': ['', ''],
                         'B': ['', ''],
                         'C': ['', ''],
                         'D': ['', '']}}
        self.assertEqual(expected, board_dictionary)  # expected, actual

    def test_player_A_moves_both_their_tokens_out_of_home_yard_to_ready_to_go_yard(self):
        # Test the function returns correct list of all the tokens
        players = ['A', 'B']
        turns = [('A', 6), ('A', 6)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        self.assertEqual(['R', 'R', 'H', 'H'], token_space)

        # Test the board spaces and home/ready-to-go yards
        board_dictionary = game.get_entire_board_dictionary()
        expected = {'Home Yard':
                        {'A': ['', ''],
                         'B': ['P', 'Q'],
                         'C': ['', ''],
                         'D': ['', '']},
                    'Ready to Go Yard':
                        {'A': ['P', 'Q'],
                         'B': ['', ''],
                         'C': ['', ''],
                         'D': ['', '']}}
        self.assertEqual(expected, board_dictionary)  # expected, actual

    def test_player_B_moves_both_their_tokens_out_of_home_yard_to_ready_to_go_yard(self):
        # Test the function returns correct list of all the tokens
        players = ['A', 'B']
        turns = [('B', 6), ('B', 6)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        self.assertEqual(['H', 'H', 'R', 'R'], token_space)

        # Test the board spaces and home/ready-to-go yards
        board_dictionary = game.get_entire_board_dictionary()
        expected = {'Home Yard':
                        {'A': ['P', 'Q'],
                         'B': ['', ''],
                         'C': ['', ''],
                         'D': ['', '']},
                    'Ready to Go Yard':
                        {'A': ['', ''],
                         'B': ['P', 'Q'],
                         'C': ['', ''],
                         'D': ['', '']}}
        self.assertEqual(expected, board_dictionary)  # expected, actual

    def test_player_C_moves_both_their_tokens_out_of_home_yard_to_ready_to_go_yard(self):
        # Test the function returns correct list of all the tokens
        players = ['A', 'C']
        turns = [('C', 6), ('C', 6)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        self.assertEqual(['H', 'H', 'R', 'R'], token_space)

        # Test the board spaces and home/ready-to-go yards
        board_dictionary = game.get_entire_board_dictionary()
        expected = {'Home Yard':
                        {'A': ['P', 'Q'],
                         'B': ['', ''],
                         'C': ['', ''],
                         'D': ['', '']},
                    'Ready to Go Yard':
                        {'A': ['', ''],
                         'B': ['', ''],
                         'C': ['P', 'Q'],
                         'D': ['', '']}}
        self.assertEqual(expected, board_dictionary)  # expected, actual

    def test_player_D_moves_both_their_tokens_out_of_home_yard_to_ready_to_go_yard(self):
        # Test the function returns correct list of all the tokens
        players = ['A', 'D']
        turns = [('D', 6), ('D', 6)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        self.assertEqual(['H', 'H', 'R', 'R'], token_space)

        # Test the board spaces and home/ready-to-go yards
        board_dictionary = game.get_entire_board_dictionary()
        expected = {'Home Yard':
                        {'A': ['P', 'Q'],
                         'B': ['', ''],
                         'C': ['', ''],
                         'D': ['', '']},
                    'Ready to Go Yard':
                        {'A': ['', ''],
                         'B': ['', ''],
                         'C': ['', ''],
                         'D': ['P', 'Q']}}
        self.assertEqual(expected, board_dictionary)  # expected, actual

    def test_player_A_moves_token_p_to_board_space_5_and_player_B_moves_token_p_to_ready_to_go_yard(self):
        # Test the function returns correct list of all the tokens
        players = ['A', 'B']
        turns = [('A', 6), ('A', 5), ('B', 6)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        self.assertEqual(['5', 'H', 'R', 'H'], token_space)  # expected, actual

        # Test the board spaces and home/ready-to-go yards
        board_dictionary = game.get_entire_board_dictionary()
        expected = {4: 'pA',
                    'Home Yard':
                        {'A': ['', 'Q'],
                         'B': ['', 'Q'],
                         'C': ['', ''],
                         'D': ['', '']},
                    'Ready to Go Yard':
                        {'A': ['', ''],
                         'B': ['P', ''],
                         'C': ['', ''],
                         'D': ['', '']}}
        self.assertEqual(expected, board_dictionary)  # expected, actual

    def test_player_A_moves_token_P_to_board_space_50(self):
        # Test the function returns correct list of all the tokens
        players = ['A', 'B', 'C', 'D']
        turns = [('A', 6), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5),
                 ('A', 5), ('A', 5), ('A', 5), ('A', 5)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        expected = ['50', 'H', 'H', 'H', 'H', 'H', 'H', 'H']
        self.assertEqual(expected, token_space)  # expected, actual

        # Test the board spaces and home/ready-to-go yards
        board_dictionary = game.get_entire_board_dictionary()
        expected = {49: 'pA',
                    'Home Yard':
                        {'A': ['', 'Q'],
                         'B': ['P', 'Q'],
                         'C': ['P', 'Q'],
                         'D': ['P', 'Q']},
                    'Ready to Go Yard':
                        {'A': ['', ''],
                         'B': ['', ''],
                         'C': ['', ''],
                         'D': ['', '']}}
        self.assertEqual(expected, board_dictionary)  # expected, actual

    def test_player_A_moves_token_p_to_board_space_A1_from_50(self):
        # Test the function returns correct list of all the tokens
        players = ['A', 'B', 'C', 'D']
        turns = [('A', 6), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5),
                 ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 1)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        expected = ['A1', 'H', 'H', 'H', 'H', 'H', 'H', 'H']
        self.assertEqual(expected, token_space)  # expected, actual

        # Test the board spaces and home/ready-to-go yards
        board_dictionary = game.get_entire_board_dictionary()
        expected = {56: [[0, 'pA']],
                    'Home Yard':
                        {'A': ['', 'Q'],
                         'B': ['P', 'Q'],
                         'C': ['P', 'Q'],
                         'D': ['P', 'Q']},
                    'Ready to Go Yard':
                        {'A': ['', ''],
                         'B': ['', ''],
                         'C': ['', ''],
                         'D': ['', '']}}
        self.assertEqual(expected, board_dictionary)  # expected, actual

    def test_player_A_moves_token_P_to_home_row_A5(self):
        # Test the function returns correct list of all the tokens
        players = ['A', 'B', 'C', 'D']
        turns = [('A', 6), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5),
                 ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        expected = ['A5', 'H', 'H', 'H', 'H', 'H', 'H', 'H']
        self.assertEqual(expected, token_space)  # expected, actual

        # Test the board spaces and home/ready-to-go yards
        board_dictionary = game.get_entire_board_dictionary()
        expected = {56: [[4, 'pA']],
                    'Home Yard':
                        {'A': ['', 'Q'],
                         'B': ['P', 'Q'],
                         'C': ['P', 'Q'],
                         'D': ['P', 'Q']},
                    'Ready to Go Yard':
                        {'A': ['', ''],
                         'B': ['', ''],
                         'C': ['', ''],
                         'D': ['', '']}}
        self.assertEqual(expected, board_dictionary)  # expected, actual

    def test_player_A_moves_p_token_from_one_home_row_to_another(self):
        # Test the function returns correct list of all the tokens
        players = ['A', 'B', 'C', 'D']
        turns = [('A', 6), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5),
                 ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 1)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        expected = ['A6', 'H', 'H', 'H', 'H', 'H', 'H', 'H']
        self.assertEqual(expected, token_space)  # expected, actual

        # Test the board spaces and home/ready-to-go yards
        board_dictionary = game.get_entire_board_dictionary()
        expected = {56: [[5, 'pA']],
                    'Home Yard':
                        {'A': ['', 'Q'],
                         'B': ['P', 'Q'],
                         'C': ['P', 'Q'],
                         'D': ['P', 'Q']},
                    'Ready to Go Yard':
                        {'A': ['', ''],
                         'B': ['', ''],
                         'C': ['', ''],
                         'D': ['', '']}}
        self.assertEqual(expected, board_dictionary)  # expected, actual

    def test_player_A_moves_token_p_between_home_rows_to_end_space(self):
        # Test the function returns correct list of all the tokens
        players = ['A', 'B', 'C', 'D']
        turns = [('A', 6), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5),
                 ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 1), ('A', 1)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        expected = ['E', 'H', 'H', 'H', 'H', 'H', 'H', 'H']
        self.assertEqual(expected, token_space)  # expected, actual

        # Test the board spaces and home/ready-to-go yards
        board_dictionary = game.get_entire_board_dictionary()
        expected = {56: [[6, 'pA']],
                    'Home Yard':
                        {'A': ['', 'Q'],
                         'B': ['P', 'Q'],
                         'C': ['P', 'Q'],
                         'D': ['P', 'Q']},
                    'Ready to Go Yard':
                        {'A': ['', ''],
                         'B': ['', ''],
                         'C': ['', ''],
                         'D': ['', '']}}
        self.assertEqual(expected, board_dictionary)  # expected, actual

    def test_backtracking_in_home_rows_for_player_A_if_exact_roll_to_enter_end_space_not_rolled(self):
        # Test the function returns correct list of all the tokens
        players = ['A', 'B', 'C', 'D']
        turns = [('A', 6), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5),
                 ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 4), ('A', 4)]  # last move is one over end space
        game = LudoGame()
        token_space = game.play_game(players, turns)
        expected = ['A6', 'H', 'H', 'H', 'H', 'H', 'H', 'H']
        self.assertEqual(expected, token_space)  # expected, actual

        # Test the board spaces and home/ready-to-go yards
        board_dictionary = game.get_entire_board_dictionary()
        expected = {56: [[5, 'pA']],
                    'Home Yard':
                        {'A': ['', 'Q'],
                         'B': ['P', 'Q'],
                         'C': ['P', 'Q'],
                         'D': ['P', 'Q']},
                    'Ready to Go Yard':
                        {'A': ['', ''],
                         'B': ['', ''],
                         'C': ['', ''],
                         'D': ['', '']}}
        self.assertEqual(expected, board_dictionary)  # expected, actual

    def test_Player_A_does_not_move_token_p_already_in_end_space(self):
        # Test the function returns correct list of all the tokens
        players = ['A', 'B', 'C', 'D']
        turns = [('A', 6), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5),
                 ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 1), ('A', 1), ('A', 3)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        expected = ['E', 'H', 'H', 'H', 'H', 'H', 'H', 'H']
        self.assertEqual(expected, token_space)  # expected, actual

        # Test the board spaces and home/ready-to-go yards
        board_dictionary = game.get_entire_board_dictionary()
        expected = {56: [[6, 'pA']],
                    'Home Yard':
                        {'A': ['', 'Q'],
                         'B': ['P', 'Q'],
                         'C': ['P', 'Q'],
                         'D': ['P', 'Q']},
                    'Ready to Go Yard':
                        {'A': ['', ''],
                         'B': ['', ''],
                         'C': ['', ''],
                         'D': ['', '']}}
        self.assertEqual(expected, board_dictionary)  # expected, actual

    def test_player_A_moves_token_q_to_ready_yard_while_token_p_at_end_space(self):
        # Test the function returns correct list of all the tokens
        players = ['A', 'B', 'C', 'D']
        turns = [('A', 6), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5),
                 ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 1), ('A', 1),
                 ('A', 1), ('A', 6)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        expected = ['E', 'R', 'H', 'H', 'H', 'H', 'H', 'H']
        self.assertEqual(expected, token_space)  # expected, actual

        # Test the board spaces and home/ready-to-go yards
        board_dictionary = game.get_entire_board_dictionary()
        expected = {56: [[6, 'pA']],
                    'Home Yard':
                        {'A': ['', ''],
                         'B': ['P', 'Q'],
                         'C': ['P', 'Q'],
                         'D': ['P', 'Q']},
                    'Ready to Go Yard':
                        {'A': ['', 'Q'],
                         'B': ['', ''],
                         'C': ['', ''],
                         'D': ['', '']}}
        self.assertEqual(expected, board_dictionary)  # expected, actual

    def test_moving_both_player_A_tokens_to_end_space_after_token_p_gets_there_first_while_token_q_in_home_yard(self):
        # Test the function returns correct list of all the tokens
        players = ['A', 'B', 'C', 'D']
        turns = [('A', 6), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5),
                 ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 1), ('A', 1),  # end space here
                 ('A', 6), ('A', 6), ('A', 6), ('A', 6), ('A', 6), ('A', 6), ('A', 6),  # these lines moves token q
                 ('A', 6), ('A', 6), ('A', 6), ('A', 3)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        expected = ['E', 'E', 'H', 'H', 'H', 'H', 'H', 'H']
        self.assertEqual(expected, token_space)  # expected, actual

        # Test the board spaces and home/ready-to-go yards
        board_dictionary = game.get_entire_board_dictionary()
        expected = {56: [[6, 'pAqA']],
                    'Home Yard':
                        {'A': ['', ''],
                         'B': ['P', 'Q'],
                         'C': ['P', 'Q'],
                         'D': ['P', 'Q']},
                    'Ready to Go Yard':
                        {'A': ['', ''],
                         'B': ['', ''],
                         'C': ['', ''],
                         'D': ['', '']}}
        self.assertEqual(expected, board_dictionary)  # expected, actual

    def test_player_A_will_not_move_again_if_both_tokens_are_in_end_space(self):
        # Test the function returns correct list of all the tokens
        players = ['A', 'B', 'C', 'D']
        turns = [('A', 6), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5),
                 ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 1), ('A', 1),  # end space here
                 ('A', 6), ('A', 6), ('A', 6), ('A', 6), ('A', 6), ('A', 6), ('A', 6),  # these lines moves token q
                 ('A', 6), ('A', 6), ('A', 6), ('A', 3), ('A', 1), ('A', 5)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        expected = ['E', 'E', 'H', 'H', 'H', 'H', 'H', 'H']
        self.assertEqual(expected, token_space)  # expected, actual

        # Test the board spaces and home/ready-to-go yards
        board_dictionary = game.get_entire_board_dictionary()
        expected = {56: [[6, 'pAqA']],
                    'Home Yard':
                        {'A': ['', ''],
                         'B': ['P', 'Q'],
                         'C': ['P', 'Q'],
                         'D': ['P', 'Q']},
                    'Ready to Go Yard':
                        {'A': ['', ''],
                         'B': ['', ''],
                         'C': ['', ''],
                         'D': ['', '']}}
        self.assertEqual(expected, board_dictionary)  # expected, actual

    def test_player_A_not_move_again_if_both_tokens_in_end_space_and_test_player_B_token_p_in_ready_space(self):
        # Test the function returns correct list of all the tokens
        players = ['A', 'B', 'C', 'D']
        turns = [('A', 6), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5),
                 ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 1), ('A', 1),  # end space here
                 ('A', 6), ('A', 6), ('A', 6), ('A', 6), ('A', 6), ('A', 6), ('A', 6),  # these lines moves token q
                 ('A', 6), ('A', 6), ('A', 6), ('A', 3), ('B', 6)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        expected = ['E', 'E', 'R', 'H', 'H', 'H', 'H', 'H']
        self.assertEqual(expected, token_space)  # expected, actual

        # Test the board spaces and home/ready-to-go yards
        board_dictionary = game.get_entire_board_dictionary()
        expected = {56: [[6, 'pAqA']],
                    'Home Yard':
                        {'A': ['', ''],
                         'B': ['', 'Q'],
                         'C': ['P', 'Q'],
                         'D': ['P', 'Q']},
                    'Ready to Go Yard':
                        {'A': ['', ''],
                         'B': ['P', ''],
                         'C': ['', ''],
                         'D': ['', '']}}
        self.assertEqual(expected, board_dictionary)  # expected, actual

    def test_player_B_token_p_on_board_being_kicked_off_to_home_yard_and_both_A_tokens_moving_to_end(self):
        # Test the function returns correct list of all the tokens
        players = ['A', 'B', 'C', 'D']
        turns = [('A', 6), ('A', 5), ('B', 6), ('B', 6), ('A', 5), ('B', 6), ('A', 5), ('A', 5), ('A', 5), ('A', 5),
                 ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 1), ('A', 1), ('A', 6), ('A', 6), ('A', 6),
                 ('A', 6), ('A', 6), ('A', 6), ('A', 6), ('A', 6), ('A', 6), ('A', 6), ('A', 3)]

        game = LudoGame()
        token_space = game.play_game(players, turns)

        expected = ['E', 'E', 'H', 'R', 'H', 'H', 'H', 'H']         # third H is token P for B that got kicked to home
        self.assertEqual(expected, token_space)  # expected, actual

        # Test the board spaces and home/ready-to-go yards
        board_dictionary = game.get_entire_board_dictionary()
        expected = {56: [[6, 'pAqA']],
                    'Home Yard':
                        {'A': ['', ''],
                         'B': ['P', ''],
                         'C': ['P', 'Q'],
                         'D': ['P', 'Q']},
                    'Ready to Go Yard':
                        {'A': ['', ''],
                         'B': ['', 'Q'],
                         'C': ['', ''],
                         'D': ['', '']}}
        self.assertEqual(expected, board_dictionary)  # expected, actual

    def test_player_a_creating_a_stacked_token(self):
        # Test the function returns correct list of all the tokens
        players = ['A', 'B']
        turns = [('A', 6), ('A', 5), ('A', 6), ('A', 5)]
        game = LudoGame()
        token_space = game.play_game(players, turns)

        expected = ['5', '5', 'H', 'H']
        self.assertEqual(expected, token_space)  # expected, actual

        # Test the board spaces and home/ready-to-go yards
        board_dictionary = game.get_entire_board_dictionary()
        expected = {4: 'pAqA',
                    'Home Yard':
                        {'A': ['', ''],
                         'B': ['P', 'Q'],
                         'C': ['', ''],
                         'D': ['', '']},
                    'Ready to Go Yard':
                        {'A': ['', ''],
                         'B': ['', ''],
                         'C': ['', ''],
                         'D': ['', '']}}
        self.assertEqual(expected, board_dictionary)  # expected, actual

    def test_player_a_creating_a_stacked_token_and_moving_it(self):
        # Test the function returns correct list of all the tokens
        players = ['A', 'B']
        turns = [('A', 6), ('A', 5), ('A', 6), ('A', 5), ('A', 3)]
        game = LudoGame()
        token_space = game.play_game(players, turns)

        expected = ['8', '8', 'H', 'H']
        self.assertEqual(expected, token_space)  # expected, actual

        # Test the board spaces and home/ready-to-go yards
        board_dictionary = game.get_entire_board_dictionary()
        expected = {7: 'pAqA',
                    'Home Yard':
                        {'A': ['', ''],
                         'B': ['P', 'Q'],
                         'C': ['', ''],
                         'D': ['', '']},
                    'Ready to Go Yard':
                        {'A': ['', ''],
                         'B': ['', ''],
                         'C': ['', ''],
                         'D': ['', '']}}
        self.assertEqual(expected, board_dictionary)  # expected, actual

    def test_the_get_completed_function_for_player_A(self):
        # Test the function returns correct list of all the tokens
        players = ['A', 'B', 'C', 'D']
        turns = [('A', 6), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5),
                 ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 1), ('A', 1),  # end space here
                 ('A', 6), ('A', 6), ('A', 6), ('A', 6), ('A', 6), ('A', 6), ('A', 6),  # these lines moves token q
                 ('A', 6), ('A', 6), ('A', 6), ('A', 3), ('A', 1), ('A', 5)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        expected = ['E', 'E', 'H', 'H', 'H', 'H', 'H', 'H']
        self.assertEqual(expected, token_space)  # expected, actual

        # Test the board spaces and home/ready-to-go yards
        board_dictionary = game.get_entire_board_dictionary()
        expected = {56: [[6, 'pAqA']],
                    'Home Yard':
                        {'A': ['', ''],
                         'B': ['P', 'Q'],
                         'C': ['P', 'Q'],
                         'D': ['P', 'Q']},
                    'Ready to Go Yard':
                        {'A': ['', ''],
                         'B': ['', ''],
                         'C': ['', ''],
                         'D': ['', '']}}
        self.assertEqual(expected, board_dictionary)  # expected, actual

        player_A = game.get_player_by_position('A')
        self.assertEqual(True, player_A.get_completed())  # expected, actual

    def test_the_get_completed_function_for_false_positives(self):
        # Test the function returns correct list of all the tokens
        players = ['A', 'B', 'C', 'D']
        turns = [('A', 6), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5),
                 ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 1), ('A', 1),  # end space here
                 ('A', 6), ('A', 6), ('A', 6), ('A', 6), ('A', 6), ('A', 6), ('A', 6),  # these lines moves token q
                 ('A', 6), ('A', 6), ('A', 6), ('A', 3), ('A', 1), ('A', 5)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        expected = ['E', 'E', 'H', 'H', 'H', 'H', 'H', 'H']
        self.assertEqual(expected, token_space)  # expected, actual

        # Test the board spaces and home/ready-to-go yards
        board_dictionary = game.get_entire_board_dictionary()
        expected = {56: [[6, 'pAqA']],
                    'Home Yard':
                        {'A': ['', ''],
                         'B': ['P', 'Q'],
                         'C': ['P', 'Q'],
                         'D': ['P', 'Q']},
                    'Ready to Go Yard':
                        {'A': ['', ''],
                         'B': ['', ''],
                         'C': ['', ''],
                         'D': ['', '']}}
        self.assertEqual(expected, board_dictionary)  # expected, actual

        player_B = game.get_player_by_position('B')
        self.assertEqual(False, player_B.get_completed())  # expected, actual
        player_C = game.get_player_by_position('C')
        self.assertEqual(False, player_C.get_completed())  # expected, actual
        player_D = game.get_player_by_position('D')
        self.assertEqual(False, player_D.get_completed())  # expected, actual

    def test_player_b_token_p_goes_past_board_space_56_as_end_space_is_8_to_board_space_3(self):
        # Test the function returns correct list of all the tokens
        players = ['A', 'B', 'C', 'D']
        turns = [('B', 6), ('B', 5), ('B', 5), ('B', 5), ('B', 5), ('B', 5), ('B', 5),
                 ('B', 5), ('B', 5), ('B', 5)]  
        game = LudoGame()
        token_space = game.play_game(players, turns)
        #expected = ['H', 'H', '45', 'H', 'H', 'H', 'H', 'H']
        expected = ['H', 'H', '3', 'H', 'H', 'H', 'H', 'H']
        self.assertEqual(expected, token_space)  # expected, actual

        # Test the board spaces and home/ready-to-go yards
        board_dictionary = game.get_entire_board_dictionary()
        expected = {2: 'pB',
                    'Home Yard':
                        {'A': ['P', 'Q'],
                         'B': ['', 'Q'],
                         'C': ['P', 'Q'],
                         'D': ['P', 'Q']},
                    'Ready to Go Yard':
                        {'A': ['', ''],
                         'B': ['', ''],
                         'C': ['', ''],
                         'D': ['', '']}}
        self.assertEqual(expected, board_dictionary)  # expected, actual

    def test_player_b_token_p_goes_goes_to_space_8_last_board_space_before_home_rows(self):
        # Test the function returns correct list of all the tokens
        players = ['A', 'B', 'C', 'D']
        turns = [('B', 6), ('B', 5), ('B', 5), ('B', 5), ('B', 5), ('B', 5), ('B', 5),
                 ('B', 5), ('B', 5), ('B', 5), ('B', 5)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        expected = ['H', 'H', '8', 'H', 'H', 'H', 'H', 'H']
        self.assertEqual(expected, token_space)  # expected, actual

        # Test the board spaces and home/ready-to-go yards
        board_dictionary = game.get_entire_board_dictionary()
        expected = {7: 'pB',
                    'Home Yard':
                        {'A': ['P', 'Q'],
                         'B': ['', 'Q'],
                         'C': ['P', 'Q'],
                         'D': ['P', 'Q']},
                    'Ready to Go Yard':
                        {'A': ['', ''],
                         'B': ['', ''],
                         'C': ['', ''],
                         'D': ['', '']}}
        self.assertEqual(expected, board_dictionary)  # expected, actual

    def test_player_b_token_p_goes_goes_to_home_row_B1(self):
        # Test the function returns correct list of all the tokens
        players = ['A', 'B', 'C', 'D']
        turns = [('B', 6), ('B', 5), ('B', 5), ('B', 5), ('B', 5), ('B', 5), ('B', 5),
                 ('B', 5), ('B', 5), ('B', 5), ('B', 5), ('B', 1)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        expected = ['H', 'H', 'B1', 'H', 'H', 'H', 'H', 'H']
        self.assertEqual(expected, token_space)  # expected, actual

        # Test the board spaces and home/ready-to-go yards
        board_dictionary = game.get_entire_board_dictionary()
        expected = {57: [[0, 'pB']],
                    'Home Yard':
                        {'A': ['P', 'Q'],
                         'B': ['', 'Q'],
                         'C': ['P', 'Q'],
                         'D': ['P', 'Q']},
                    'Ready to Go Yard':
                        {'A': ['', ''],
                         'B': ['', ''],
                         'C': ['', ''],
                         'D': ['', '']}}
        self.assertEqual(expected, board_dictionary)  # expected, actual

    def test_player_b_token_p_goes_goes_to_home_row_B2(self):
        # Test the function returns correct list of all the tokens
        players = ['A', 'B', 'C', 'D']
        turns = [('B', 6), ('B', 5), ('B', 5), ('B', 5), ('B', 5), ('B', 5), ('B', 5),
                 ('B', 5), ('B', 5), ('B', 5), ('B', 5), ('B', 1), ('B', 1)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        expected = ['H', 'H', 'B2', 'H', 'H', 'H', 'H', 'H']
        self.assertEqual(expected, token_space)  # expected, actual

        # Test the board spaces and home/ready-to-go yards
        board_dictionary = game.get_entire_board_dictionary()
        expected = {57: [[1, 'pB']],
                    'Home Yard':
                        {'A': ['P', 'Q'],
                         'B': ['', 'Q'],
                         'C': ['P', 'Q'],
                         'D': ['P', 'Q']},
                    'Ready to Go Yard':
                        {'A': ['', ''],
                         'B': ['', ''],
                         'C': ['', ''],
                         'D': ['', '']}}
        self.assertEqual(expected, board_dictionary)  # expected, actual

    def test_player_b_token_p_goes_goes_to_end_space(self):
        # Test the function returns correct list of all the tokens
        players = ['A', 'B', 'C', 'D']
        turns = [('B', 6), ('B', 5), ('B', 5), ('B', 5), ('B', 5), ('B', 5), ('B', 5),
                 ('B', 5), ('B', 5), ('B', 5), ('B', 5), ('B', 1), ('B', 1), ('B', 5)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        expected = ['H', 'H', 'E', 'H', 'H', 'H', 'H', 'H']
        self.assertEqual(expected, token_space)  # expected, actual

        # Test the board spaces and home/ready-to-go yards
        board_dictionary = game.get_entire_board_dictionary()
        expected = {57: [[6, 'pB']],
                    'Home Yard':
                        {'A': ['P', 'Q'],
                         'B': ['', 'Q'],
                         'C': ['P', 'Q'],
                         'D': ['P', 'Q']},
                    'Ready to Go Yard':
                        {'A': ['', ''],
                         'B': ['', ''],
                         'C': ['', ''],
                         'D': ['', '']}}
        self.assertEqual(expected, board_dictionary)  # expected, actual

    def test_player_b_token_p_goes_backtracking_in_home_row_spaces_to_B6(self):
        # Test the function returns correct list of all the tokens
        players = ['A', 'B', 'C', 'D']
        turns = [('B', 6), ('B', 5), ('B', 5), ('B', 5), ('B', 5), ('B', 5), ('B', 5),
                 ('B', 5), ('B', 5), ('B', 5), ('B', 5), ('B', 1), ('B', 1), ('B', 1), ('B', 5)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        expected = ['H', 'H', 'B6', 'H', 'H', 'H', 'H', 'H']
        self.assertEqual(expected, token_space)  # expected, actual

        # Test the board spaces and home/ready-to-go yards
        board_dictionary = game.get_entire_board_dictionary()
        expected = {57: [[5, 'pB']],
                    'Home Yard':
                        {'A': ['P', 'Q'],
                         'B': ['', 'Q'],
                         'C': ['P', 'Q'],
                         'D': ['P', 'Q']},
                    'Ready to Go Yard':
                        {'A': ['', ''],
                         'B': ['', ''],
                         'C': ['', ''],
                         'D': ['', '']}}
        self.assertEqual(expected, board_dictionary)  # expected, actual

    def test_player_b_token_p_goes_goes_to_end_space_and_will_not_move_again(self):
        # Test the function returns correct list of all the tokens
        players = ['A', 'B', 'C', 'D']
        turns = [('B', 6), ('B', 5), ('B', 5), ('B', 5), ('B', 5), ('B', 5), ('B', 5),
                 ('B', 5), ('B', 5), ('B', 5), ('B', 5), ('B', 1), ('B', 1), ('B', 5), ('B', 5)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        expected = ['H', 'H', 'E', 'H', 'H', 'H', 'H', 'H']
        self.assertEqual(expected, token_space)  # expected, actual

        # Test the board spaces and home/ready-to-go yards
        board_dictionary = game.get_entire_board_dictionary()
        expected = {57: [[6, 'pB']],
                    'Home Yard':
                        {'A': ['P', 'Q'],
                         'B': ['', 'Q'],
                         'C': ['P', 'Q'],
                         'D': ['P', 'Q']},
                    'Ready to Go Yard':
                        {'A': ['', ''],
                         'B': ['', ''],
                         'C': ['', ''],
                         'D': ['', '']}}
        self.assertEqual(expected, board_dictionary)  # expected, actual

    def test_game_returns_string_matching_the_readme_project_sample_output(self):
        # Test the function returns correct list of all the tokens
        players = ['A', 'B']
        turns = [('A', 6), ('A', 4), ('A', 5), ('A', 4), ('B', 6), ('B', 4), ('B', 1), ('B', 2), ('A', 6), ('A', 4),
                 ('A', 6), ('A', 3), ('A', 5), ('A', 1), ('A', 5), ('A', 4)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        expected = ['28', '28', '21', 'H']
        self.assertEqual(expected, token_space)  # expected, actual

        player_A = game.get_player_by_position('A')
        player_A_completed = player_A.get_completed()
        player_A_step_count = player_A.get_token_p_step_count()
        self.assertEqual(False, player_A_completed)  # expected, actual
        self.assertEqual(28, player_A_step_count)  # expected, actual

        player_B = game.get_player_by_position('B')
        player_B_Space_name = player_B.get_space_name(55)
        self.assertEqual("B5", player_B_Space_name)  # expected, actual

        # Test the board spaces and home/ready-to-go yards
        board_dictionary = game.get_entire_board_dictionary()
        expected = {20: 'pB', 27: 'pAqA',
                    'Home Yard':
                        {'A': ['', ''],
                         'B': ['', 'Q'],
                         'C': ['', ''],
                         'D': ['', '']},
                    'Ready to Go Yard':
                        {'A': ['', ''],
                         'B': ['', ''],
                         'C': ['', ''],
                         'D': ['', '']}}
        self.assertEqual(expected, board_dictionary)  # expected, actual

    def test_readme_sample_turns_up_to_turn_12_where_player_A_tokens_should_be_stacked(self):
        # Test the function returns correct list of all the tokens
        players = ['A', 'B']
        turns = [('A', 6), ('A', 4), ('A', 5), ('A', 4), ('B', 6), ('B', 4), ('B', 1), ('B', 2), ('A', 6), ('A', 4),
                 ('A', 6), ('A', 3)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        expected = ['13', '13', '21', 'H']
        self.assertEqual(expected, token_space)  # expected, actual

        # Test the board spaces and home/ready-to-go yards
        board_dictionary = game.get_entire_board_dictionary()
        expected = {12: 'pAqA', 20: 'pB',
                    'Home Yard':
                        {'A': ['', ''],
                         'B': ['', 'Q'],
                         'C': ['', ''],
                         'D': ['', '']},
                    'Ready to Go Yard':
                        {'A': ['', ''],
                         'B': ['', ''],
                         'C': ['', ''],
                         'D': ['', '']}}
        self.assertEqual(expected, board_dictionary)  # expected, actual

    def test_player_c_token_p_goes_to_board_space_33(self):
        # Test the function returns correct list of all the tokens
        players = ['A', 'B', 'C', 'D']
        turns = [('C', 6), ('C', 5)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        expected = ['H', 'H', 'H', 'H', '33', 'H', 'H', 'H']
        self.assertEqual(expected, token_space)  # expected, actual

        # Test the board spaces and home/ready-to-go yards
        board_dictionary = game.get_entire_board_dictionary()
        expected = {32: 'pC',
                    'Home Yard':
                        {'A': ['P', 'Q'],
                         'B': ['P', 'Q'],
                         'C': ['', 'Q'],
                         'D': ['P', 'Q']},
                    'Ready to Go Yard':
                        {'A': ['', ''],
                         'B': ['', ''],
                         'C': ['', ''],
                         'D': ['', '']}}
        self.assertEqual(expected, board_dictionary)  # expected, actual

    def test_player_c_token_p_goes_to_board_space_53_not_into_A_home_rows(self):
        # Test the function returns correct list of all the tokens
        players = ['A', 'B', 'C', 'D']
        turns = [('C', 6), ('C', 5), ('C', 5), ('C', 5), ('C', 5), ('C', 5)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        expected = ['H', 'H', 'H', 'H', '53', 'H', 'H', 'H']
        self.assertEqual(expected, token_space)  # expected, actual

        # Test the board spaces and home/ready-to-go yards
        board_dictionary = game.get_entire_board_dictionary()
        expected = {52: 'pC',
                    'Home Yard':
                        {'A': ['P', 'Q'],
                         'B': ['P', 'Q'],
                         'C': ['', 'Q'],
                         'D': ['P', 'Q']},
                    'Ready to Go Yard':
                        {'A': ['', ''],
                         'B': ['', ''],
                         'C': ['', ''],
                         'D': ['', '']}}
        self.assertEqual(expected, board_dictionary)  # expected, actual

    def test_player_c_token_p_goes_to_board_space_2(self):
        # Test the function returns correct list of all the tokens
        players = ['A', 'B', 'C', 'D']
        turns = [('C', 6), ('C', 5), ('C', 5), ('C', 5), ('C', 5), ('C', 5), ('C', 5)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        expected = ['H', 'H', 'H', 'H', '2', 'H', 'H', 'H']
        self.assertEqual(expected, token_space)  # expected, actual

        # Test the board spaces and home/ready-to-go yards
        board_dictionary = game.get_entire_board_dictionary()
        expected = {1: 'pC',
                    'Home Yard':
                        {'A': ['P', 'Q'],
                         'B': ['P', 'Q'],
                         'C': ['', 'Q'],
                         'D': ['P', 'Q']},
                    'Ready to Go Yard':
                        {'A': ['', ''],
                         'B': ['', ''],
                         'C': ['', ''],
                         'D': ['', '']}}
        self.assertEqual(expected, board_dictionary)  # expected, actual

    def test_player_c_token_p_goes_to_board_space_C2(self):
        # Test the function returns correct list of all the tokens
        players = ['A', 'B', 'C', 'D']
        turns = [('C', 6), ('C', 5), ('C', 5), ('C', 5), ('C', 5), ('C', 5), ('C', 5),
                 ('C', 5), ('C', 5), ('C', 5), ('C', 5), ('C', 1)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        expected = ['H', 'H', 'H', 'H', 'C1', 'H', 'H', 'H']
        self.assertEqual(expected, token_space)  # expected, actual

        # Test the board spaces and home/ready-to-go yards
        board_dictionary = game.get_entire_board_dictionary()
        expected = {58: [[0, 'pC']],
                    'Home Yard':
                        {'A': ['P', 'Q'],
                         'B': ['P', 'Q'],
                         'C': ['', 'Q'],
                         'D': ['P', 'Q']},
                    'Ready to Go Yard':
                        {'A': ['', ''],
                         'B': ['', ''],
                         'C': ['', ''],
                         'D': ['', '']}}
        self.assertEqual(expected, board_dictionary)  # expected, actual

    def test_player_d_token_p_goes_to_board_space_47(self):
        # Test the function returns correct list of all the tokens
        players = ['A', 'B', 'C', 'D']
        turns = [('D', 6), ('D', 5)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        expected = ['H', 'H', 'H', 'H', 'H', 'H', '47', 'H']
        self.assertEqual(expected, token_space)  # expected, actual

        # Test the board spaces and home/ready-to-go yards
        board_dictionary = game.get_entire_board_dictionary()
        expected = {46: 'pD',
                    'Home Yard':
                        {'A': ['P', 'Q'],
                         'B': ['P', 'Q'],
                         'C': ['P', 'Q'],
                         'D': ['', 'Q']},
                    'Ready to Go Yard':
                        {'A': ['', ''],
                         'B': ['', ''],
                         'C': ['', ''],
                         'D': ['', '']}}
        self.assertEqual(expected, board_dictionary)  # expected, actual

    def test_player_d_token_p_goes_to_board_space_52_not_into_others_home_rows(self):
        # Test the function returns correct list of all the tokens
        players = ['A', 'B', 'C', 'D']
        turns = [('D', 6), ('D', 5), ('D', 5)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        expected = ['H', 'H', 'H', 'H', 'H', 'H', '52', 'H']
        self.assertEqual(expected, token_space)  # expected, actual

        # Test the board spaces and home/ready-to-go yards
        board_dictionary = game.get_entire_board_dictionary()
        expected = {51: 'pD',
                    'Home Yard':
                        {'A': ['P', 'Q'],
                         'B': ['P', 'Q'],
                         'C': ['P', 'Q'],
                         'D': ['', 'Q']},
                    'Ready to Go Yard':
                        {'A': ['', ''],
                         'B': ['', ''],
                         'C': ['', ''],
                         'D': ['', '']}}
        self.assertEqual(expected, board_dictionary)  # expected, actual

    def test_player_d_token_p_goes_to_board_space_1(self):
        # Test the function returns correct list of all the tokens
        players = ['A', 'B', 'C', 'D']
        turns = [('D', 6), ('D', 5), ('D', 5), ('D', 5)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        expected = ['H', 'H', 'H', 'H', 'H', 'H', '1', 'H']
        self.assertEqual(expected, token_space)  # expected, actual

        # Test the board spaces and home/ready-to-go yards
        board_dictionary = game.get_entire_board_dictionary()
        expected = {0: 'pD',
                    'Home Yard':
                        {'A': ['P', 'Q'],
                         'B': ['P', 'Q'],
                         'C': ['P', 'Q'],
                         'D': ['', 'Q']},
                    'Ready to Go Yard':
                        {'A': ['', ''],
                         'B': ['', ''],
                         'C': ['', ''],
                         'D': ['', '']}}
        self.assertEqual(expected, board_dictionary)  # expected, actual

    def test_player_d_token_p_goes_to_board_space_1(self):
        # Test the function returns correct list of all the tokens
        players = ['A', 'B', 'C', 'D']
        turns = [('D', 6), ('D', 5), ('D', 5), ('D', 5)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        expected = ['H', 'H', 'H', 'H', 'H', 'H', '1', 'H']
        self.assertEqual(expected, token_space)  # expected, actual

        # Test the board spaces and home/ready-to-go yards
        board_dictionary = game.get_entire_board_dictionary()
        expected = {0: 'pD',
                    'Home Yard':
                        {'A': ['P', 'Q'],
                         'B': ['P', 'Q'],
                         'C': ['P', 'Q'],
                         'D': ['', 'Q']},
                    'Ready to Go Yard':
                        {'A': ['', ''],
                         'B': ['', ''],
                         'C': ['', ''],
                         'D': ['', '']}}
        self.assertEqual(expected, board_dictionary)  # expected, actual

    def test_moving_player_D_token_p_to_end_space(self):
        # Test the function returns correct list of all the tokens
        players = ['A', 'B', 'C', 'D']
        turns = [('D', 6), ('D', 5), ('D', 5), ('D', 5), ('D', 5), ('D', 5), ('D', 5),
                 ('D', 5), ('D', 5), ('D', 5), ('D', 5), ('D', 5), ('D', 1), ('D', 1)]  # end space here

        game = LudoGame()
        token_space = game.play_game(players, turns)
        expected = ['H', 'H', 'H', 'H', 'H', 'H', 'E', 'H']
        self.assertEqual(expected, token_space)  # expected, actual

        # Test the board spaces and home/ready-to-go yards
        board_dictionary = game.get_entire_board_dictionary()
        expected = {59: [[6, 'pD']],
                    'Home Yard':
                        {'A': ['P', 'Q'],
                         'B': ['P', 'Q'],
                         'C': ['P', 'Q'],
                         'D': ['', 'Q']},
                    'Ready to Go Yard':
                        {'A': ['', ''],
                         'B': ['', ''],
                         'C': ['', ''],
                         'D': ['', '']}}
        self.assertEqual(expected, board_dictionary)  # expected, actual

    def test_moving_player_C_token_p_to_end_space(self):
        # Test the function returns correct list of all the tokens
        players = ['A', 'B', 'C', 'D']
        turns = [('C', 6), ('C', 5), ('C', 5), ('C', 5), ('C', 5), ('C', 5), ('C', 5),
                 ('C', 5), ('C', 5), ('C', 5), ('C', 5), ('C', 5), ('C', 1), ('C', 1)]  # enC space here

        game = LudoGame()
        token_space = game.play_game(players, turns)
        expected = ['H', 'H', 'H', 'H', 'E', 'H', 'H', 'H']
        self.assertEqual(expected, token_space)  # expected, actual

        # Test the board spaces and home/ready-to-go yards
        board_dictionary = game.get_entire_board_dictionary()
        expected = {58: [[6, 'pC']],
                    'Home Yard':
                        {'A': ['P', 'Q'],
                         'B': ['P', 'Q'],
                         'C': ['', 'Q'],
                         'D': ['P', 'Q']},
                    'Ready to Go Yard':
                        {'A': ['', ''],
                         'B': ['', ''],
                         'C': ['', ''],
                         'D': ['', '']}}
        self.assertEqual(expected, board_dictionary)  # expected, actual

    def test_moving_player_D_token_p_to_end_space_and_backtracking_back_1(self):
        # Test the function returns correct list of all the tokens
        players = ['A', 'B', 'C', 'D']
        turns = [('D', 6), ('D', 5), ('D', 5), ('D', 5), ('D', 5), ('D', 5), ('D', 5),
                 ('D', 5), ('D', 5), ('D', 5), ('D', 5), ('D', 5), ('D', 1), ('D', 2)]  # end space here

        game = LudoGame()
        token_space = game.play_game(players, turns)
        expected = ['H', 'H', 'H', 'H', 'H', 'H', 'D6', 'H']
        self.assertEqual(expected, token_space)  # expected, actual

        # Test the board spaces and home/ready-to-go yards
        board_dictionary = game.get_entire_board_dictionary()
        expected = {59: [[6, 'pD']],
                    'Home Yard':
                        {'A': ['P', 'Q'],
                         'B': ['P', 'Q'],
                         'C': ['P', 'Q'],
                         'D': ['', 'Q']},
                    'Ready to Go Yard':
                        {'A': ['', ''],
                         'B': ['', ''],
                         'C': ['', ''],
                         'D': ['', '']}}
        self.assertEqual(expected, board_dictionary)  # expected, actual

    """
    Received this test from professor Zhang on request via Teams.
    """
    def test_we_can_create_players_list_and_each_players_attributes_are_initilized_correctly(self):
        game = LudoGame()
        players = ['A', 'B']
        turns = []
        current_tokens_space = game.play_game(players, turns)
        self.assertAlmostEqual(current_tokens_space, ['H', 'H', 'H', 'H'],
                               msg=f'\nExpected value for current_tokens_space: [\'H\', \'H\', \'H\', \'H\'] \nValue from your code: {current_tokens_space}')
        player_A = game.get_player_by_position('A')
        finished = player_A.get_completed()
        self.assertAlmostEqual(finished, False, msg=f'\nExpected value: False \nValue from your code: {finished}')
        player_B = game.get_player_by_position('B')
        steps = player_B.get_token_p_step_count()
        self.assertAlmostEqual(steps, -1, msg=f'\nExpected value: -1 \nValue from your code: {steps}')
        steps = player_A.get_token_q_step_count()
        self.assertAlmostEqual(steps, -1, msg=f'\nExpected value: -1 \nValue from your code: {steps}')




"""Statement so that file only runs main if ran as a script, not when imported."""
if __name__ == '__main__':
    unittest.main()
