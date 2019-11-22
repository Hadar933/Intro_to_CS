import largest_and_smallest as las


def tester():
    """
    tester for function 4 - largest_and_smallest
    :return: true is all tests have passed. false otherwise
    """
    flag = True
    if las.largest_and_smallest(-1, -2, -3) != (-1, -3):
        print('test 1 failed')
        flag = False
    if las.largest_and_smallest(0, 0, 0) != (0, 0):
        print('test 2 failed')
        flag = False
    if las.largest_and_smallest(0.5, -1.7, 0) != (0.5, -1.7):
        print('test 3 failed')
        flag = False
    if las.largest_and_smallest(1/2, 1/4, 1/5) != (0.5, 0.2):
        print('test 4 failed')
        flag = False
    if las.largest_and_smallest(-1/2, -2/4, -1/5) != (-0.2, -0.5):
        print('test 5 failed')
        flag = False
    return flag


if __name__== 'main':
    tester()
