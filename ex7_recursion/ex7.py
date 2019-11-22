def print_to_n(n):
    """
    executes the recursive, then printing the result - providing print
    of numbers in ascending order
    :param n: any whole number
    """
    if n<1:
        pass
    else:
        print_to_n(n-1)
        print(n)


def print_reversed(n):
    """
     executes the print, then applying the recursive function -
     providing print of numbers in descending order
     :param n: any whole number
     """
    if n<1:
        pass
    else:
        print(n)
        print_reversed(n-1)


def has_divisor_smaller_than(n, i=3):
    """
    checks for prime by using i which might or might not divide n
    :return: True if prime, false otherwise
    """
    if n == 2:
        prime = True
    elif n <= 1 or n % 2 == 0: # even, or equal or smaller than 1
        prime = False
    elif i * i > n: # doesnt divide by any number up until square root
        prime = True
    elif (n % i) == 0: # divides by i - obviously not prime
        prime = False
    else:
        prime = has_divisor_smaller_than(n, i+2)
    return prime


def is_prime(n):
    """
    determining whether a number is prime
    """
    return has_divisor_smaller_than(n,3)


def factorial(n):
    """
    returns factorial of given whole number n
    :param n: number
    :return: n!
    """
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def something(n):
    if n >1:
        n*=n-1
    else:
        print(n)
        something(n-1)
something(4)

def exp_n_x(n,x):
    """
    exponential sum
    return: sum of all numbers from 0 to n that are equal to
    (x^i/i!)
    """
    if n == 0:
        return 1
    else:
        value = x**n / factorial(n)
        return value + exp_n_x(n-1,x)


def play_hanoi(hanoi,n,src,dest,temp):
    """
    by using two recursive calls, the function solves the play hanoi game
    :param hanoi: game call
    :param n: number of rings
    :param src: source peg
    :param dest: destination peg
    :param temp: temporary peg
    """
    if n == 1: # only 1 ring
        hanoi.move(src,dest)
        return
    if n > 1: #more than 1 ring
        play_hanoi(hanoi,n-1,src,temp,dest) #moves n-1 rings to temp using
                                            #dest
        hanoi.move(src,dest) #moves n'th ring to dest
        play_hanoi(hanoi,n-1,temp,dest,src) #move n-1 rings to dest using src


def repetitive_sequences(char_list, n, string):
    """
    creating all possible sequences of  length n from
    given list of letters,  with repetition.
    :param char_list: list of letters
    :param n: length of a possible repetition
    :param string: iterable  string
    """
    if n == 0:
        return None
    if len(string) == n: #prints every string that has reached length n
        print(string)
        return
    else:
        temp = string #sets a temporary value which changes according to
        #the value of the string
        for char in char_list:
            string = temp + char #adds the char to the temporary string
            repetitive_sequences(char_list, n, string) #repeats


def print_sequences(char_list,n):
    """
    using the previous func, this func will return all permutations of
    lettes in a char list with repetitions.
    :param char_list: list of letters
    :param n: length of wanted string
    """
    string = ''
    repetitive_sequences(char_list,n,string)


def non_repetitive_sequences(char_list, n, string):
    """
     creating all possible sequences of  length n from
     given list of letters,  without repetitions.
     :param char_list: list of letters
     :param n: length of a possible repetition
     :param string: iterable  string
     """
    if n == 0:
        return None
    if len(string) == n:
        print(string)
        return
    else:
        temp = string
        for char in char_list:
            if char not in string: #only actual difference between
                #the fucntions - changes the string only if the char
                #isnt already in the string.
                string = temp + char
                non_repetitive_sequences(char_list, n, string)


def print_no_repetition_sequences(char_list,n):
    """
    using the previous func, this func will return all permutations of
    lettes in a char list without repetitions.
    :param char_list: list of letters
    :param n: length of wanted string
    """
    string = ''
    non_repetitive_sequences(char_list,n,string)


def parentheses(n):
    """
    generates all possible couples of parentheses given n options.
    :param n: whole positive integer
    :return: list of all possible parentheses
    """
    par_set = {}
    if n == 0: #base case
        return {''}
    elif n in par_set:
        return par_set[n] #makes sure no repetitions occur
    else:
        par = set('(' + p + ')' for p in parentheses(n-1)) #creating a set
        # that contains the strings '(' and ')' according to p
        for k in range(1,n):
            par.update(p+q for p in parentheses(k) for q in parentheses(n-k))
            #updating the par set according to values of q and p which
            #represent the parentheses
        par_set[n] = par
        return list(par)


