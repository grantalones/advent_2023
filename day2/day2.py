import json
import pdb
import numpy as np
# only 12 red cubes, 13 green cubes, and 14 blue cubes
debug = False

class CubeGame:
    def __init__(self, game_string):
        self.game_string = game_string
        self.game_id = self.get_game_id(self.game_string)
        self.draws = self.get_draws(self.game_string)
        self.color_amounts = self.get_color_amounts()
        self.valid_game = self.valid_game({"red":12, "green":13, "blue":14})
        self.game_power = self.get_game_power()

    def get_game_id(self, game_string):
        return int(game_string.split(":")[0].replace("Game ", ""))


    def get_draws(self, game_string):
        draws = []
        for game_round in game_string.split(": ")[1].split("; "):
            draws.append(game_round.split())

        return game_string.split(": ")[1].split("; ")

    def get_color_amounts(self):
        color_amounts = []
        for draw in self.draws:
            game_info = {}
            for cube_group in draw.split(", "):
                info = cube_group.split(" ")
                color, count = info[1], int(info[0])
                game_info[color] = count
            color_amounts.append(game_info)
        return color_amounts

    def valid_game(self, cube_requirements):
        for a_round in self.color_amounts:
            for color in a_round:
                if a_round[color] <= cube_requirements[color]:
                    continue
                else:
                    return False
        return True

    def get_minimum_dice_needed(self):
        min_dice_needed = {"red":0, "blue":0, "green":0}
        for a_round in self.color_amounts:
            for color in a_round:
                if a_round[color] > min_dice_needed[color]:
                    min_dice_needed[color] = a_round[color]
        print (self.draws, min_dice_needed)
        return min_dice_needed

    def get_game_power(self):
        power_dict = self.get_minimum_dice_needed()
        return power_dict['blue'] * power_dict['green'] * power_dict['red'] 



if __name__ == '__main__':

    cube_requirements = {"red":12, "green":13, "blue":14}
    # read data
    if debug:
        f = open('test.txt')
    else:
        f = open('input.txt')
    input_string = f.read()
    f.close()



    lines = input_string.split("\n")
    game_sum_part_1 = 0
    game_sum_part_2 = 0

    for line in lines:
        game_1 = CubeGame(line)

        if game_1.valid_game:
            game_sum_part_1 += game_1.game_id

    for line in lines:
        game_2 = CubeGame(line)
        game_sum_part_2 += game_2.game_power
    

    print("part 1 answer: " + str(game_sum_part_1))
    print("part 2 answer: " + str(game_sum_part_2))
    if debug:
        assert  game_sum_part_1 == 8
        assert  game_sum_part_2 == 2286
    else:
        assert game_sum_part_1 == 2528
     
    
