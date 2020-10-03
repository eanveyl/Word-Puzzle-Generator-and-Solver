# generate game


import numpy
import random


def create_game(size_w_user_input, size_l_user_input, num_of_words_h, num_of_words_v, word_list):
    global lexicon
    global size_w
    global size_l
    global board
    lexicon = word_list
    size_w = size_w_user_input
    size_l = size_l_user_input
    board = numpy.zeros((size_w, size_l), dtype=str)
    print(board)
    fill_horizontal(num_of_words_h)
    print(board)
    fill_vertical(num_of_words_v)
    # fill_board()
    print(board)


def get_word():
    #dictionary = ["HELLO", "WORLD", "SAND", "SHERIF", "CURLS", "SIMBA", "CLOUT", "EXCURSION", "SETTLE", "RABBIT"]
    #random_word = random.randint(0, len(dictionary) - 1)
    global lexicon
    return (random.choice(lexicon)).upper()


def check_row_availability(row):
    i = 0
    while i < size_w:
        if row[i] == "" or " ":
            i += 1
            continue
        else:
            return 0
    return 1


def check_col_availability(col):
    i = 0
    while i < size_l:
        if col[i] == "" or " ":
            i += 1
            continue
        else:
            return 0
    return 1


# broken
def advanced_col_availability_check(col, word):
    i = 0
    j = 0
    while j < len(word):
        while i < size_l:
            if board[i, col] == word[j]:
                if size_l - (i + 1) >= len(word) - (j + 1):
                    return 1
                else:
                    continue
            else:
                i += 1
        i = 0
        j += 1
    return 0


def pick_row():
    temp_row = random.randint(0, size_l - 1)
    get_temp_row = board[temp_row, :]
    if check_row_availability(get_temp_row) == 1:
        return temp_row
    else:
        return pick_row()


def pick_col(word):
    temp_col = random.randint(0, size_w - 1)
    get_temp_col = board[:, temp_col]
    if advanced_col_availability_check(temp_col, word) == 1:
        return temp_col
    elif check_col_availability(get_temp_col) == 1:
        return temp_col
    else:
        return pick_col()


def row_spacer(word, length):
    if length >= size_w:
        return word
    elif length < size_w:
        n = random.randint(0, size_w - length)
        return n * " " + word


def insert_row(word, row):
    i = 0
    for letter in word:
        board[row, i] = letter
        i += 1


def insert_col(word, col):
    i = 0
    for letter in word:
        board[i, col] = letter
        i += 1


def fill_horizontal(num_of_words_h):
    i = num_of_words_h
    if i <= 0:
        print("No horizontal words filled.")
    else:
        while num_of_words_h > 0:
            temp_word_placeholder = get_word()
            temp_word = row_spacer(temp_word_placeholder, len(temp_word_placeholder))
            length_of_temp_word = len(temp_word)
            if length_of_temp_word > size_w:
                i -= 1
                print("Insertion of horizontal word : '{}' failed due to size limitations.".format(temp_word))
            else:
                temp_row = pick_row()
                insert_row(temp_word, temp_row)
                num_of_words_h -= 1
                print("Inserted horizontal word : '{}' successfully.".format(temp_word))


def fill_vertical(num_of_words_v):
    i = num_of_words_v
    if i <= 0:
        print("No vertical words filled.")
    else:
        while num_of_words_v > 0:
            temp_word = get_word()
            length_of_temp_word = len(temp_word)
            if length_of_temp_word > size_l:
                i -= 1
                print("Insertion of vertical word : '{}' failed due to size limitations.".format(temp_word))
            else:
                temp_col = pick_col(temp_word)
                insert_col(temp_word, temp_col)
                num_of_words_v -= 1
                print("Insertion of vertical word : '{}' successful.".format(temp_word))


def random_letter():
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                "V", "W", "X", "Y", "Z"]
    temp_random_letter = random.randint(0, len(alphabet) - 1)
    return alphabet[temp_random_letter]


def fill_board():
    i = 0
    j = 0
    while i < size_l:
        while j < size_w:
            if board[i, j] == "":
                board[i, j] = random_letter()
                j += 1
            else:
                j += 1
        i += 1
        j = 0


#create_game(10, 10, 5, 0)
#print("git_test")
