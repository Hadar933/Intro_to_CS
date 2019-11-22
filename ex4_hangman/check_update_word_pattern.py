from hangman import update_word_pattern


def update_word_pattern_checker():
    flag = True
    """
    the function checks the function update word pattern in 4 different
    edge situations.
    :return: if all tests are correct. True will return. If one or more of
    the tests fail, the function will return False.
    """
    if update_word_pattern('cooperate','c__p_rat_','o') != 'coop_rat_':
        flag = False
        print('test 1 has failed')
    if update_word_pattern('pattern','_______','t') != '__tt___':
        flag = False
        print('test 2 has failed')
    if update_word_pattern('coop'+'erate','c__p_rat_','o') != 'coop_rat_':
        flag = False
        print('test 3 has failed')
    if update_word_pattern('hangman','hangman','a') != 'hangman':
        flag = False
        print('test 4 has failed')
    else:
        print('Tests passed successfully!')
    return flag


if __name__ == "__main__":
    (update_word_pattern_checker())