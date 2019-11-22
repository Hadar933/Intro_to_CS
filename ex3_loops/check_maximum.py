from ex3 import maximum

def test():
    """
    the function tests four different inputs to the maximum function.
    :return: 4 times 'test 1 is A-OK' prints
    """
    if maximum([0]) == 0:
        print('Test 1 is A-OK')
    else:
        print('Test 1 Failed')
    if maximum([]) is None:
        print('Test 1 is A-OK')
    else:
        print('Test 1 Failed')
    if maximum([1,1,1]) == 1:
        print('Test 1 is A-OK')
    else:
        print('Test 1 Failed')
    if maximum([0,0,0]) == 0:
        print('Test 1 is A-OK')
    else:
        print('Test 1 Failed')

if __name__ == '__main__':
    test()