import pygame, ctypes
from tkinter import *
import numpy as np

user32 = ctypes.windll.user32
screensize = (user32.GetSystemMetrics(1) - 80, user32.GetSystemMetrics(1) - 80)  # get screensize
WIDTH, HEIGHT = screensize
divisor = 1
array_len = int(WIDTH / divisor)
speed = 1


def generate_numbers(a, d):
    lst = np.array([i for i in range(a)])

    arr = np.random.choice(lst, size=a, replace=False)

    rects = []
    for i, val in enumerate(arr):
        rects.append(pygame.Rect(i * d, (HEIGHT - val) - val * (d - 1), d, val * d))

    return (lst, arr, rects)


def set_divisor(n):
    global divisor
    global array_len

    divisor = n
    array_len = int(WIDTH / divisor)


def set_speed(s):
    global speed

    speed = s


def menu():
    def get_sort_type(sort_type):
        pygame.quit()
        root.destroy()
        main(sort_type)

    root = Tk()
    root.configure(bg='black')
    root.title('Sorting Algorithms')
    root.geometry('300x340')

    selection_button = Button(root, text='SELECTION\nO(n^2)', width=10, height=5, bd=5, bg='GREEN', fg='WHITE',
                              command=lambda: get_sort_type('selection'))
    selection_button.grid(row=0, column=0, padx=5, pady=5)

    insertion_button = Button(root, text='INSERTION\nO(n^2)', width=10, height=5, bd=5, bg='GREEN', fg='WHITE',
                              command=lambda: get_sort_type('insertion'))
    insertion_button.grid(row=0, column=1, padx=5, pady=5)

    bubble_button = Button(root, text='BUBBLE\nO(n^2)', width=10, height=5, bd=5, bg='GREEN', fg='WHITE',
                           command=lambda: get_sort_type('bubble'))
    bubble_button.grid(row=0, column=2, padx=5, pady=5)

    divisor_label = Label(root, width=10, height=5, bg='BLACK')
    divisor_label.grid(row=1, column=1)

    divisor_prompt = Label(divisor_label, text='Set Divisor\nDefault=1', width=10, height=2, bg='BLACK', fg='WHITE')
    divisor_prompt.pack(pady=5)

    divisor_scale = Scale(divisor_label, from_=1, to=10, orient=HORIZONTAL)
    divisor_scale.pack(pady=5)

    divisor_button = Button(divisor_label, text='Set Divisor', bg='GREEN', fg='WHITE', bd=5,
                            command=lambda: set_divisor(int(divisor_scale.get())))
    divisor_button.pack(pady=5)

    speed_scale = Scale(divisor_label, from_=1, to=10, orient=HORIZONTAL)
    speed_scale.pack(pady=5)

    speed_button = Button(divisor_label, text='Set Sort Speed', bg='GREEN', fg='WHITE', bd=5,
                          command=lambda: set_speed(int(speed_scale.get())))
    speed_button.pack(pady=5)

    # heap_button = Button(root, text='HEAP\nO(n log(n))', width=10, height=5, bd=5, bg='GREEN',
    #                        command=lambda: get_sort_type('heap'))
    # heap_button.grid(row=1, column=0)
    #
    # quick_button = Button(root, text='QUICK\nO(n log(n))', width=10, height=5, bd=5, bg='GREEN',
    #                      command=lambda: get_sort_type('quick'))
    # quick_button.grid(row=1, column=1)
    #
    # merge_button = Button(root, text='MERGE\nO(n log(n))', width=10, height=5, bd=5, bg='GREEN',
    #                      command=lambda: get_sort_type('merge'))
    # merge_button.grid(row=1, column=2)

    root.mainloop()


colors = ['WHITE' for i in range(array_len)]


