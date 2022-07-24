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
        expected = {56: [4, 'pA'],
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
        expected = {56: [5, 'pA'],
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

    def test_player_A_moves_token_p_between_home_rows_to_end_row(self):
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
        expected = {56: [6, 'pA'],
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
        expected = {56: [6, 'pA'],
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
        expected = {56: [6, 'pA'],
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
        expected = {56: [6, 'pAqA'],
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
        expected = {56: [6, 'pAqA'],
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
        expected = {56: [6, 'pAqA'],
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
        turns = [('A', 6), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5),
                 ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 1), ('A', 1),  # end space here
                 ('A', 6), ('A', 6), ('A', 6), ('A', 6), ('A', 6), ('A', 6), ('A', 6),  # these lines moves token q
                 ('A', 6), ('A', 6), ('A', 6), ('A', 3), ('B', 6), ('B', 6), ('B', 6)]  # move Bs to ready, one on board
        game = LudoGame()
        token_space = game.play_game(players, turns)

        expected = ['E', 'E', 'H', 'R', 'H', 'H', 'H', 'H']
        self.assertEqual(expected, token_space)  # expected, actual

        # Test the board spaces and home/ready-to-go yards
        board_dictionary = game.get_entire_board_dictionary()
        expected = {56: [6, 'pAqA'],
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
        expected = {56: [6, 'pAqA'],
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
        expected = {56: [6, 'pAqA'],
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

    def test_game_returns_string_matching_the_readme_project_sample_output(self):
        # Test the function returns correct list of all the tokens
        players = ['A', 'B']
        turns = [('A', 6), ('A', 4), ('A', 5), ('A', 4), ('B', 6), ('B', 4), ('B', 1), ('B', 2), ('A', 6), ('A', 4),
                 ('A', 6), ('A', 3), ('A', 5), ('A', 1), ('A', 5), ('A', 4)]
        game = LudoGame()
        token_space = game.play_game(players, turns)
        expected = ['28', '28', '21', 'H']
        self.assertEqual(expected, token_space)  # expected, actual

        # Test the board spaces and home/ready-to-go yards
        board_dictionary = game.get_entire_board_dictionary()
        expected = {56: [6, 'pAqA'],
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
        expected = {56: [5, 'pA'],
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

    def test_player_b_token_p_goes_past_board_space_56_as_end_space_is_8_to_board_space_3(self):
        # Test the function returns correct list of all the tokens
        players = ['A', 'B', 'C', 'D']
        turns = [('B', 6), ('B', 5), ('B', 5), ('B', 5), ('B', 5), ('B', 5), ('B', 5),
                 ('B', 5), ('B', 5), ('B', 5)]  
        game = LudoGame()
        token_space = game.play_game(players, turns)
        expected = ['H', 'H', '45', 'H', 'H', 'H', 'H', 'H']
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
        expected = ['H', 'H', '50', 'H', 'H', 'H', 'H', 'H']
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
        expected = {57: [1, 'pB'],
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
        expected = {57: [2, 'pB'],
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
        expected = {57: [6, 'pB'],
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
        expected = {57: [6, 'pB'],
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


"""Statement so that file only runs main if ran as a script, not when imported."""
if __name__ == '__main__':
    unittest.main()
