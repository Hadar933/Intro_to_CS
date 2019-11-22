import sys
import os.path


WORD_FILE_ERROR = 'unable to find words list'
MATRIX_FILE_ERROR = 'unable to find matrix file'
DIRECTION_ERROR = 'invalid direction'
LENGTH_ERROR = 'Invalid number of arguments'


def word_file_locator(args):
    """
    locates the word file
    :param args: all arguments from user
    :return: True if file exists
    """
    word_file_location = args[1] #location as received from user
    word_file_exists = os.path.isfile(word_file_location)
    if not word_file_exists:
        return False
    return True


def matrix_file_locator(args):
    """
    locates the file file
    :param args: all arguments from user
    :return: True if file exists
    """
    matrix_file_location = args[2] #location as received from user
    matrix_file_exists = os.path.isfile(matrix_file_location)
    if not matrix_file_exists:
        return False
    return True


def valid_direction(directions):
    """
    checks if given string of directions is valid
    :param directions: all options available
    :return: True if lists are valid
    """
    VALID_DIRECTIONS = ['u', 'd', 'r', 'l', 'w', 'x', 'y', 'z']
    for direction in directions:
        if direction not in VALID_DIRECTIONS:
            return False
    return True


def invalid_length(args):
    """
    checks the number of arguments
    :param args: as given by user
    :return: True if number of arguments is valid
    """
    if len(args) != 5:
        return False
    return True


def check_input_args(args):
    """
    check all previous functions altogether
    :param args: as given by user
    :return: None if all "tests" have passed
    """
    if invalid_length(args) is False:
        return LENGTH_ERROR
    if word_file_locator(args) is False:
        return WORD_FILE_ERROR
    if matrix_file_locator(args) is False:
        return MATRIX_FILE_ERROR
    if valid_direction(args[4]) is False:
        return DIRECTION_ERROR
    return None


def read_wordlist_file(filename):
    """
    reads the content of the word file
    :param filename: name of the word file
    :return: list of the words in the file
    """
    words_list = []
    with open(filename, 'r') as word_list:
        words = word_list.readlines()
        for word in words:
            word = word[:-1]
            words_list.append(word)
    return words_list


def read_matrix_file(filename):
    """
    reads the content of the matrix file
    :param filename: the matrix file name
    :return: list of lists portraying the matrix
    """
    matrix_list = []
    with open(filename, 'r') as mat_list:
        matrixes = mat_list.readlines()
        for matrix in matrixes:
            matrix = matrix[:-1] #deletes the string '/n'
            matrix_list.append(matrix.split(',')) #appends files with comma
    return matrix_list


def direction_u(word_list, matrix):
    """
    checks presence of words in the given direction
    :param word_list: words to search
    :param matrix: given matrix
    :return: list of the words that are in the matrix in the given direction
    """
    u_list = []
    for col in range(len(matrix[0])):
        for row in range(len(matrix)-1,-1,-1):
            for word in word_list:
                found_word = True
                match_len = 0 # making sure all letters are in the matrix
                for i in range(len(word)):
                    if row - i <0:
                        break
                    if word[i] != matrix[row-i][col]: #how I search
                        found_word=False
                        break
                    match_len += 1
                if (match_len == len(word)) and (found_word is True):
                    u_list.append(word)
    return u_list


def direction_d(word_list,matrix):
    """
    checks presence of words in the given direction
    :param word_list: words to search
    :param matrix: given matrix
    :return: list of the words that are in the matrix in the given direction
    """
    d_list = []
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            for word in word_list:
                match_len = 0
                found_word = True
                for i in range(len(word)):
                    if row + i > len(matrix)-1:
                        break
                    if word[i] != matrix[row+i][col]:
                        found_word=False
                        break
                    match_len += 1
                if (match_len == len(word)) and (found_word is True):
                    d_list.append(word)
    return d_list


def direction_r(word_list, matrix):
    """
    checks presence of words in the given direction
    :param word_list: words to search
    :param matrix: given matrix
    :return: list of the words that are in the matrix in the given direction
    """
    r_list = []
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            for word in word_list:
                match_len = 0
                found_word = True
                for i in range(len(word)):
                    if col + i > len(matrix[0])-1:
                        break
                    if word[i] != matrix[row][col+i]:
                        found_word=False
                        break
                    match_len += 1
                if (match_len == len(word)) and (found_word is True):
                    r_list.append(word)
    return r_list


def direction_l(word_list, matrix):
    """
    checks presence of words in the given direction
    :param word_list: words to search
    :param matrix: given matrix
    :return: list of the words that are in the matrix in the given direction
    """
    l_list = []
    for col in range(len(matrix[0])-1,-1,-1):
        for row in range(len(matrix)):
            for word in word_list:
                match_len = 0
                found_word = True
                for i in range(len(word)):
                    if col - i < 0:
                        break
                    if word[i] != matrix[row][col-i]:
                        found_word=False
                        break
                    match_len += 1
                if (match_len == len(word)) and (found_word is True):
                    l_list.append(word)
    return l_list


