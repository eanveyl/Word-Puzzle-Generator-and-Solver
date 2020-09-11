

import wr_generator
import json

filename = "word_database/words_dictionary.json"
with open(filename) as words_json:
    word_dict = json.load(words_json)
    word_list = list(word_dict)  # nice

wr_generator.create_game(10, 10, 1, 5, word_list)




