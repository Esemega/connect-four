import numpy

NUMBER_OF_ROWS = 6
NUMBER_OF_COLLUMNS = 7
PLAYER_1_PIECE = 1
PLAYER_2_PIECE = 2

def create_board():
    board = numpy.zeros((NUMBER_OF_ROWS,NUMBER_OF_COLLUMNS))
    return board

def drop_piece(board, row, collumn, piece):
    board[row][collumn] = piece

def is_valid_location(board, collumn):
    return board[len(board) - 1][collumn] == 0

def get_next_open_row(board, collumn):
    for row in range(NUMBER_OF_ROWS):
        if board[row][collumn] == 0:
            return row

def print_board(board):
    print(numpy.flip(board, 0))

def winning_move(board, piece):
    #Check horizontal locations for win
    for col in range(NUMBER_OF_COLLUMNS - 3):
        for row in range(NUMBER_OF_ROWS):
            if board[row][col] == piece and board[row][col+1] == piece and board[row][col+2] == piece and board[row][col+3] == piece:
                return True

    #Check vertical locations for win
    for col in range(NUMBER_OF_COLLUMNS):
        for row in range(NUMBER_OF_ROWS - 3):
            if board[row][col] == piece and board[row+1][col] == piece and board[row+2][col] == piece and board[row+3][col] == piece:
                return True
    #Check positive sloped locations for win
    for col in range(NUMBER_OF_COLLUMNS - 3):
        for row in range(NUMBER_OF_ROWS - 3):
            if board[row][col] == piece and board[row+1][col+1] == piece and board[row+2][col+2] == piece and board[row+3][col+3] == piece:
                return True
    #Check negative sloped locations for win
    for col in range(NUMBER_OF_COLLUMNS - 3):
        for row in range(3, NUMBER_OF_ROWS):
            if board[row][col] == piece and board[row-1][col+1] == piece and board[row-2][col+2] == piece and board[row-3][col+3] == piece:
                return True

board = create_board()
print_board(board)
game_over = False
turn = 0

while not game_over:
    #Ask for Player 1 Input
    if turn == 0:
        selected_collumn = int(input("Player 1 - Make your selection (0-6): "))

        if is_valid_location(board, selected_collumn):
            row = get_next_open_row(board, selected_collumn)
            drop_piece(board, row, selected_collumn, PLAYER_1_PIECE)
        
            if winning_move(board, PLAYER_1_PIECE):
                print("PLAYER 1 WINS!!!! Congrats!!!!")
                game_over = True
        
    #Ask for Player 2 Input
    else:
        selected_collumn = int(input("Player 2 - Make your selection (0-6): "))

        if is_valid_location(board, selected_collumn):
            row = get_next_open_row(board, selected_collumn)
            drop_piece(board, row, selected_collumn, PLAYER_2_PIECE)

            if winning_move(board, PLAYER_2_PIECE):
                print("PLAYER 2 WINS!!!! Congrats!!!!")
                game_over = True
    
    print_board(board)

    turn += 1
    turn = turn % 2

