import json
import pdb
import numpy as np
import time

debug = True


class Almanac:
    def __init__(self, input_string, list_or_range):
        self.raw_string = input_string
        self.seeds = []
        self.instructions = {}
        self.parse_input(list_or_range)





if __name__ == '__main__':
    start_time = time.time()
    # read data
    if debug:
        f = open('test.txt')
    else:
        f = open('input.txt')
    input_string = f.read()
    f.close()

    part1_almanac = Almanac(input_string, "list")
    part2_almanac = Almanac(input_string, "range")

    part_1 = part1_almanac.get_closest_location()
    part_2 = part2_almanac.get_closest_location()



    print("part 1 answer: ", part_1)
    print("part 2 answer: ", part_2)
    
    if debug:
        assert part_1 == 35
        assert part_2 == 46
    else:
        assert part_1 == 227653707
    print("--- %s seconds ---" % (time.time() - start_time))