def direction_w(word_list, matrix):
    """
    checks presence of words in the given direction
    :param word_list: words to search
    :param matrix: given matrix
    :return: list of the words that are in the matrix in the given direction
    """
    w_list = []
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            for word in word_list:
                found_word = True
                match_len = 0
                for i in range(len(word)):
                    if col + i > len(matrix[0])-1 or\
                            row - i > (len(matrix)):
                        break
                    if word[i] != matrix[row-i][col+i]:
                        found_word=False
                        break
                    match_len += 1
                if (match_len == len(word)) and (found_word is True):
                    w_list.append(word)
    return w_list


def direction_x(word_list, matrix):
    """
    checks presence of words in the given direction
    :param word_list: words to search
    :param matrix: given matrix
    :return: list of the words that are in the matrix in the given direction
    """
    x_list = []
    for col in range(len(matrix[0])-1,-1,-1):
        for row in range(len(matrix)-1,-1,-1):
            for word in word_list:
                found_word = True
                match_len = 0
                for i in range(len(word)):
                    if col - i <0 or row - i <0:
                        break
                    if word[i] != matrix[row-i][col-i]:
                        found_word=False
                        break
                    match_len += 1
                if (match_len == len(word)) and (found_word is True):
                    x_list.append(word)
    return x_list


def direction_y(word_list,matrix):
    """
    checks presence of words in the given direction
    :param word_list: words to search
    :param matrix: given matrix
    :return: list of the words that are in the matrix in the given direction
    """
    y_list = []
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            for word in word_list:
                match_len = 0
                found_word = True
                for i in range(len(word)):
                    if row + i > len(matrix)-1 or\
                            col + i > len(matrix[0])-1:
                        break
                    if word[i] != matrix[row+i][col+i]:
                        found_word=False
                        break
                    match_len += 1
                if (match_len == len(word)) and (found_word is True):
                    y_list.append(word)
    return y_list


def direction_z(word_list,matrix):
    """
    checks presence of words in the given direction
    :param word_list: words to search
    :param matrix: given matrix
    :return: list of the words that are in the matrix in the given direction
    """
    z_list = []
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            for word in word_list:
                found_word = True
                match_len = 0
                for i in range(len(word)):
                    if row + i > len(matrix) - 1 or\
                            col - i > len(matrix[0])-1:
                        break
                    if word[i] != matrix[row + i][col-i]:
                        found_word=False
                        break
                    match_len += 1
                if (match_len == len(word)) and (found_word is True):
                    z_list.append(word)
    return z_list


def from_list_of_lists_to_list(list_of_list):
    """
    converts a list of lists to a single list of items
    :param list_of_list: list of lists
    :return: single list of items
    """
    lst = []
    for inner_list in list_of_list:
        for word in inner_list:
            lst.append(word)
    return lst


def list_to_tuple(lst):
    """
    converts a list to a tuple, using dictionary
    :param lst: given list
    :return: tuple
    """
    d = dict()
    tuple_list = []
    for element in lst:
        if element not in d:
            d[element] = 1
        else:
            d[element] += 1
    for word in d:
        tuple_list.append((word,d[word])) # this part converts the dict to
                                          # tuple
    return tuple_list


def find_words_in_matrix(word_list,matrix, directions):
    """
    main part of the search- calls functions to search in all directions.
    :param word_list: words to search
    :param matrix: given mattirx
    :param directions: all directions available
    :return: histogram of the words (in tuple format)
    """
    words_list = []
    if valid_direction(directions):
        direction_list = list(set(directions)) #deletes direction duplicates
        for direction in direction_list:
            if direction == 'u':
                words_list.append(direction_u(word_list, matrix))
            if direction == 'd':
                words_list.append(direction_d(word_list, matrix))
            if direction == 'r':
                words_list.append(direction_r(word_list,matrix))
            if direction == 'l':
                words_list.append(direction_l(word_list, matrix))
            if direction == 'w':
                words_list.append(direction_w(word_list, matrix))
            if direction == 'x':
                words_list.append(direction_x(word_list, matrix))
            if direction == 'y':
                words_list.append(direction_y(word_list, matrix))
            if direction == 'z':
                words_list.append(direction_z(word_list, matrix))

    all_words_list = from_list_of_lists_to_list(words_list)
    tuple_list = list_to_tuple(all_words_list)
    return tuple_list


def write_output_file(results,output_filename):
    """
    copies the tuple from the previous funcion to a new file in the needed
    format- list of words and their occurrences, seperated by comma
    :param results: tuple lists from the last func
    :param output_filename: name of the file that is being created
    :return:
    """
    with open(output_filename,'w') as output:
        for item in results:
            word = item[0]
            repetition = item[1]
            new_string =str(word) + ',' + str(repetition) #seperating strings
                                                           #with a comma
            output.write(new_string+'\n')  # adding new line as needed


def main():
    """
    calls the functions from before to run the game
    :return:
    """
    if check_input_args(sys.argv) is None:
        word_file = read_wordlist_file(sys.argv[1])
        mat_file = read_matrix_file(sys.argv[2])
        output_file = sys.argv[3]
        directions = sys.argv[4]
        results = find_words_in_matrix(word_file,mat_file,directions)
        write_output_file(results,output_file)
    else:
        print(check_input_args(sys.argv))
        exit()

if __name__ == "__main__":
    main()



