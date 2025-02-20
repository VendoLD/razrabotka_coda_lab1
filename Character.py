from Map import Map

class Character:
    def __init__(self, hp, arm):
        self.hp = hp
        self.arm = arm
        self.map : Map = None
        self.character_x = None
        self.character_y = None
        self.map_char = None

    
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
        