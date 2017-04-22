"""
Tic-tac game where the goal is to become the first person with 3 in a row.

Learning variables, automatic filling lists and other minor stuff.

The logic behind this is having player_x and player_y as its own variable. A board going from 1 to 9.
3 in each rows for 3 rows. The stats are logged in a dictionary and checked if either x or y owns all the
spots in one of the winning rows list.
"""

# TODO Building the CLI UI.
# TODO Get the game working playing vs myself :<
# TODO Build winning_rows with a function.
# TODO A simple completely random bot.

# Debug board.
debug_board = {1: 'y', 2: 'y', 3: 'y', 4: 'x', 5: 'x', 6: 'y', 7: 'x', 8: 'x', 9: ''}

# Game variables.
player_x = "x"
player_y = "y"
gaming_board = {}
winning_rows = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (3, 6, 9), (1, 5, 9), (3, 5, 7)]

# Building the board. Simple dictionary building.
for number in range(1, 10):
    gaming_board[number] = ""

if debug_board.values() == "y" in debug_board.keys(winning_rows):
    print("WIN")
else:
    print("LOSE")

print(winning_rows)
