import json
import pdb
import numpy as np

debug = False

class EngineSchematic:
    def __init__(self, schematic_string):
        
        self.schematic_string = schematic_string
        self.rows = schematic_string.split('\n') #array type
        self.num_rows, self.num_cols = self.get_schematic_size()
        self.symbols = self.get_symbol_positions()
        self.numbers = self.get_number_positions()
        self.adjacent_numbers = self.get_adjacent_numbers()


    def get_number_positions(self):
        current_number, current_start_position, current_end_position = "", 0 ,0
        numbers = []
        in_number = False
        for index, char in enumerate(self.schematic_string):
            if char in "1234567890":
                if in_number == False:
                    current_start_position = index
                in_number = True
                current_number += char
            else:
                if in_number == True:
                    current_end_position = index-1
                    row = current_start_position//self.num_cols
                    col_span = [current_start_position%self.num_cols, current_end_position%self.num_cols]
                    corners = [(row-1, col_span[0]-1),(row-1, col_span[1]+1),(row+1, col_span[0]-1),(row+1, col_span[1]+1)]
                    numbers.append({
                        "num":int(current_number), 
                        "pos":{
                            # "start":current_start_position, 
                            # "end":current_end_position,
                            "corners":corners,
                            "highlight":self.get_highlight(corners)
                            # "row":row,
                            # "col_span":col_span
                            }})
                    current_number, current_start_position, current_end_position = "", 0 ,0
                in_number = False
        return numbers

    def get_symbol_positions(self):
        current_position = 0
        symbols = []
        for index, char in enumerate(self.schematic_string):
            if is_symbol(char):
                symbols.append({"char":char,
                    "position":index, 
                    "row":index//self.num_cols, 
                    "col":index%self.num_cols,
                    "adjacent_numbers":[]})
                #assert index == self.relative_to_absolute(((index//self.num_cols), (index%self.num_cols)))
            else:
                continue
        return symbols

    def get_schematic_size(self):
        return (self.get_num_rows(), self.get_num_cols())

    def get_num_rows(self):
        return self.schematic_string.count('\n')+1
    def get_num_cols(self):
        return len(self.schematic_string.split('\n')[0])+1

    def get_highlight(self, corners):
        top_left = corners[0]
        bottom_right = corners[3]
        highlight = []
        for row in range(top_left[0], bottom_right[0]+1):
            for col in range(top_left[1], bottom_right[1]+1):
                highlight.append((row,col))
        return highlight

    def get_adjacent_numbers(self):
        adjacent_numbers = []
        for num in self.numbers:
            for symbol in self.symbols:
                if (symbol["row"], symbol["col"]) in num["pos"]["highlight"]:
                    adjacent_numbers.append(num["num"])
                    symbol["adjacent_numbers"].append(num["num"])
        return adjacent_numbers

    def get_gear_ratio_sum(self):
        gear_ratio = 0
        for symbol in self.symbols:
            if len(symbol["adjacent_numbers"]) == 2:
                gear_ratio = gear_ratio + (symbol["adjacent_numbers"][0]*symbol["adjacent_numbers"][1])
        return gear_ratio


def is_symbol(character):
        symbol_string = "@#$%&*+=-/"
        if character in symbol_string:
            return True
        return False

if __name__ == '__main__':

    # read data
    if debug:
        f = open('test.txt')
    else:
        f = open('input.txt')
    input_string = f.read()
    f.close()

    engine = EngineSchematic(input_string)
    # print(engine.get_number_positions())
    # print(engine.get_symbol_positions())
    # print("rows", engine.num_rows, "cols", engine.num_cols)
    # print(engine.adjacent_numbers)

    print("part 1 answer: ", sum(engine.adjacent_numbers))

    print("part 2 answer: ", engine.get_gear_ratio_sum())

    if debug:
        assert sum(engine.adjacent_numbers) == 4361
        assert engine.get_gear_ratio_sum() == 467835





    
