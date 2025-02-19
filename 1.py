import keyboard
import os
import time

map_size = list(map(int, input('Enter map size in format: x, y; Input "0" for default map: ').split(', ')))

# MAP = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
#         ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
#         ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'], 
#         ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'], 
#         ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'], 
#         ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'], 
#         ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
#         ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
#         ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]

def map_generation():
    if map_size[0] == 0:
        MAP = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
            ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'], 
            ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'], 
            ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'], 
            ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'], 
            ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
            ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]
    else:
        if map_size[0] < 5 or map_size[1] < 5:
            print('Minimum map size: 5x5')
            return 
        MAP = []
        for i in range(map_size[1] + 1):
            MAP.append([])
            for j in range(map_size[0] + 1):
                if i == 0 or i == map_size[1] or j == 0 or j == map_size[0]:
                    MAP[i].append('#')
                else:
                    MAP[i].append('.')
    return MAP

MAP = map_generation()





class Character:
    def __init__(self, hp, arm, dmg):
        self.hp = hp
        self.arm = arm
        self.dmg = dmg
        self.map : Map = None
        self.character_x = None
        self.character_y = None

    
    def move_up(self):
        self.map.move_character(self, 0, -1)


    def move_left(self):
        self.map.move_character(self, -1, 0)


    def move_down(self):
        self.map.move_character(self, 0, 1)


    def move_right(self):
        self.map.move_character(self, 1, 0)
    

    def kill(self):
        self.map.remove_character(self)



class Map:
    def __init__(self, map_list: list[list]):
        self.map_list = map_list
        self.player = None
        self.enemies = []
    
    def add_character(self, character: Character, x, y):
        if self.map_list[y][x] != '.':
            return 
        
        self.map_list[y][x] = character

        if isinstance(character, Player):
            self.player = character
        else:
            self.enemies.append(character)
        
        character.map = self
        character.character_x = x
        character.character_y = y
    
    def remove_character(self, character: Character):
        x = character.character_x
        y = character.character_y

        self.map_list[y][x] = '.'

        del character

    def move_character(self, character: Character, x_move, y_move):
        current_x = character.character_x
        current_y = character.character_y

        new_x = character.character_x + x_move
        new_y = character.character_y + y_move

        if self.map_list[new_y][new_x] != '.':
            return
        
        self.map_list[current_y][current_x], self.map_list[new_y][new_x] = self.map_list[new_y][new_x], self.map_list[current_y][current_x]

        character.character_x = new_x
        character.character_y = new_y

    def enemies_around(self):
        l = [self.map_list[self.player.character_y + 1][self.player.character_x]]
        l.append(self.map_list[self.player.character_y - 1][self.player.character_x])
        l.append(self.map_list[self.player.character_y][self.player.character_x + 1])
        l.append(self.map_list[self.player.character_y][self.player.character_x - 1])
        result = []
        for i in l:
            if isinstance(i, Enemy):
                result.append(i)
        return result


    def render(self):
        for string in self.map_list:
            for char in string:
                if isinstance(char, Player):
                    print('P', end=' ')
                elif isinstance(char, Enemy):
                    print('E', end=' ')
                else:
                    print(char, end=' ')
            print()


class Enemy(Character):
    pass



class Player(Character):
    def __init__(self, name, hp, arm, dmg):
        super().__init__(hp, arm, dmg)
        self.name = name

    def attack(self):
        enemies_to_attack = self.map.enemies_around()
        for enemy in enemies_to_attack:
            enemy.hp -= 100
            if enemy.hp <= 0:
                enemy.kill()










def on_w_click():
    player.move_up()

def on_a_click():
    player.move_left()

def on_s_click():
    player.move_down()


def on_d_click():
    player.move_right()

def on_space_click():
    player.attack()


keyboard.add_hotkey('w', on_w_click)
keyboard.add_hotkey('a', on_a_click)
keyboard.add_hotkey('s', on_s_click)
keyboard.add_hotkey('d', on_d_click)
keyboard.add_hotkey('space', on_space_click)

# def render(map):
#     for string in map:
#         for char in string:
#             if isinstance(char, Character):
#                 print('P', end=' ')
#             else:
#                 print(char, end=' ')
#         print()




player = Player('Player123', 100, 10, 10)
enemy = Enemy(10, 10, 10)
enemy2 = Enemy(100, 10, 10)
map = Map(MAP)


map.add_character(player, 4, 3)
map.add_character(enemy, 6, 3)
map.add_character(enemy2, 5, 2)


INTERFACE = f'''
--------------------------------------------------------
NAME {player.name} | HP {player.hp} | ARM {player.arm} | DMG {player.dmg}
--------------------------------------------------------
w - up | a - left | s - down | d - right | space - attack
'''

while True:
    map.render()
    print(INTERFACE)
    time.sleep(0.001)
    os.system('cls')


    
