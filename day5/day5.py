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

    def parse_input(self, list_or_range):
        instructions = self.raw_string.split('\n\n')
        for instruction in instructions:

            title, locations = instruction.split(":")

            locations = list(filter(None, locations.split('\n')))
            if title == "seeds":
                # create SeedList
                if list_or_range == "list":
                    seed_list = SeedList(title, locations[0])
                else:
                    seed_list = SeedRange(title, locations[0])
                self.seeds = seed_list.seeds
            else:
                # create AlmanacMap
                # key is map_title
                # values are mappings
                almanac_map = AlmanacMap(title, locations)
                self.instructions[almanac_map.source] = almanac_map

    def get_closest_location(self):
        destinations = {}
        # paths = []
        for seed in self.seeds:
            # path = []

            current_destination = seed
            source_choice = "seed"
            while source_choice != 'location':
                current_map = self.instructions[source_choice]
                current_destination = current_map.get_destination(current_destination)
                source_choice = current_map.destination
            destinations[seed] = current_destination
        return min(list(destinations.values()))
 
class AlmanacMap:
    def __init__(self, title, instructions):
        self.title = title
        self.source, self.destination = self.get_source_and_destination()
        self.mappings = self.create_mappings(instructions)

    def describe(self):
        print(self.title, self.mappings)

    def create_mappings(self, mappings):
        mapping_array = []

        for mapping_string in mappings:
            destination_start, source_start, mapping_range = list(map(int, mapping_string.split(" ")))
            source_destination_diff = destination_start - source_start
            mapping_array.append({"source_start":source_start, "source_end":mapping_range + source_start, "offset":source_destination_diff})
            
        return mapping_array

    def get_source_and_destination(self):
        title = self.title
        title = title.replace(" map", "")
        return title.split("-to-")

    def get_destination(self, source):
        source = int(source)

        for mapping in self.mappings:
            if mapping["source_start"] <= source <= mapping["source_end"]:
                return source + mapping["offset"]
        return source

class SeedList:
    def __init__(self, title, seed_list_string):
        self.title = title
        self.seeds = self.create_seed_list(seed_list_string)

    def describe(self):
        print(self.title, self.seeds)

    def create_seed_list(self, seed_list_string):
        return list(map(int, filter(None, seed_list_string.split(" "))))

class SeedRange(SeedList):
    def __init__(self, title, seed_list_string):
        super().__init__(title, seed_list_string)

    def create_seed_list(self, seed_list_string):
        seed_list = list(map(int, filter(None, seed_list_string.split(" "))))
        
        starters = seed_list[::2]
        ranges = seed_list[1::2]
        seeds = []
        for index, starter in enumerate(starters):
            seeds.append({starter, starter+ranges[index]})
        print("done importing seed range")
        pdb.set_trace()
        return seeds



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



