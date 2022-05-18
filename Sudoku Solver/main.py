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

# board = [[None, 7, None, None, 2, None, 9, None, None],
# [None, 4, None, 8, None, 6, None, None, None],
# [None, 1, 2, None, None, None, 3, None, None],
# [None, None, None, None, None, None, 8, 7, None],
# [None, 6, None, 9, 7, 2, None, 5, None],
# [None, 2, 5, None, None, None, None, None, None],
# [None, None, 1, None, None, None, 2, 9, None],
# [None, None, None, 5, None, 4, None, 3, None],
# [None, None, 7, None, 6, None, None, 1, None],
# ]

# board = [[9, 7, None, 4, 6, 8, None, None, None],
#          [None, 5, None, 7, 3, None, None, None, 8],
#          [8, 3, None, None, 5, 2, None, None, None],
#          [1, None, None, None, None, 5, None, 7, None],
#          [None, 8, None, 2, 1, 9, None, None, None],
#          [None, 6, 2, 8, None, 3, None, 1, 9],
#          [None, None, 7, 5, 9, None, 2, None, 6],
#          [None, 2, 9, None, 8, None, None, 5, None],
#          [5, 4, None, None, 2, None, 1, None, None]]

# board = [[None, None, 4, None, None, 8, None, 6, 9],
#          [None, 9, None, None, None, None, None, 4, None],
#          [6, None, None, None, 9, 1, None, None, None],
#          [9, None, None, None, 4, None, None, None, 5],
#          [None, 5, 3, None, 6, None, None, 9, None],
#          [2, None, None, None, 7, None, 4, None, 8],
#          [None, None, None, 6, 8, None, None, None, 2],
#          [None, 6, None, None, None, None, None, 5, None],
#          [5, 3, None, 2, None, None, 9, None, None]]

# board = [[3, None, 6, 5, None, 8, 4, None, None],
# [5, 2, None, None, None, None, None, None, None],
# [None, 8, 7, None, None, None, None, 3, 1],
# [None, None, 3, None, 1, None, None, 8, None],
# [9, None, None, 8, 6, 3, None, None, 5],
# [None, 5, None, None, 9, None, 6, None, None],
# [1, 3, None, None, None, None, 2, 5, None],
# [None, None, None, None, None, None, None, 7, 4],
# [None, None, 5, 2, None, 6, 3, None, None]]

original_board = board # to check if it has changed by the end

board_rects = [[i for i in range(1, 10)] for i in range(1, 10)]

possible_nums = {}
impossible_nums = {}
possibilities_filled = False

offset = HEIGHT / 11
for i in range(len(board_rects)):
    for k in range(len(board_rects[0])):
        board_rects[i][k] = pygame.Rect(offset * k + offset, offset * i + offset, offset, offset)

# board = [[i for i in range(1,10)]for i in range(1,10)]

font = pygame.font.Font('freesansbold.ttf', 64)

solving = False
row = 0
col = 0

# speed
VISUALIZE = pygame.USEREVENT
pygame.time.set_timer(VISUALIZE, 50)

start = 0


def display_board():
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
            if board[i][k] is not None:
                num_text = font.render(str(board[i][k]), True, (0, 0, 0))
                screen.blit(num_text, (HEIGHT / 11 * k + offset + 7, WIDTH / 11 * i + offset - 5))


def iterate(row, col):
    global possibilities_filled

    col += 1
    if row == 8 and col > 8:
        row = 0
        col = 0
        possibilities_filled = True
    if col > 8:
        col = 0
        row += 1

    return (row, col)


