from Player import Player
from Enemy import Enemy
from Game import Game


player_name = input('Enter player`s name: ')
map_size = list(map(int, input('Enter map size in format: x, y; Input "0" for default map: ').split(', ')))

if map_size[0] == 0:
    map_size = [10, 10]


player = Player(player_name, 100, 10, 60)


enemy = Enemy(200, 10)
enemy2 = Enemy(100, 20)


game = Game(map_size[0], map_size[1], player, 4, 2)

game.add_character(enemy, 3, 5)
game.add_character(enemy2, 3, 7)

game.start()




    
