import numpy as np # for easy play with arrays
import pygame 
import sys
import math
# import pygame.freetype
import pygame.font # for font object and rendering data on screen

# Specifying colors via rgb
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

# Default row and column numbers of the game
ROW_COUNT = 6
COLUMN_COUNT = 7

# Function to create the board
def create_board():
	board = np.zeros((ROW_COUNT,COLUMN_COUNT))
	return board

# Function to drop pieces in the place
def drop_piece(board, row, col, piece):
	board[row][col] = piece

# Function to check if the position is valid or not
def is_valid_location(board, col):
	return board[ROW_COUNT-1][col] == 0

# Function to get the empty of row of specified column
def get_next_open_row(board, col):
	for r in range(ROW_COUNT):
		if board[r][col] == 0:
			return r
# Function to print the board on console
def print_board(board):
	print(np.flip(board, 0))

# Function to check if the winning move has been played
def winning_move(board, piece):
	# Check horizontal locations for win
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT):
			if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
				return True

	# Check vertical locations for win
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT-3):
			if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
				return True

	# Check positively sloped diaganols
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT-3):
			if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
				return True

	# Check negatively sloped diaganols
	for c in range(COLUMN_COUNT-3):
		for r in range(3, ROW_COUNT):
			if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
				return urn i
# Function to draw board via pygame
def draw_board(board):
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):
			pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
			pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
	
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):		
			if board[r][c] == 1:
				pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
			elif board[r][c] == 2: 
				pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
	pygame.display.update()

board = create_board() # Create board 
print_board(board) # Print the board
game_over = False
turn = 0 # to decide whose turn is it

pygame.init() # initiate pygame

SQUARESIZE = 100 

width = COLUMN_COUNT * SQUARESIZE # width of game window
height = (ROW_COUNT+1) * SQUARESIZE # height of game window

size = (width, height) # size of game window

RADIUS = int(SQUARESIZE/2 - 5) # radius of circle

screen = pygame.display.set_mode(size) # setting screen for game
draw_board(board) # drawing the board using pygame
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 75) # create a font object

while not game_over: # Main game loop

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEMOTION:
			pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
			posx = event.pos[0]
			if turn == 0:
				pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
			else: 
				pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
		pygame.display.update()

		if event.type == pygame.MOUSEBUTTONDOWN:
			pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
			#print(event.pos)
			# Ask for Player 1 Input
			if turn == 0:
				posx = event.pos[0]
				col = int(math.floor(posx/SQUARESIZE))

				if is_valid_location(board, col):
					row = get_next_open_row(board, col)
					drop_piece(board, row, col, 1)

					if winning_move(board, 1):
						label = myfont.render("Player 1 wins!!", 1, RED)
						screen.blit(label, (40,10))
						game_over = True


			# # Ask for Player 2 Input
			else:				
				posx = event.pos[0]
				col = int(math.floor(posx/SQUARESIZE))

				if is_valid_location(board, col):
					row = get_next_open_row(board, col)
					drop_piece(board, row, col, 2)

					if winning_move(board, 2):
						label = myfont.render("Player 2 wins!!", 1, YELLOW)
						screen.blit(label, (40,10))
						game_over = True

			print_board(board) # print board in shell
			draw_board(board) # draw board in game window

			turn += 1 # to change the turns
			turn = turn % 2

			if game_over:
				pygame.time.wait(3000)
