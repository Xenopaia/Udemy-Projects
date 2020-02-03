# importing the relevant packages
from tkinter import *

# creating the empty template for the tic tac toe grid
positions = {'pos1':' ', 'pos2':' ', 'pos3':' ', 'pos4':' ', 'pos5':' ', 'pos6':' ', 'pos7':' ', 'pos8':' ', 'pos9':' '}

grid = f'\n {positions["pos1"]} | {positions["pos2"]} | {positions["pos3"]} ' \
       '\n----------------' \
       f'\n {positions["pos4"]} | {positions["pos5"]} | {positions["pos6"]} ' \
       '\n----------------' \
       f'\n {positions["pos7"]} | {positions["pos8"]} | {positions["pos9"]} '

#testing it out
print(grid)


# creating input fields to input
# 1. who goes first

# 2. whether to be X or O


charChoice = input("Player 1, choose your character! (X or O)")
while charChoice not in ['x','X','o','O']:
       print('You did not specify a valid character.')
       charChoice = input("Player 1, choose your character! (X or O)")

while charChoice in ['x','X','o','O']:
       if charChoice == 'X' or charChoice == 'x':
              players = {'x':'Player 1','o':'Player 2'}
              print('Player 1 chose to be X and therefore starts the round.')
              break
       elif charChoice == 'O' or charChoice == 'o':
              players = {'o':'Player 1','x':'Player 2'}
              print('Player 1 chose to be O. Player 2 starts the round.')
              break

# 3. where to put X or O
print(f'{players["x"]}, make your move. (1-9)')
