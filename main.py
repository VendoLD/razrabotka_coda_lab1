from Player import Player
from Enemy import Enemy
from Game import Game
import random
import time

random.seed(time.time_ns())


player_name = input('Enter player`s name: ')


map_size = list(map(int, input('Enter map size in format: x, y; Input "0" for default map: ').split(', ')))

if map_size[0] == 0:
    map_size = [10, 10]

while map_size[0] < 10 or map_size[1] < 10:
    map_size =  list(map(int, input('Minimum size: 10x10; Enter map size again: ').split(',')))



player = Player(player_name, hp=100, arm=10, dmg=60)


enemy = Enemy(hp=200, arm=10)
enemy2 = Enemy(hp=100, arm=20)




game = Game(map_size[0], map_size[1], player, 4, 2)

def random_cords():
    x = random.randint(1, map_size[0])
    y = random.randint(1, map_size[1])

    while x == player.character_x and y == player.character_y:
        x = random.randint(1, map_size[0])
        y = random.randint(1, map_size[1])
    return (x, y)



game.add_character(enemy, *random_cords())
game.add_character(enemy2, *random_cords())

game.start()




    
