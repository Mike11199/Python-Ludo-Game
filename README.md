# Python-Ludo-Game



-CS 162 Portfolio Project.  Allowed to be posted to a public GitHub repo per the Syllabus.  This is an implementation of the game [Ludo](https://en.wikipedia.org/wiki/Ludo_(board_game)) in Python, using object-oriented programming concepts taught in the course.  

-It is very similar to the game Sorry! and involves 4 players rolling dice to move tokens around a game board, attempting to reach the end space.  It contains two classes with various functions, unit testing, and a main function that can be called with an array of players and array of tuples containg the game moves (player/roll).

<br>
<h2>Game Description</h2>

<img src="https://user-images.githubusercontent.com/91037796/185715851-58d242f7-cfdc-43c7-8666-0cca9bd03db2.png" width=60% height=60%>


<br>
<h2>Printing Game Board Function</h2>

<img src="https://user-images.githubusercontent.com/91037796/185717022-680e6f80-d709-4539-8a90-51389414bc48.png" width=60% height=60%>



<br>
<h2>Test Cases</h2>

-Added 54 test cases to this project, 9 provided by the instructors.  

-Tested board position in the board game array, and token steps, boad space variables in the player object data members.

-Test cases were essential in this project to ensure that complex game rules functioned correctly, and that each new feature added did not break previous functions.  For example, this was helpful in adding token backtracking in the home spaces, deciding whether to kick an opponent's token, and token priorty rules in the game.


<br>
<img src="https://user-images.githubusercontent.com/91037796/185717670-5a8aee14-b0fe-4d06-9657-a6d5f88607fc.png" width=90% height=90%>



-For example, here is a test case which checks that checks that the play_game function returns the correct string, indicating the positions of all tokens in the game, in the order of Players A, B, C, and D, from token P to token Q.  In this series of moves, one of Player A's tokens should have kicked Player B's token back to the home yard spaces.  This also tests that Player A's tokens were stacked (both landing on the same space, and can move together).  

-A function is used to return all non-empty spaces of the board as a dictionary, which is used by the test case to also test that the board array was updated correctly (old position cleared by a move, new position filled).  This array was not required by the project, but was added in case a GUI was ever added for the game.


```python
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

```


<br>
<h2>Class and Function Structure</h2>

```python
 class LudoGame:
 
    
    def __init__(self):
      
    def sort_turns(self, turns_list):
      
    def play_game(self, players_list, turns_list):
      
    def current_spaces_of_all_tokens(self):
    
    def update_players_actual_token_spaces_board_positions_not_steps(self):
     
    def choose_token_algorithm(self, player, current_roll, p_steps, q_steps):
   
    def move_token(self, player_obj, token_name, board_steps):
        

    def move_to_home_rows(self, p_char, player_obj, token_name, home_row_spaces, future_board_pos_space, token_string,
                          step_count, board_steps, backtracking):
       
    def set_board_pos_space(self, token, board_pos, board_pos2=None, clear=None):
     
    def get_board_position_space(self, board_pos):
     
    def get_entire_board(self):
       
    def get_entire_board_dictionary(self):
        
    def create_player_list(self, players_list):
     
    def print_game_board(self):
        
        
class Player:
   

    def __init__(self, position):

    def get_position(self):                                       # e.g- "A", "B", "C", or "D"
     
    def set_token_steps(self, token, pos):
       
    def set_actual_board_spaces_for_tokens(self, token, pos):
        
    def get_actual_board_spaces_for_tokens(self, token):
      
    def set_player_status_as_completed_if_finished(self):
       
    def get_completed(self):
      
    def get_token_p_step_count(self):                            # H = -1, R = 0, s/b no more than 57
    
    def get_token_q_step_count(self):                            # H = -1, R = 0, s/b no more than 57
     
    def get_space_name(self, total_steps):
      
    def get_start_space(self):
    
    def get_end_space(self):

```
