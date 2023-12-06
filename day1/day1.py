import json
import pdb
import numpy as np

debug = False


class NumberString:
    

    def __init__(self, raw_string):
        self.raw_string = raw_string
        self.numbers = []
        self.short_form_digits = {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"0":0,}
        self.long_form_digits = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"zero":0}
        self.digit_strings = self.short_form_digits|self.long_form_digits 

    def extract_first_digit_part_1(self):
        first_index = len(self.raw_string)
        for key in self.short_form_digits:
            index_of_found_number = self.raw_string.find(key)
            if index_of_found_number != -1:
                if index_of_found_number <= first_index:
                    first_index = index_of_found_number
                    first_index_value = self.short_form_digits[key]
        assert first_index != -1
        return first_index_value
                
    def extract_last_digit_part_1(self):
        last_index = -1
        for key in self.short_form_digits:
            index_of_found_number = self.raw_string.rfind(key)
            if index_of_found_number != -1:
                if index_of_found_number > last_index:
                    last_index = index_of_found_number
                    last_index_value = self.short_form_digits[key]
        assert last_index != -1
        return last_index_value

    def extract_first_digit(self):
        first_index = len(self.raw_string)
        for key in self.digit_strings:
            index_of_found_number = self.raw_string.find(key)
            if index_of_found_number != -1:
                if index_of_found_number <= first_index:
                    first_index = index_of_found_number
                    first_index_value = self.digit_strings[key]
        assert first_index != -1
        return first_index_value


    def extract_last_digit(self):
        last_index = -1
        for key in self.digit_strings:
            index_of_found_number = self.raw_string.rfind(key)
            if index_of_found_number != -1:
                if index_of_found_number > last_index:
                    last_index = index_of_found_number
                    last_index_value = self.digit_strings[key]
        assert last_index != -1
        return last_index_value

    def extract_calibration_value(self, problem_part):
        if "1" in problem_part:
            return int(str(self.extract_first_digit_part_1()) + str(self.extract_last_digit_part_1()))
        else:
            return int(str(self.extract_first_digit()) + str(self.extract_last_digit()))
 

def get_calibration_values_part_1(lines):
    calibration_values = []
    for line in lines:
        line_object = NumberString(line)
        calibration_value = line_object.extract_calibration_value("part 1")
        calibration_values.append(calibration_value)
    return calibration_values


def get_calibration_values_part_2(lines):
    calibration_values = []
    for line in lines:
        line_object = NumberString(line)
        calibration_value = line_object.extract_calibration_value("part 2")
        calibration_values.append(calibration_value)
    return calibration_values



if __name__ == '__main__':

    # read data
    if debug:
        f = open('test.txt')
    else:
        f = open('input.txt')
    input_string = f.read()
    f.close()



    # print(lines)
    lines = input_string.split("\n")
    print("part 1 answer: ", sum(get_calibration_values_part_1(lines))) # should get 55386
    print("part 2 answer: ", sum(get_calibration_values_part_2(lines)))
    if debug:
        assert sum(get_calibration_values_part_1(lines)) == 142
    else:
        assert sum(get_calibration_values_part_1(lines)) == 55386
     
    


    # print(get_calibration_values(lines))