from Character import Character
from Enemy import Enemy

class Player(Character):
    def __init__(self, name, hp, arm, dmg):
        super().__init__(hp, arm)
        self.dmg = dmg
        self.name = name
        self.map_char = 'P'

    def attack(self):
        enemies_to_attack: list[Enemy] = self.enemies_around()
        for enemy in enemies_to_attack:
            damage = self.dmg - enemy.arm
            if damage > 0:
                enemy.hp -= damage
                
    
    def enemies_around(self):
        cords = [self.map.map_list[self.character_y + 1][self.character_x],
             self.map.map_list[self.character_y - 1][self.character_x],
             self.map.map_list[self.character_y][self.character_x + 1],
             self.map.map_list[self.character_y][self.character_x - 1]]

        result = []
        for i in cords:
            if isinstance(i, Enemy):
                result.append(i)
        return result