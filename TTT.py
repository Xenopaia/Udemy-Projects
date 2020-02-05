# This program



# importing the relevant packages
from tkinter import *

# creating the empty template for the tic tac toe grid
# to do: make a function out of this, so you don't have to print it again and again!
positions = {'1':' ', '2':' ', '3':' ', '4':' ', '5':' ', '6':' ', '7':' ', '8':' ', '9':' '}

grid = f'\n {positions["1"]} | {positions["2"]} | {positions["3"]} ' \
       '\n----------------' \
       f'\n {positions["4"]} | {positions["5"]} | {positions["6"]} ' \
       '\n----------------' \
       f'\n {positions["7"]} | {positions["8"]} | {positions["9"]} '

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
print("In the following grid, you will place your characters in turn. The numbers indicate the available positions you can pick.")
gridNumbers = f'\n 1 | 2 | 3 ' \
       '\n-------------' \
       f'\n 4 | 5 | 6 ' \
       '\n-------------' \
       f'\n 7 | 8 | 9 '
print(gridNumbers)

# being able to place a move
i=0
# missing: not be able to overwrite moves
# missing: game should end when someone has three in a row, or every field in the grid has been filled
#      or there are no winning combinations possible anymore
while i<9:
       # missing: only numbers should be put in here; try again and again until number is given
       i += 1

       # player X
       nextMove = input(f'{players["x"]}, make your move. (1-9)')
       while nextMove not in range(1,10):
              nextMove = input("Your input was not a number between 1 and 9. Please input a valid number.")
              nextMove = {str(nextMove):"X"}
       else:
              nextMove = {str(nextMove):"X"}

       # update and print out the grid
       positions.update(nextMove)
       grid = f'\n {positions["1"]} | {positions["2"]} | {positions["3"]} ' \
              '\n----------------' \
              f'\n {positions["4"]} | {positions["5"]} | {positions["6"]} ' \
              '\n----------------' \
              f'\n {positions["7"]} | {positions["8"]} | {positions["9"]} '
       print(grid)

       # player O
       nextMove = {input(str(f'{players["o"]}, make your move. (1-9)')):'O'}
       if nextMove not in range(1,10):
              nextMove = input("Your input was not a number between 1 and 9. Please input a valid number.")
              nextMove = {str(nextMove):"O"}
       else:
              nextMove = {str(nextMove):"O"}

       # update and print out the grid
       positions.update(nextMove)
       grid = f'\n {positions["1"]} | {positions["2"]} | {positions["3"]} ' \
              '\n----------------' \
              f'\n {positions["4"]} | {positions["5"]} | {positions["6"]} ' \
              '\n----------------' \
              f'\n {positions["7"]} | {positions["8"]} | {positions["9"]} '
       print(grid)


# continue until someone gets three in a row ==> while loop, breaks after condition is met