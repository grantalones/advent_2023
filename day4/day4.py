import json
import pdb
import numpy as np

debug = False


class ScratcherCard:
    def __init__(self, raw_string):
        self.raw_string = raw_string
        self.card_id, self.winning_numbers, self.playing_numbers = self.read_card()
        self.rounds_won, self.score_of_card = self.score_of_card()

    def read_card(self):
        card_text = self.raw_string
        card_id, card_content = self.raw_string.split(":")
        card_id = int(card_id.replace("Card ", ""))
        winning_numbers, playing_numbers = [NumberSet(number_string) for number_string in card_content.split("|")]
        return card_id, winning_numbers, playing_numbers

    def score_of_card(self):
        rounds_won = len(self.winning_numbers.number_set.intersection(self.playing_numbers.number_set))
        if rounds_won == 0:
            return 0, 0
        return rounds_won ,2**(rounds_won - 1)


class NumberSet:
    def __init__(self, number_string):
        self.number_string = number_string
        self.number_array = self.read_number_string()
        self.number_set = set(self.number_array)

    def read_number_string(self):
        return list(filter(None, self.number_string.split(" ")))


class Deck:
    def __init__(self, raw_string):
        self.num_plays = {1:0}
        lines = raw_string.split("\n")
        self.num_cards = len(lines)
        sum_of_scores = 0
        for line in lines:
            card = ScratcherCard(line)
            sum_of_scores += card.score_of_card
            self.update_num_plays(card)
        self.sum_of_scores = sum_of_scores
        self.total_number_of_plays = sum(list(self.num_plays.values()))
    
    def update_num_plays(self, card):
        card_wins = card.rounds_won
        card_id = card.card_id

        if card.card_id not in self.num_plays.keys():
                self.num_plays[card.card_id] = 1 #create self-game
        else:
            self.num_plays[card.card_id] += 1 #increment from self-game
        
        for i in range(card_id+1, card_id+card_wins+1):#copy the correct number of cards
            if i > self.num_cards:#don't worry about cards that don't exist
                return
            elif i in self.num_plays.keys():#if we have already made a copy of the card
                self.num_plays[i] += self.num_plays[card_id]#add the number of times that it's parent played to it
            else: #if this is the first time we're making a copy of the card
                self.num_plays[i] = self.num_plays[card_id]#play it as many times as its parent


if __name__ == '__main__':

    # read data
    if debug:
        f = open('test.txt')
    else:
        f = open('input.txt')
    input_string = f.read()
    f.close()

    deck = Deck(input_string)

    part_1 = deck.sum_of_scores
    part_2 = deck.total_number_of_plays

    print("part 1 answer: ", part_1)
    print("part 2 answer: ", part_2)
    
    if debug:
        assert part_1 == 13
        assert part_2 == 30
    else:
        assert part_1 == 32001




