Human vs. AI Tic-Tac-Toe Terminal application

Uses the minimax algorithm to play a perfect game of tic-tac-toe. Since the search space of Tic-Tac-Toe is small enough to calculate relatively quickly, the computer can always play a perfect game of Tic-Tac-Toe, resulting in an unbeatable AI.
The minimax algorithm generates a tree of children states for a given game state down to terminal nodes, and returns a win/loss score. The maximum score out of the set of children nodes is chosen during AI turns, and vice versa. It then follows the path that returns the highest score/greatest number of wins. The utility function I used for tic-tac-toe simply returns a 1 if
the computer wins, -1 if the human wins, and 0 for a draw. 

Instructions to run:

python3 tictactoe.py
