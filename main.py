

import wr_generator
import json  # To import the complete word database containing fcking difficult words
import pickle  # To import the easy words dumped from pickle from a nltk.tokenize function



difficulty_level = input("Give the difficulty level: [easy/hard]")
if difficulty_level == "easy":
    filename = "word_database/easy_words_database.txt"
    with open(filename, "rb") as words_text:
        word_list = pickle.load(words_text)
    # Todo something here
else:
    filename = "word_database/words_dictionary.json"
    with open(filename) as words_json:
        word_dict = json.load(words_json)
        word_list = list(word_dict)  # nice

wr_generator.create_game(10, 10, 1, 5, word_list)




