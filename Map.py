
class Map:
    def __init__(self, x_size, y_size):
        self.map_list = []
        for i in range(y_size + 1):
            self.map_list.append([])
            for j in range(x_size + 1):
                if i == 0 or i == y_size or j == 0 or j == x_size:
                    self.map_list[i].append('#')
                else:
                    self.map_list[i].append('.')
    
    def add_character(self, character, x, y):
        if self.map_list[y][x] != '.':
            return 
        
        self.map_list[y][x] = character
        
        character.map = self
        character.character_x = x
        character.character_y = y
    
    def remove_character(self, character):
        x = character.character_x
        y = character.character_y

        self.map_list[y][x] = '.'

    def move_character(self, character, x_move, y_move):
        current_x = character.character_x
        current_y = character.character_y

        new_x = character.character_x + x_move
        new_y = character.character_y + y_move

        if self.map_list[new_y][new_x] != '.':
            return
        
        self.map_list[current_y][current_x], self.map_list[new_y][new_x] = self.map_list[new_y][new_x], self.map_list[current_y][current_x]

        character.character_x = new_x
        character.character_y = new_y


    def render(self):
        from Character import Character
        for string in self.map_list:
            for el in string:
                if isinstance(el, Character):
                    print(el.map_char, end=' ')
                else:
                    print(el, end=' ')
            print()
        
