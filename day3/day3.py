import json
import pdb
import numpy as np

debug = True

class EngineSchematic:
    def __init__(self, schematic_string):
        
        self.schematic_string = schematic_string
        self.rows = schematic_string.split('\n') #array type


        
    def is_symbol(character):
        symbol_string = "@#$%&*+=-/"
        if character in symbol_string:
            return True
        return False

    def get_number_positions(schematic):
        current_number = ""
        current_start_position = 0
        current_end_position = 0
        

    def get_number_positions(self):
        number_positions = {}
        for char in self.schematic_string:
            if char == ".":
                continue
            else

    def get_symbol_positions(self):




if __name__ == '__main__':

    # read data
    if debug:
        f = open('test.txt')
    else:
        f = open('input.txt')
    input_string = f.read()
    f.close()



    lines = input_string.split("\n")
    engine_parts_sum_1 = 0
    engine_parts_sum_2 = 0

    for line in lines:
        engine = EngineSchematic(line)

        if game_1.valid_game:
            game_sum_part_1 += game_1.game_id

    for line in lines:
        game_2 = CubeGame(line)
        game_sum_part_2 += game_2.game_power
    

    print("part 1 answer: " + str(game_sum_part_1))
    print("part 2 answer: " + str(game_sum_part_2))
    if debug:
        assert  part_1 == 4361
        # assert  game_sum_part_2 == 2286
    else:
        # assert game_sum_part_1 == 2528
     
    
