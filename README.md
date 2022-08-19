# Python-Ludo-Game



-CS 162 Portfolio Project.  Allowed to be posted to a public GitHub repo per Syllabus.  This is an implementation of the game [Ludo](https://en.wikipedia.org/wiki/Ludo_(board_game)) in Python, using object-oriented programming concepts taught in the course.  

-It is very similar to the game Sorry!, and involves 4 players rolling dice to move tokens around a game board, attempting to reach the end space.  It contains two classes with various functions, unit testing, and a main function that can be called with an array of players and array of tuples containg the game moves (player/roll).


<h2>Game Description</h2>

<img src="https://user-images.githubusercontent.com/91037796/185715851-58d242f7-cfdc-43c7-8666-0cca9bd03db2.png" width=60% height=60%>



<h2>Printing Game Board Function</h2>

<img src="https://user-images.githubusercontent.com/91037796/185717022-680e6f80-d709-4539-8a90-51389414bc48.png" width=60% height=60%>




<h2>Test Cases</h2>

-Added 54 test cases to this project, 9 provided by the instructors.  

-Tested board position in the board game array, and token steps, boad space variables in the player object data members.

-Test cases were essential in this project to ensure that complex game rules functioned correctly, and that each new feature added did not break previous functions.  For example, this was helpful in adding token backtracking in the home spaces, deciding whether to kick an opponent's token, and token priorty rules in the game.


<br>
<img src="https://user-images.githubusercontent.com/91037796/185717670-5a8aee14-b0fe-4d06-9657-a6d5f88607fc.png" width=90% height=90%>



-For example, here is a test case which check that


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


