import numpy

def create_board():
    board = numpy.zeros((6,7))
    return board

board = create_board()
game_over = False
turn = 0

while not game_over:
    #Ask for Player 1 Input
    if turn == 0:
        selection = input("Player 1 - Make your selection (0-6): ")

        print(selection)
        print(type(selection))
        
    #Ask for Player 2 Input

