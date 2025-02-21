from Player import Player
from Character import Character
from Map import Map
from Map import Map
import keyboard
import time
import os


def on_w_click(player):
    player.move_up()


def on_a_click(player):
    player.move_left()

def on_s_click(player):
    player.move_down()


def on_d_click(player):
    player.move_right()

def on_space_click(player):
    player.attack()



class Game:
    def __init__(self, map_size_x, map_size_y, player: Player, player_start_x, player_start_y):
        self.map = Map(map_size_x, map_size_y)
        self.player = player
        self.characters: list[Character] = []
        self.add_character(player, player_start_x, player_start_y)
        self.interface = f'''
--------------------------------------------------------
NAME {player.name} | HP {player.hp} | ARM {player.arm} | DMG {player.dmg}
--------------------------------------------------------
w - up | a - left | s - down | d - right | space - attack
'''
        self.bind_keyboard()
    def start(self):
        while True:
            self.map.render()
            print(self.interface)
            self.update_characters()
            time.sleep(0.0001)
            # print("\033c\033[3J", end="")
            os.system('cls')

    def update_characters(self):   
        for character in self.characters:
            if character.hp <= 0:
                character.kill()
                self.characters.remove(character)

    def add_character(self, character: Character, x, y):
        self.characters.append(character)
        self.map.add_character(character, x, y)
    
    def bind_keyboard(self):
        keyboard.add_hotkey('w', lambda: on_w_click(self.player))
        keyboard.add_hotkey('a', lambda: on_a_click(self.player))
        keyboard.add_hotkey('s', lambda: on_s_click(self.player))
        keyboard.add_hotkey('d', lambda: on_d_click(self.player))
        keyboard.add_hotkey('space', lambda: on_space_click(self.player))
