import keyboard
import os
import time

map_size = list(map(int,(input('Enter map size in format: x, y; Input "0" for default map').split(', '))))

if map_size == 0:
    MAP = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
        ['#', '.', '.', '.', 'P', '.', '.', '.', '.', '.', '.', '.', '.', '#'], 
        ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'], 
        ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'], 
        ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'], 
        ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]
else:
    MAP = []
    for i in range(map_size[1]):
        MAP.append([])
        for j in range(map_size[0]):
            if i == 0 or i == (map_size[1] - 1) or j == 0 or j == map_size[0] - 1:
                MAP[i].append('#')
            else:
                MAP[i].append('.')


CHARACTER_INDEX_X = 4
CHARACTER_INDEX_Y = 2


def render(map):
    for string in map:
        for char in string:
            print(char, end=' ')
        print()

    # os.system('cls')


def move_up(map, x, y):
    if map[y - 1][x] == '#':
        return
    map[y][x], map[y - 1][x] = map[y - 1][x], map[y][x]
    y -= 1
    global CHARACTER_INDEX_Y
    CHARACTER_INDEX_Y = y


def move_left(map, x, y):
    if map[y][x - 1] == '#':
        return
    map[y][x], map[y][x - 1] = map[y][x - 1], map[y][x]
    x -= 1
    global CHARACTER_INDEX_X
    CHARACTER_INDEX_X = x


def move_down(map, x, y):
    if map[y + 1][x] == '#':
        return
    map[y][x], map[y + 1][x] = map[y + 1][x], map[y][x]
    y += 1 
    global CHARACTER_INDEX_Y
    CHARACTER_INDEX_Y = y


def move_right(map, x, y):
    if map[y][x + 1] == '#':
        return
    map[y][x], map[y][x + 1] = map[y][x + 1], map[y][x]
    x += 1
    global CHARACTER_INDEX_X
    CHARACTER_INDEX_X = x


def on_w_click():
    move_up(MAP, CHARACTER_INDEX_X, CHARACTER_INDEX_Y)

def on_a_click():
    move_left(MAP, CHARACTER_INDEX_X, CHARACTER_INDEX_Y)

def on_s_click():
    move_down(MAP, CHARACTER_INDEX_X, CHARACTER_INDEX_Y)


def on_d_click():
    move_right(MAP, CHARACTER_INDEX_X, CHARACTER_INDEX_Y)


keyboard.add_hotkey('w', on_w_click)
keyboard.add_hotkey('a', on_a_click)
keyboard.add_hotkey('s', on_s_click)
keyboard.add_hotkey('d', on_d_click)



while True:
    render(MAP)
    time.sleep(0.001)
    os.system('cls')


    