def list_of_directions(n,k):
    """
    creates a list of 'r's and 'u's according to the numbers n and k
    :param n: number
    :param k: number
    :return: list of directions
    """
    list_of_directions = []
    for i in range(n):
        # for every index, appends r
        list_of_directions.append('r')
    for j in range(k):
        # for every index, appends u
        list_of_directions.append('u')
    return list_of_directions


def permute(array):
    """
    generates all permutations of an array without repetition. takes into
    account an array that might has repetition of letters
    :param array: list of letters
    :return: list of permutations
    """
    if len(array) == 1:
        return [array]
    result = []
    for permutation in permute(array[1:]): #recursive call for the first
        #letter
        for i in range(len(array)):
            #appending all possibilities - permutation from zero to i,
            # array from 0 to one and permutation from i to the end
            result.append(permutation[:i] + array[0:1] + permutation[i:])
    return result


def up_and_right(n,k):
    """
    converts an array of permutations to string of all possible directions
    according to given numbers n and k. permutations are based on a list
    of directions as described before.
    """
    final_list = []
    lst_of_directions = list_of_directions(n,k)
    lst_of_permutes = permute(lst_of_directions)
    for item in lst_of_permutes:
        str = ''.join(item) #converts all items to a string
        final_list.append(str) #appends the strings to the final result
    final_list_as_set = set(final_list)
    for item in final_list_as_set:
        print(item)


def flood_fill(image,start):
    """
    according to a start position, the function will create a somewhat flood
    fill, converting dots to asterisks that are in the surrounding ot the dot
    :param image: matrix of dots and asterisks
    :param start: tuple that represents the start position
    :return: new changed image
    """
    row = start[0]
    col = start[1]
    new_image = flood_fill_helper(image,row,col)
    return new_image


def flood_fill_helper(image,row,col):
    """
    using 4 recursive calls, checks for dots in a matrix to convert
    into asterisks.
    :param image: 2d matrix
    :param row: place in matrix's row
    :param col: place in matrix's column
    :return: new image
    """
    if image[row][col] == '*': # base case 1
        return image
    if image[row][col] == '.': #base case 2
        image[row][col] = '*'
        flood_fill_helper(image,row+1,col) #down
        flood_fill_helper(image, row - 1, col)  #up
        flood_fill_helper(image, row , col+1)  # right
        flood_fill_helper(image, row , col-1)  # left
    return image

# ###########################################################################
# #                           second try                                    #
# ###########################################################################
#

#
# def print_to_n(n):
#     if n < 1:
#         return
#     else:
#         print_to_n(n-1)
#         print(n)
#
#
# def print_reversed(n):
#     if n < 1:
#         return
#     else:
#         print(n)
#         print_reversed(n-1)
#
#
# def is_prime(n):
#     return prime_helper(n,3)
#
#
# def prime_helper(n, i):
#     if n == 2 or n == 3:
#         return True
#     if n % i == 0 or n <= 1 or n % 2 == 0:
#         return False
#     elif i*i > n:
#         return True
#     else:
#         return prime_helper(n,i+2)
# # new_lst = [i for i in range(1000000) if is_prime(i) is True]
# # print(new_lst)
#
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n*factorial(n-1)
#
#
# def exp_n_x(n,x):
#     if n == 0:
#         return 1
#     else:
#         return x**n/factorial(n) + exp_n_x(n-1,x)
#
#
# def play_hanoi(hanoi,n,src,dest,temp):
#     if n == 1:
#         hanoi.move(src,dest)
#     elif n > 1:
#         play_hanoi(hanoi,n-1,src,temp,dest)
#         hanoi.move(src,dest)
#         play_hanoi(hanoi,n-1,temp,dest,src)
#
#
# def print_sequence(char_list,n,string):
#     if len(string) == n:
#         print(string)
#         return
#     if n == 0:
#         return
#     else:
#         val = string
#         for char in char_list:
#             string = val + char
#             print_sequence(char_list,n,string)
#
#
# def print_no_repetition(char_list,n,string):
#     if len(string) == n:
#         print(string)
#         return
#     if n == 0:
#         return
#     else:
#         val = string
#         for char in char_list:
#             if char not in val:
#                 string = val + char
#                 print_no_repetition(char_list,n,string)
#
# def parentheses(n):
#     parentheses_helper(n,0,0,'')
#
# def parentheses_helper(n,left,right,s):
#     if right == n:
#         print(s)
#         return
#     if left < n:
#         parentheses_helper(n,left+1,right,s+'(')
#     if right < left:
#         parentheses_helper(n,left,right+1,s+')')
#
def func(lst,n,h=""):
    if n == 0:
        print(h)
    else:
        for i in range(len(lst)):
            new = lst[:i]+lst[i+1:]
            func(new,n-1,h+lst[i])

func(['a','b','c'],1)