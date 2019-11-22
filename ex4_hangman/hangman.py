from hangman_helper import *
import string
LETTERS = 26
ERROR_COUNT = 0


def lowcase_alphabet(letter):
    """
    checks if a string is a lowercase english letter
    :param letter: a given string
    :return: True if string is lowercase or False otherwise.
    """
    if letter in list(string.ascii_lowercase):
        return True
    return False


def update_word_pattern(word, pattern, letter):
    """
    Given a letter that is a part of the word, the function will switch the
    '_' string from the pattern with the letter mentioned. By doing so, a new
    pattern will return
    :param word: the word that the player needs to guess
    :param pattern: the word with blanked letters
    :param letter: a letter that the user had guessed
    :return: a new pattern, containing the letter(or not)
    """
    for i in range(len(word)):
        if word[i] == letter:
            pattern = pattern[:i] + letter + pattern[i + 1:]
    return pattern


def run_single_game(words_list):
    """
    This functions takes care of the entire run of a single hangman game.
    There are three main processes: the initialization, the gameplay and the
    ending. The continuity of the game relies mostly on the user's input and
    according to different inputs a different output will arise.
    :param words_list: given list of word from a file

    """
    # INITIALIZATION #
    word = get_random_word(words_list)
    wrong_guess_lst = []
    pattern = '_' * len(word)
    msg = DEFAULT_MSG
    error_count = ERROR_COUNT

    # GAME-PLAY #
    while pattern != word and error_count < MAX_ERRORS:
        display_state(pattern, error_count, wrong_guess_lst, msg)
        user_input = get_input()
        if user_input[0] == HINT:
            filtered_list = filter_words_list(words_list, pattern,
                                              wrong_guess_lst)
            frequent_letter = choose_letter(filtered_list, pattern)
            msg = HINT_MSG + frequent_letter
            continue
        if user_input[0] == LETTER:
            letter = user_input[1]
            if len(letter) != 1 or lowcase_alphabet(letter) != True:
                msg = NON_VALID_MSG
                continue
            elif letter in pattern or letter in wrong_guess_lst:
                msg = ALREADY_CHOSEN_MSG + letter
            elif letter in word:
                pattern = update_word_pattern(word, pattern, letter)
                msg = DEFAULT_MSG
            else:
                wrong_guess_lst.append(letter)
                error_count += 1
                msg = DEFAULT_MSG
        if user_input[0] == HINT:
            msg = NO_HINTS_MSG
    # ENDING #
    if word == pattern and error_count < MAX_ERRORS: # win
        display_state(pattern, error_count,
                      wrong_guess_lst, WIN_MSG, ask_play=True)
    else:
        display_state(pattern, error_count, # lose
                      wrong_guess_lst, LOSS_MSG + word, ask_play=True)


def main():
    """
    this functions is in charge of running the game, when the right input is
    provided. Furthermore, the function loads the words file.
    :return:
    """
    all_words = load_words(file='words.txt')
    run_single_game(all_words)
    while get_input() == (PLAY_AGAIN, True):
        run_single_game(all_words)


def letters_repetition(word,pattern):
    """
    this function helps filter_words_list
    checks for repetitive letters in a word
    :param word: any word
    :return: True if word has letters that repeats themselves. false
    otherwise
    """
    for i in range(len(word)):
        if word[i] in pattern:
            for j in range(i+1,len(word)):
                if word[i] == word[j]:
                    return True
    return False


def word_has_bad_letters(word,wrong_guess_lst):
    """
    checks if a letter from word is in the list wrong guess list
    :return: True if so, false otherwise
    """
    for letter in word:
        if letter in wrong_guess_lst:
            return True
    return False


def similar_to_pattern(word,pattern):
    """
    checks if the word is similar to to the pattern
    :return: True if so, false otherwise
    """
    flag = True
    for i in range(len(word)):
        if pattern[i] == '_':
            continue
        elif word[i] != pattern[i]:
            flag = False
    return flag


def filter_words_list(words,pattern,wrong_guess_lst):
    """
    using three helping functions, removes all words that:
    1.has different length than pattern
    2.has letters that are in wrong guess lst
    3.aren't similar to pattern
    :return: new list with the suitable words
    """
    new_lst = words[:]
    for word in words:
        if letters_repetition(word,pattern) or len(word) != len(pattern) or\
            word_has_bad_letters(word,wrong_guess_lst)\
                or not similar_to_pattern(word,pattern):
            new_lst.remove(word)
    return new_lst


def maximum_value(lst):
    """
    a helping function to choose_letter. determines the biggest value in a
    list of numbers.
    :param lst: given list
    :return: maximun value number from the list
    """
    maxima = 0
    for num in lst:
        if num > maxima:
            maxima = num
    return maxima


CHAR_A = 97
def letter_to_index(letter):
    """
    Return the index of the given letter in an alphabet list.
    """
    return ord(letter.lower()) - CHAR_A


def choose_letter(words,pattern):
    """
    from a list of words, and according to a pattern formation,
    the functions shows which letter shows up the most.
    :param words: list of given words
    :param pattern: pattern from the gamee
    :return: most frequent letter in the list of words
    """
    lowcase_ab = list('abcdefghijklmnopqrstuvwxyz')
    letters_histlist = [0] * LETTERS
    for word in words:
        for letter in word:
            if letter in pattern:
                continue
            letters_histlist[letter_to_index(letter)]+=1
    max_occurrences = max(letters_histlist)
    common_letter = lowcase_ab[letters_histlist.index(max_occurrences)]
    return common_letter

if __name__ == "__main__":
     main()

