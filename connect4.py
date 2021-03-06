import numpy
import pygame
import sys
import math

NUMBER_OF_ROWS = 6
NUMBER_OF_COLLUMNS = 7
PLAYER_1_PIECE = 1
PLAYER_2_PIECE = 2

SQUARESIZE = 75 #pixels
SQUARE_OFFSET = 1
CIRCLE_OFFSET = int(SQUARESIZE/2)

RADIUS = SQUARESIZE/2 - 3
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)

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

def draw_board(board):
    #draw the board and the free slots
    for col in range(NUMBER_OF_COLLUMNS):
        for row in range(NUMBER_OF_ROWS): 
            pygame.draw.rect(screen, BLUE, (col*SQUARESIZE, row*SQUARESIZE + SQUARE_OFFSET*SQUARESIZE, SQUARESIZE, SQUARESIZE))

            free_slot_position = (int(col*SQUARESIZE+CIRCLE_OFFSET), int(row*SQUARESIZE + SQUARE_OFFSET*SQUARESIZE + CIRCLE_OFFSET))
            pygame.draw.circle(screen, BLACK, free_slot_position, RADIUS )
    
    #draw the pieces of each player
    for col in range(NUMBER_OF_COLLUMNS):
        for row in range(NUMBER_OF_ROWS):
            pieze_position = (int(col*SQUARESIZE+CIRCLE_OFFSET), height - int(row*SQUARESIZE + CIRCLE_OFFSET))
            if board[row][col] == 1:
                pygame.draw.circle(screen, RED, pieze_position, RADIUS )
            elif board[row][col] == 2:
                pygame.draw.circle(screen, GREEN, pieze_position, RADIUS )
    pygame.display.update()



board = create_board()
print_board(board)
game_over = False
turn = 0

#init pygame
pygame.init()



width = NUMBER_OF_COLLUMNS * SQUARESIZE
height = (NUMBER_OF_ROWS + 1) * SQUARESIZE

size = (width, height)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", int(SQUARESIZE*0.8)) #font_name, pixels

while not game_over:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0,0,width,SQUARESIZE))
            posX = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen,RED,(posX,int(SQUARESIZE/2)),RADIUS)
            else:
                pygame.draw.circle(screen,GREEN,(posX,int(SQUARESIZE/2)),RADIUS)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0,0,width,SQUARESIZE))
            #GRAPHIC VERSION
            #Player 1 turn
            if turn == 0:
                posX = event.pos[0]
                selected_collumn = int(math.floor(posX/SQUARESIZE))

                if is_valid_location(board, selected_collumn):
                    row = get_next_open_row(board, selected_collumn)
                    drop_piece(board, row, selected_collumn, PLAYER_1_PIECE)
                
                    if winning_move(board, PLAYER_1_PIECE):
                        label = myfont.render("Player 1 wins!", 1, RED)
                        screen.blit(label, (5,5))
                        game_over = True
                
            #Ask for Player 2 Input
            else:
                posX = event.pos[0]
                selected_collumn = int(math.floor(posX/SQUARESIZE))

                if is_valid_location(board, selected_collumn):
                    row = get_next_open_row(board, selected_collumn)
                    drop_piece(board, row, selected_collumn, PLAYER_2_PIECE)

                    if winning_move(board, PLAYER_2_PIECE):
                        label = myfont.render("Player 2 wins!", 1, GREEN)
                        screen.blit(label, (5,5))
                        game_over = True
            
            print_board(board)
            draw_board(board)

            turn += 1
            turn = turn % 2

            if game_over:
                pygame.time.wait(3000)

            #COMAND LINE VERSION
            #Ask for Player 1 Input
            # if turn == 0:
            #     selected_collumn = int(input("Player 1 - Make your selection (0-6): "))

            #     if is_valid_location(board, selected_collumn):
            #         row = get_next_open_row(board, selected_collumn)
            #         drop_piece(board, row, selected_collumn, PLAYER_1_PIECE)
                
            #         if winning_move(board, PLAYER_1_PIECE):
            #             print("PLAYER 1 WINS!!!! Congrats!!!!")
            #             game_over = True
                
            # #Ask for Player 2 Input
            # else:
            #     selected_collumn = int(input("Player 2 - Make your selection (0-6): "))

            #     if is_valid_location(board, selected_collumn):
            #         row = get_next_open_row(board, selected_collumn)
            #         drop_piece(board, row, selected_collumn, PLAYER_2_PIECE)

            #         if winning_move(board, PLAYER_2_PIECE):
            #             print("PLAYER 2 WINS!!!! Congrats!!!!")
            #             game_over = True
            
            # print_board(board)

            # turn += 1
            # turn = turn % 2

