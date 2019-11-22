

def input_list():
    """
the function requests an input from the user and then enters a loop
in which another input is requested.The loop will keep on going
for whenever a non-None value will be assigned. the loop will eventually
append the given input to an empty list.
    :return:a list containing all inputs assigned from the first input
    to the one before the empty input.
    """
    user_input = input()
    list1 = []                  #an empty list
    while user_input != "":     #loop will run only if an input is given
        list1.append(user_input) #appends the input to the list
        user_input = input()    #requests another input
    return(list1)               #list with all given values return.

def concat_list(str_list):
    """
    the function adds any component within the str_list
    to a new (and empty) string by performing a loop
    :param str_list:
    :return: new string containing each component separated with space
    """
    new_string = ''                  #this empty string will fill up with
                                     # strings
    for component in str_list:
        new_string += component + ' '#a new component is added to
                                     #the string every time.
    return(new_string[:-1])          #deletes the space at the end

def maximum(num_list):
    """
    the functions goes through a list and compares each number
    with the one preceding it, starting with 0. if a number is bigger than
    the previous number, it will be assigned as the new number that numbers
    will be compared to. in such manner the biggest number in the list
    will not be replaced by any other number in the list
    :param num_list: list of numbers bigger or equal to 0
    :return: function returns the maximum number OR None
    """
    if num_list == []:        #returns none when list remains empty
        return None
    max_val_num = 0           #sets a benchmark value (as described in
                              #question)
    for num in num_list:
        if num > max_val_num: #compare which is bigger
            max_val_num = num #assign the bigger number to the benchmark
    return max_val_num        #returns biggest number

def cyclic(lst1, lst2):
    """
    by checking the indexes of all items in a given list, the function will
    declare if a list is a cyclic permutation of a different list. The method
    being used compares numbers of index i to numbers of index (i+m)%k,
    whereas k is represented as the length of lst1 (len(lst1)).
    :param lst1: list with numbers
    :param lst2: list with same amount of numbers as lst1
    :return: True for when a lst1 is a cyclic permutation of lst2. False for
             when lst1 isn't a cyclic permutation of lst2
    """
    if len(lst1) != len(lst2):                      #program runs for list
                                                    #with the same amount of
                                                    #items.
        return False
    for m in range(len(lst1)):
        wanted_outcome = True                       #assuming the list is,
                                                    # infact, a cyclic
                                                    #permutation
        for i in range(len(lst1)):
            if lst1[i] != lst2[(i+m) % len(lst1)]: #comparing items that
                                                   #should be identical if
                                                   #the lists are cyclic
                                                   #permutation of one another

                wanted_outcome = False             #condition changes the
                                                   #wanted outcome

                break                              #breaks out of loop

        if wanted_outcome:                         #True of False is decided
                                                   #according to boolean
                                                   #value of wanted_outcome
            return wanted_outcome
        else:
            return False

def seven_boom(n):
    """
    If a number is divisible by 7 or/and if a number has '7' in it,
    it will be added to list_boom as 'boom'. otherwise, it will be added
    as itself.
    :param n: specifies the size of the list
    :return: a list of strings containing numbers and 'boom's
    """
    list_boom = []           #numbers will be inserted to this list
    for num in range(1, n+1): # I want the range to be from 1 to n, and not
                              # from 0 to n-1 for example
        if '7' in str(num):   #checks if the string '7'is in the str 'num'
            list_boom.append('boom')
        elif (num) % 7 == 0:  #checks if num is divisible by 7
            list_boom.append('boom')
        else:                 #if num doesnt have 7 in in or if num isnt
                              #divisible by 7, num itself will be added to
                              #list_boom
            list_boom.append(str(num))
    return list_boom

def histogram(n, num_list):
    """
    the functions goes through num_list, and whenever a 'new' number shows
    up, the number with the same index in hist_list grows by 1. That way,
    the hist_list acts as a some-what counter for numbers shown on num_list.
    eventually, hist_list is a histogram of num_list with n items.
    :param n: the number of items in hist_list
    :param num_list: a list from which numbers are withdrawn.
    :return: hist_list - a histogram of num_list with n items.
    """
    hist_list = [0]*n # starts as a list of 0s (n zeros)
    for num in num_list:
        hist_list[num] += 1 #whenever a number shows up, +1 is added to a
                            #number in hist_list according to the index.
    return hist_list

def prime_factors(n):
    """by using division operators, the function finds all prime factors
    of number n
    :param n: any number bigger than or equal to zero
    :return: list of prime numbers that make up n
    """
    i = 2 #sets a benchmark
    factors = []
    while i * i <= n: #because the number's smallest
        #prime factor will always be smaller than the number's square root.
        if n % i: #if i doesnt divide n
            i += 1 #adding 1 to i and starting again
        else:
            n = n//i #n is the remainer from the dividion n/i
            factors.append(i) #adds the remainer
    factors.append(n) #adds the number itself
    return factors

max1 = 0
for i in range(10000000):
    p = len(prime_factors(i))
    if (p > max1):
        max1 = p


def cartesian(lst1, lst2):
    """
    the function creates new lists containing each component from two
    given lists (lst1 and lst2) in a manner similar to cartesian product.
    :param lst1: list of values (int,str,float,etc..)
    :param lst2: list of values(int,str,float,etc..)
    :return: cartesian product of lst1 and lst2
    """
    list3 = []
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            list3.append([lst1[i],lst2[j]]) #add in a loop each component
            #within lst1 to each component in lst2
    return list3


def pairs(num_list, n):
    """
    the function goes through a list with two loops. the first loop checks
    a number from the list, and then the second loop compares that number
    with the numbers that FOLLOWS it. by doing that the function will not
    print pairs that are the same (for ex. (3,4) and (4,3)
    :param num_list: given list
    :param n: number to which sums from num_list should add up to
    :return: list1 - containing only non-repetitive pairs
    """
    list1 = []
    for i in range(len(num_list)): #any number in num_list
        for j in range(i, len(num_list)): # number that follows i
            if num_list[i] + num_list[j] == n: #checks if sum adds up to n
                list1.append([num_list[i], num_list[j]]) #adds to list1
    return list1


print(cyclic([1,2],[1,2]))