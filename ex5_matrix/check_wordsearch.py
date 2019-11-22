from wordsearch import list_to_tuple

def list_to_tuple_checker():
    """
    check the function list_to_tuple by going over its items and sub items
    :return: True if all tests pass. False otherwise
    """
    flag = True
    lst = ['dog','cat','Cat','DOG','dog']
    histogram_tuple = list_to_tuple(lst)
    print(histogram_tuple)
    if histogram_tuple[0][0] != ('dog'):
        flag = False
    if histogram_tuple[0] != ('dog',2):
        flag = False
    if histogram_tuple[0] == histogram_tuple[3]:
        flag = False
    if histogram_tuple[0][1] == histogram_tuple[1][1]:
        flag = False
    return flag

if __name__ == "__main__":
    list_to_tuple_checker()