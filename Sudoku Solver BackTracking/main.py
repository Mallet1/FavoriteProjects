import ctypes, pygame, time, sys
from Maker import Maker

user32 = ctypes.windll.user32
screensize = (user32.GetSystemMetrics(1) - 80, user32.GetSystemMetrics(1) - 80)  # get screensize
WIDTH, HEIGHT = screensize
pygame.init()

screen = pygame.display.set_mode(screensize)
pygame.display.set_caption('Sudoku Solver')
clock = pygame.time.Clock()


board = Maker.create_board()

# print('board = [', end='')
# for row in board:
#     print(f'{row},')
# print(']')
# sys.exit()

# board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
# [5, 2, 0, 0, 0, 0, 0, 0, 0],
# [0, 8, 7, 0, 0, 0, 0, 3, 1],
# [0, 0, 3, 0, 1, 0, 0, 8, 0],
# [9, 0, 0, 8, 6, 3, 0, 0, 5],
# [0, 5, 0, 0, 9, 0, 6, 0, 0],
# [1, 3, 0, 0, 0, 0, 2, 5, 0],
# [0, 0, 0, 0, 0, 0, 0, 7, 4],
# [0, 0, 5, 2, 0, 6, 3, 0, 0]]

# board = [[9, 7, 0, 4, 6, 8, 0, 0, 0],
#          [0, 5, 0, 7, 3, 0, 0, 0, 8],
#          [8, 3, 0, 0, 5, 2, 0, 0, 0],
#          [1, 0, 0, 0, 0, 5, 0, 7, 0],
#          [0, 8, 0, 2, 1, 9, 0, 0, 0],
#          [0, 6, 2, 8, 0, 3, 0, 1, 9],
#          [0, 0, 7, 5, 9, 0, 2, 0, 6],
#          [0, 2, 9, 0, 8, 0, 0, 5, 0],
#          [5, 4, 0, 0, 2, 0, 1, 0, 0]]

# board = [[0, 0, 4, 0, 0, 8, 0, 6, 9],
#          [0, 9, 0, 0, 0, 0, 0, 4, 0],
#          [6, 0, 0, 0, 9, 1, 0, 0, 0],
#          [9, 0, 0, 0, 4, 0, 0, 0, 5],
#          [0, 5, 3, 0, 6, 0, 0, 9, 0],
#          [2, 0, 0, 0, 7, 0, 4, 0, 8],
#          [0, 0, 0, 6, 8, 0, 0, 0, 2],
#          [0, 6, 0, 0, 0, 0, 0, 5, 0],
#          [5, 3, 0, 2, 0, 0, 9, 0, 0]]

new_rects = []
board_rects = [[i for i in range(1, 10)] for i in range(1, 10)]

offset = HEIGHT / 11
for i in range(len(board_rects)):
    for k in range(len(board_rects[0])):
        board_rects[i][k] = pygame.Rect(offset * k + offset, offset * i + offset, offset, offset)

font = pygame.font.Font('freesansbold.ttf', 64)

# speed
VISUALIZE = pygame.USEREVENT
pygame.time.set_timer(VISUALIZE, 50)

start = 0


def display_board(board):
    offset = HEIGHT / 11

    for i in range(1, 11):  # vertical rects
        if (i - 1) % 3 == 0:
            pygame.draw.rect(screen, 'BLACK', pygame.Rect(offset * i, 0 + offset, 4, HEIGHT - offset * 2 + 4))
        else:
            pygame.draw.rect(screen, 'BLACK', pygame.Rect(offset * i, 0 + offset, 1, HEIGHT - offset * 2 + 4))

    for i in range(1, 11):  # horizontal rects
        if (i - 1) % 3 == 0:
            pygame.draw.rect(screen, 'BLACK', pygame.Rect(0 + offset, offset * i, WIDTH - offset * 2, 4))
        else:
            pygame.draw.rect(screen, 'BLACK', pygame.Rect(0 + offset, offset * i, WIDTH - offset * 2, 1))

    offset = HEIGHT / 9

    for i in range(len(board)):
        for k in range(len(board[0])):
            if board[i][k] != 0:
                num_text = font.render(str(board[i][k]), True, (0, 0, 0))
                screen.blit(num_text, (HEIGHT / 11 * k + offset + 7, WIDTH / 11 * i + offset - 5))


def checkGrid(grid):
  for row in range(0,9):
      for col in range(0,9):
        if grid[row][col]==0:
          return False

  #We have a complete grid!
  return True


def solveGrid(grid):
  for i in range(0,81):
    row=i//9
    col=i%9
    if grid[row][col]==0:
      for value in range (1,10):
        if not(value in grid[row]):
          if not value in (grid[0][col],grid[1][col],grid[2][col],grid[3][col],grid[4][col],grid[5][col],grid[6][col],grid[7][col],grid[8][col]):
            square=[]
            if row<3:
              if col<3:
                square=[grid[i][0:3] for i in range(0,3)]
              elif col<6:
                square=[grid[i][3:6] for i in range(0,3)]
              else:
                square=[grid[i][6:9] for i in range(0,3)]
            elif row<6:
              if col<3:
                square=[grid[i][0:3] for i in range(3,6)]
              elif col<6:
                square=[grid[i][3:6] for i in range(3,6)]
              else:
                square=[grid[i][6:9] for i in range(3,6)]
            else:
              if col<3:
                square=[grid[i][0:3] for i in range(6,9)]
              elif col<6:
                square=[grid[i][3:6] for i in range(6,9)]
              else:
                square=[grid[i][6:9] for i in range(6,9)]
            if not value in (square[0] + square[1] + square[2]):
              grid[row][col]=value
              new_rects.append(board_rects[row][col])
              if checkGrid(grid):
                print("Grid Complete and Checked")
                return True
              else:
                if solveGrid(grid):
                  return True
      break
  print("Backtrack")
  grid[row][col]=0


def highlight_rect(rect, fill):
    s = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)  # per-pixel alpha
    s.fill(fill)  # notice the alpha value in the color
    screen.blit(s, (rect.x, rect.y))


running = True
while running:

    screen.fill((255, 255, 255))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                solveGrid(board)

    for rect in new_rects:
        highlight_rect(rect, '#C7FFC4')

    display_board(board)

    clock.tick(144)
    pygame.display.update()
