# This program lets two players play tic-tac-toe against each other using basic keyboard inputs.



# importing the relevant packages
import random

# defining the relevant functions
def print_grid(def_positions):
       '''
       This function prints out the playing board at each step of the game.
       :param def_positions: dictionary that specifies the entries for all nine positions on the board
       :return: displays the full grid of the board with the positions numbered or already filled in with X and O
       '''
       default_grid = f'\n {def_positions["1"]} | {def_positions["2"]} | {def_positions["3"]} ' \
              '\n----------------' \
              f'\n {def_positions["4"]} | {def_positions["5"]} | {def_positions["6"]} ' \
              '\n----------------' \
              f'\n {def_positions["7"]} | {def_positions["8"]} | {def_positions["9"]} ' \
              f'\n'
       print(default_grid)

# I could also define a marker and check if these positions are equal to this marker
def someoneWon(pos):
       '''
       :param pos: dictionary of the positions on the board
       :return: returns a boolean that states whether the conditions for winning have been met
       '''
       return pos["1"] == pos["2"] == pos["3"] or \
              pos["4"] == pos["5"] == pos["6"] or \
              pos["7"] == pos["8"] == pos["9"] or \
              pos["1"] == pos["4"] == pos["7"] or \
              pos["2"] == pos["5"] == pos["8"] or \
              pos["3"] == pos["6"] == pos["9"] or \
              pos["1"] == pos["5"] == pos["9"] or \
              pos["3"] == pos["5"] == pos["7"]

def firstMove():
       '''
       This function determines who begins the round and plays as X.
       :return: boolean that states whether player 1 or 2 will start.
       '''
       print("The flip of a coin now determines who will start.")
       if random.randint(0,1) == 0:
              players = {'o': 'Player 2', 'x': 'Player 1'}
              return print("Player 1 will start the game.\n")
       else:
              players = {'o': 'Player 1', 'x': 'Player 2'}
              return print("Player 2 will start the game.\n")


# 2. whether to be X or O
# charChoice = input("Player 1, choose your character! (X or O)")
# while charChoice not in ['x','X','o','O']:
#        print('You did not specify a valid character.')
#        charChoice = input("Player 1, choose your character! (X or O)")
#
# while charChoice in ['x','X','o','O']:
#        if charChoice == 'X' or charChoice == 'x':
#               players = {'x':'Player 1','o':'Player 2'}
#               print('Player 1 chose to be X and therefore starts the round.')
#               break
#        elif charChoice == 'O' or charChoice == 'o':
#               players = {'o':'Player 1','x':'Player 2'}
#               print('Player 1 chose to be O. Player 2 starts the round.')
#               break



# missing: not be able to overwrite moves

def placingMove(currentPlayer, pos):
       '''
       This function is needed to place each move that is put in by the players.
       :param currentPlayer: this is the string 'x' or 'o', depending on which player is currently moving
       :param pos: dictionary of all the nine positions on the board
       :return: returns a key value pair of the next move the player is going to make
       '''
       nextMove = input(f'{players[currentPlayer]}, make your move. (1-9)')
       while int(nextMove) not in list(range(1, 10)):
              nextMove = input("Your input was not a number between 1 and 9. Please input a valid number.")
              return {str(nextMove): currentPlayer.upper()}
       else:
              storeMoves.append(int(nextMove))
              return {str(nextMove): currentPlayer.upper()}

def replay():
       '''
       This function gives the option to replay the game after it ended.
       :return: boolean which states whether the players want to play again.
       '''
       replayChoice = input("Would you like to play again? [y/n]")
       return replayChoice in ["yes","y","Yes","Y"]

while True:
       print("Welcome to Tic-Tac-Toe!\n")
       firstMove()

       # 3. where to put X or O
       print("In the following grid, you will place your characters in turn. The numbers indicate the available positions you can pick.")
       gridNumbers = f'\n 1 | 2 | 3 ' \
                     '\n-------------' \
                     f'\n 4 | 5 | 6 ' \
                     '\n-------------' \
                     f'\n 7 | 8 | 9 ' \
                     '\n'
       print(gridNumbers)
       positions = {'1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}

       storeMoves = []
       i=0
       class ending(Exception): pass
       class tie(Exception): pass
              while i<9 and someoneWon(positions) == False:
                     try:
                            for player in ["x","o"]:
                                   positions.update(placingMove(player,positions))
                                   print_grid(positions)
                                   i += 1
                                   if someoneWon(positions) == True:
                                       raise ending
                                   elif i==9:
                                          raise tie

                     except ending:
                            print(f'{players[player]} has won the round!')
                     except tie:
                            print("The game ends in a tie.")
              if not replay():
                      break