def is_solved():
    for row in board:
        for val in row:
            if val == None:
                return False

    return True


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
                if not solving:
                    solving = True
                else:
                    board = Maker.create_board(board)

                    for item in possible_nums.items():
                        print(item)

                    possible_nums = {}
                    impossible_nums = {}
                    possibilities_filled = False
                    solving = False
                    row = 0
                    col = 0
                # start = time.time()

        if event.type == VISUALIZE and solving:
            # if row == 0 and col == 0:
            #     for i in possible_nums.items():
            #         print(i)
            #     print()

            # iterate past any None values
            row, col = iterate(row, col)
            while board[row][col] != None:
                row, col = iterate(row, col)

    # display process can't be in function because it looks buggy
    solved = is_solved()

    if solved:
        solving = False
        # print(time.time() - start)

    valid_nums = []
    invalid_nums = []
    if not solved:
        if board[row][col] == None: #solving:
            for num in range(1, 10):
                valid_num = True
                for i in range(len(board_rects)):  # highlight the column
                    if board[i][col] != None:
                        highlight_rect(board_rects[i][col], (255, 0, 0))  # red
                        if board[i][col] == num:
                            valid_num = False
                    else:
                        highlight_rect(board_rects[i][col], (255, 0, 0, 12))

                for i in range(len(board_rects[row])):  # highlight the row
                    if board[row][i] != None:
                        highlight_rect(board_rects[row][i], (255, 0, 0))  # red
                        if board[row][i] == num:
                            valid_num = False
                    else:
                        highlight_rect(board_rects[row][i], (255, 0, 0, 12))

                # top left
                if row <= 2 and col <= 2:
                    for i in range(0, 3):
                        for k in range(0, 3):
                            if board[i][k] != None:
                                highlight_rect(board_rects[i][k], (255, 0, 0))  # red
                                if board[i][k] == num:
                                    valid_num = False
                            else:
                                highlight_rect(board_rects[i][k], (255, 0, 0, 12))

                # top middle
                elif row <= 2 and col <= 5:
                    for i in range(0, 3):
                        for k in range(3, 6):
                            if board[i][k] != None:
                                highlight_rect(board_rects[i][k], (255, 0, 0))  # red
                                if board[i][k] == num:
                                    valid_num = False
                            else:
                                highlight_rect(board_rects[i][k], (255, 0, 0, 12))

                # top right
                elif row <= 2 and col <= 8:
                    for i in range(0, 3):
                        for k in range(6, 9):
                            if board[i][k] != None:
                                highlight_rect(board_rects[i][k], (255, 0, 0))  # red
                                if board[i][k] == num:
                                    valid_num = False
                            else:
                                highlight_rect(board_rects[i][k], (255, 0, 0, 12))

                # middle left
                elif row <= 5 and col <= 2:
                    for i in range(3, 6):
                        for k in range(0, 3):
                            if board[i][k] != None:
                                highlight_rect(board_rects[i][k], (255, 0, 0))  # red
                                if board[i][k] == num:
                                    valid_num = False
                            else:
                                highlight_rect(board_rects[i][k], (255, 0, 0, 12))

                # middle middle
                elif row <= 5 and col <= 5:
                    for i in range(3, 6):
                        for k in range(3, 6):
                            if board[i][k] != None:
                                highlight_rect(board_rects[i][k], (255, 0, 0))  # red
                                if board[i][k] == num:
                                    valid_num = False
                            else:
                                highlight_rect(board_rects[i][k], (255, 0, 0, 12))

                # middle right
                elif row <= 5 and col <= 8:
                    for i in range(3, 6):
                        for k in range(6, 9):
                            if board[i][k] != None:
                                highlight_rect(board_rects[i][k], (255, 0, 0))  # red
                                if board[i][k] == num:
                                    valid_num = False
                            else:
                                highlight_rect(board_rects[i][k], (255, 0, 0, 12))

                # bottom left
                elif row <= 8 and col <= 2:
                    for i in range(6, 9):
                        for k in range(0, 3):
                            if board[i][k] != None:
                                highlight_rect(board_rects[i][k], (255, 0, 0))  # red
                                if board[i][k] == num:
                                    valid_num = False
                            else:
                                highlight_rect(board_rects[i][k], (255, 0, 0, 12))

                # bottom middle
                elif row <= 8 and col <= 5:
                    for i in range(6, 9):
                        for k in range(3, 6):
                            if board[i][k] != None:
                                highlight_rect(board_rects[i][k], (255, 0, 0))  # red
                                if board[i][k] == num:
                                    valid_num = False
                            else:
                                highlight_rect(board_rects[i][k], (255, 0, 0, 12))

                # bottom right
                elif row <= 8 and col <= 8:
                    for i in range(6, 9):
                        for k in range(6, 9):
                            if board[i][k] != None:
                                highlight_rect(board_rects[i][k], (255, 0, 0))  # red
                                if board[i][k] == num:
                                    valid_num = False
                            else:
                                highlight_rect(board_rects[i][k], (255, 0, 0, 12))

                highlight_rect(board_rects[row][col], (0, 255, 0))  # green

                if valid_num is True:
                    valid_nums.append(num)
                else:
                    invalid_nums.append(num)

    if valid_nums != [] or invalid_nums != []:
        possible_nums[(row, col)] = valid_nums
        impossible_nums[(row, col)] = invalid_nums

    valid_nums = []
    invalid_nums = []
    # check if current location is the only possibility for a number
    if possibilities_filled:
        for possible_num in possible_nums[(row, col)]:
            x, y = (row, col)  # get key at value location
            valid_num = True


            # top left
            if x <= 2 and y <= 2:
                for i in range(0, 3):
                    for k in range(0, 3):
                        if board[i][k] == None and (i != x or k != y):
                            if possible_num in possible_nums[(i, k)]:
                                valid_num = False
                                # print('top left')

            # top middle
            elif x <= 2 and y <= 5:
                for i in range(0, 3):
                    for k in range(3, 6):
                        if board[i][k] == None and (i != x or k != y):
                            if possible_num in possible_nums[(i, k)]:
                                valid_num = False
                                # print('top middle')


            # top right
            elif x <= 2 and y <= 8:
                for i in range(0, 3):
                    for k in range(6, 9):
                        if board[i][k] == None and (i != x or k != y):
                            if possible_num in possible_nums[(i, k)]:
                                valid_num = False
                                # print('top right')


            # middle left
            elif x <= 5 and y <= 2:
                for i in range(3, 6):
                    for k in range(0, 3):
                        if board[i][k] == None and (i != x or k != y):
                            if possible_num in possible_nums[(i, k)]:
                                valid_num = False
                                # print('middle left')


            # middle middle
            elif x <= 5 and y <= 5:
                for i in range(3, 6):
                    for k in range(3, 6):
                        if board[i][k] == None and (i != x or k != y):
                            if possible_num in possible_nums[(i, k)]:
                                valid_num = False
                            # for val in possible_nums[(i, k)]:
                            #     if val == possible_num:
                            #         valid_num = False
                            #         print('middle middle')

            # middle right
            elif x <= 5 and y <= 8:
                for i in range(3, 6):
                    for k in range(6, 9):
                        if board[i][k] == None and (i != x or k != y):
                            if possible_num in possible_nums[(i, k)]:
                                valid_num = False
                                # print('middle right')


            # bottom left
            elif x <= 8 and y <= 2:
                for i in range(6, 9):
                    for k in range(0, 3):
                        if board[i][k] == None and (i != x or k != y):
                            if possible_num in possible_nums[(i, k)]:
                                valid_num = False
                                # print('bottom left')


            # bottom middle
            elif x <= 8 and y <= 5:
                for i in range(6, 9):
                    for k in range(3, 6):
                        if board[i][k] == None and (i != x or k != y):
                            if possible_num in possible_nums[(i, k)]:
                                valid_num = False
                                # print('bottom middle')


            # bottom right
            elif x <= 8 and y <= 8:
                for i in range(6, 9):
                    for k in range(6, 9):
                        if board[i][k] == None and (i != x or k != y):
                            if possible_num in possible_nums[(i, k)]:
                                valid_num = False
                                # print('bottom right')

            if valid_num is True:
                valid_nums.append(possible_num)
            else:
                invalid_nums.append(possible_num)

    if len(valid_nums) == 1:
        possible_nums[(row, col)] = valid_nums
        impossible_nums[(row, col)] = invalid_nums
        # print('lower', valid_nums)

    valid_nums = []
    invalid_nums = []
    # check if current location is the only possibility for a number
    if possibilities_filled:
        for possible_num in possible_nums[(row, col)]:
            x, y = (row, col)  # get key at value location
            valid_num = True

            # go down each row in a column
            for i in range(len(board_rects)):
                if board[i][y] == None and i != x:
                    if possible_num in possible_nums[(i, col)]:
                        # print('rows', possible_nums[(i, col)])
                        valid_num = False

            # go across each column in a row
            for i in range(len(board_rects[row])):
                if board[row][i] == None and i != y:
                    if possible_num in possible_nums[(row, i)]:
                        # print('columns', possible_nums[(row, i)])
                        valid_num = False

            if valid_num is True:
                valid_nums.append(possible_num)
            else:
                invalid_nums.append(possible_num)

    # this will later set it to the current
    if len(valid_nums) == 1:
        possible_nums[(row, col)] = valid_nums
        # print('rows', possible_nums[(row, col)])

    new_nums = {}
    # set valid numbers to board
    for key in possible_nums.keys():
        new_nums[key] = possible_nums[key]
        if len(possible_nums[key]) == 1:
            x, y = key  # get key at value location
            board[x][y] = possible_nums[key][0]

            del new_nums[key]

    # if comes to the end between two numbers choose randomly
    if len(new_nums.keys()) == 4 and possibilities_filled:
        temp = list(new_nums.keys())
        board[row][col] = new_nums[temp[0]][0]

    if solved:
        board = Maker.create_board()
        possible_nums = {}
        impossible_nums = {}
        possibilities_filled = False
        solving = False
        row = 0
        col = 0

    # highlight filled in numbers
    for key in possible_nums.keys():
        x, y = key
        if board[x][y] != None:
            highlight_rect(board_rects[x][y], ((0, 255, 0, 50)))

    display_board()

    clock.tick(144)
    pygame.display.update()
