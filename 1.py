import keyboard
import os
import time

map_size = list(map(int, input('Enter map size in format: x, y; Input "0" for default map').split(', ')))

MAP = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', 'P', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'], 
        ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'], 
        ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'], 
        ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'], 
        ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]


# if map_size[0] == 0:
#     MAP = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
#         ['#', 'P', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
#         ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'], 
#         ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'], 
#         ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'], 
#         ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'], 
#         ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
#         ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
#         ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]
# else:
#     MAP = []
#     for i in range(map_size[1]):
#         MAP.append([])
#         for j in range(map_size[0]):
#             if i == 0 or i == (map_size[1] - 1) or j == 0 or j == map_size[0] - 1:
#                 MAP[i].append('#')
#             else:
#                 MAP[i].append('.')


INTERFACE = [['-', '-', '-', '-', '-']]




class Character:
    def __init__(self, start_x, start_y, map):
        self.character_x = start_x
        self.character_y = start_y
        self.map = map


    def move(self, x_move, y_move):

        new_x = self.character_x + x_move
        new_y = self.character_y + y_move

        if self.map[new_y][new_x] == '#':
            return
        
        self.map[self.character_y][self.character_x], self.map[new_y][new_x] = self.map[new_y][new_x], self.map[self.character_y][self.character_x]

        self.character_x = new_x
        self.character_y = new_y
    
    def move_up(self):
        self.move(0, -1)


    def move_left(self):
        self.move(-1, 0)


    def move_down(self):
        self.move(0, 1)


    def move_right(self):
        self.move(1, 0)






def render(map):
    for string in map:
        for char in string:
            print(char, end=' ')
        print()





character = Character(1, 1, MAP)


def on_w_click():
    character.move_up()

def on_a_click():
    character.move_left()

def on_s_click():
    character.move_down()


def on_d_click():
    character.move_right()


keyboard.add_hotkey('w', on_w_click)
keyboard.add_hotkey('a', on_a_click)
keyboard.add_hotkey('s', on_s_click)
keyboard.add_hotkey('d', on_d_click)



while True:
    render(MAP)
    time.sleep(0.001)
    os.system('cls')


    