def main(sorting_type):
    pygame.init()

    screen = pygame.display.set_mode(screensize)
    pygame.display.set_caption('Sorting Algorithm')
    clock = pygame.time.Clock()

    # generate numbers in random order
    lst, arr, rects = generate_numbers(array_len, divisor)

    # slow the sorting process for visual
    VISUALIZE = pygame.USEREVENT
    pygame.time.set_timer(VISUALIZE, int(8 * divisor / speed + 0.5))

    # general
    font = pygame.font.Font('freesansbold.ttf', 24)
    final_animate = False

    global colors
    global i
    i = 0

    def display_start():
        overText = font.render('PRESS SPACE TO SORT', True, (255, 255, 255))
        screen.blit(overText, (WIDTH / 2 - 200, 0))


    def display_randomize():
        overText = font.render('PRESS SPACE TO RANDOMIZE', True, (255, 255, 255))
        screen.blit(overText, (WIDTH / 2 - 200, 0))


    def display_rects(rects):
        for i in range(len(rects)):
            pygame.draw.rect(screen, colors[i], rects[i])


    def animate(color):
        global i
        colors[i] = color

        try:
            colors[i + 1] = color  # to make it go faster
            colors[i + 2] = color
            colors[i + 3] = color
        except:
            pass
        i += 4


    def generate_numbers_animate():
        global i
        global colors

        val = arr[i]
        rects[i] = (pygame.Rect(i * divisor, (HEIGHT - val) - val * (divisor - 1), divisor, val * divisor))

        i += 1

        return rects


    def is_sort_finished(arr):
        n = len(arr)

        for i in range(n - 1):
            if arr[i].height > arr[i + 1].height:
                return False

        return True


    def selection_sort(rects):
        global i
        global colors

        if i < array_len:
            min_idx = i
            for j in range(i + 1, array_len):
                colors[j] = 'RED'
                if rects[min_idx].height > rects[j].height:
                    min_idx = j

            rects[i].y, rects[min_idx].y = rects[min_idx].y, rects[i].y
            rects[i].height, rects[min_idx].height = rects[min_idx].height, rects[i].height

            i += 1


    def insertion_sort(rects):
        global i
        global colors

        key = rects[i].height
        y_coord = rects[i].y

        j = i - 1
        while j >= 0 and key < rects[j].height:
            colors[j + 1] = 'RED'
            rects[j + 1].y = rects[j].y
            rects[j + 1].height = rects[j].height
            j -= 1

        rects[j + 1].y = y_coord
        rects[j + 1].height = key

        i += 1


    def bubble_sort(rects):
        global i
        global colors

        n = len(rects)

        for j in range(0, n - i - 1):
            colors[j] = 'RED'
            if rects[j].height > rects[j + 1].height:
                rects[j].y, rects[j + 1].y = rects[j + 1].y, rects[j].y
                rects[j].height, rects[j + 1].height = rects[j + 1].height, rects[j].height

        i += 1


    gen_new = False
    gen_new_animate = False
    sorting = False
    running = True
    while running:

        screen.fill((0, 0, 0))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE and not gen_new and not gen_new_animate:

                    i = 0
                    if is_sort_finished(rects) or sorting or final_animate:
                        gen_new = True
                        sorting = False
                        final_animate = False

                    elif not gen_new:
                        sorting = True

            if event.type == VISUALIZE:

                if sorting:

                    if sorting_type == 'selection':
                        selection_sort(rects)
                    elif sorting_type == 'insertion':
                        insertion_sort(rects)
                    elif sorting_type == 'bubble':
                        bubble_sort(rects)

                if gen_new:

                    try:
                        rects = generate_numbers_animate()
                        colors[0] = 'RED'
                        colors[i] = 'RED'

                    except:
                        gen_new = False
                        i = 0
                        gen_new_animate = True

                if gen_new_animate and i < array_len:
                    animate('WHITE')

                    if i >= array_len - 5:
                        gen_new_animate = False

                if is_sort_finished(rects) and sorting is True:  # if finished sorting

                    for i in range(len(colors)):
                        colors[i] = 'WHITE'

                    sorting = False
                    final_animate = True
                    i = 0

                if final_animate:

                    sorting = False
                    if i >= array_len:  # check if all rects are green
                        final_animate = False

                        # generate new numbers
                        lst = np.array([i for i in range(array_len)])

                        arr = np.random.choice(lst, size=array_len, replace=False)

                        # menu() # crashes often so removed

                    else:
                        animate('GREEN')

        if not sorting and not final_animate and not gen_new and not is_sort_finished(rects):
            display_start()

        elif is_sort_finished(rects) and not final_animate:
            display_randomize()

        display_rects(rects)

        if not final_animate and not gen_new and not is_sort_finished(rects) and not gen_new_animate:

            for k in range(len(colors)):
                colors[k] = 'WHITE'

        if sorting and (sorting_type == 'selection' or sorting_type == 'insertion'):
            colors[i - 1] = 'GREEN'

        if sorting and sorting_type == 'bubble':
            colors[array_len - i - 1] = 'GREEN'

        clock.tick(144)
        pygame.display.update()


menu()
