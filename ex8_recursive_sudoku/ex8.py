# SUDOKU #
def find_vacant(board,lst):
    """
    finding zeros in the sudoku
    :param board: given sudoku board
    :param lst: stores the row and col values of the spot containing zero
    :return: True if there are zeros, False otherwise (sudoku is complete)
    """
    for row in range(len(board[0])):
        for col in range(len(board)):
            if board[row][col] == 0:
                lst[0] = row
                lst[1] = col
                return True
    return False


def in_row(board,row,num):
    """
    checks if a number shows up in a certain row
    :return: True if number shows up. False otherwise
    """
    for col in range(len(board)):
        if board[row][col] == num:
            return True
    return False


def in_col(board,col,num):
    """
    checks if a number shows up in a certain column
    :return: True if number shows up. False otherwise
    """
    for row in range(len(board)):
        if board[row][col] == num:
            return True
    return False


def in_zone(board,row,col,num):
    """
    checks if a number shows up in a certain zone sqrt(n)*sqrt(n)
    :return: True if number shows up. False otherwise
    """
    for i in range(int(len(board)**0.5)): # using sqrt to limit the zone
        for j in range(int(len(board)**0.5)):
            if board[i+row][j+col] == num:
                return True
    return False


def safe_location(board,row,col,num):
    """
    checks if a num can be assigned to a specific spot in the sudoku
    :return: True if assignment is plausible, False otherwise
    """
    sqrt = int((len(board))**(0.5))
    if not in_row(board,row,num) and not in_col(board,col,num) \
            and not in_zone(board,row - row%sqrt,col - col%sqrt,num):
        # using modulo in order to make sure indexes stays inside the zone
        return True
    return False


def solve_sudoku(board):
    """
    main function that uses all previous functions in order to solve the
    puzzle
    :return: True if the sudoku can be solved(and has been).False otherwise
    """
    lst = [0,0] #lst of indexes is assigned first as 0's
    if find_vacant(board,lst) is False:
        return True # meaning that the sudoku is complete
    row = lst[0]
    col = lst[1]
    for num in range(1,len(board)+1):
        if safe_location(board,row,col,num) is True:
            board[row][col] = num # If it is safe to assign, the boards
            # is being given the new number.
            if solve_sudoku(board): # Recursive call
                return True
            board[row][col] = 0 # returning to base if the number has turned
            # out to provide a wrong outcome
    return False

# End Sudoku #
solve_sudoku([
        [0, 0, 9, 0, 2, 0, 0, 3, 6],
        [0, 8, 5, 0, 0, 0, 0, 1, 7],
        [0, 0, 0, 0, 5, 7, 2, 0, 4],
        [5, 0, 0, 0, 0, 2, 0, 6, 0],
        [0, 6, 4, 3, 0, 8, 1, 2, 0],
        [0, 7, 0, 1, 0, 0, 0, 0, 9],
        [3, 0, 1, 7, 8, 0, 0, 0, 0],
        [4, 9, 0, 0, 0, 0, 8, 5, 0],
        [6, 2, 0, 0, 3, 0, 4, 0, 0]
    ])

# Print K subsets #

def print_k_subsets(n,k):
    """
    printing all subsets of n that has length of k
    :param n: represents the group of numbers
    :param k: length of a subset from n
    :return: prints the subsets
    """
    if n == 0 or k == 0:
        return None
    if k <= n:
        cur_set = [False]*n #creating a set with n items that are False
        k_subset_helper(cur_set,k,0,0)


def print_set(cur_set):
    """
    this function is responsible for the printing of the subsets
    :param cur_set: list containing True of False items
    :return: prints a subset
    """
    lst_of_values = []
    for (idx,in_cur_set) in enumerate(cur_set): #each value receives an idx
        if in_cur_set: #if in cur set is true then its index is added to lst
            lst_of_values.append(idx)
    print(lst_of_values)


def k_subset_helper(cur_set,k,index,picked):
    """
    function that is responsible for the recursive calls
    :param cur_set: a subset
    :param k: length of subset
    :param index: specific index on the subset
    :param picked: value that is being used as picked = 0 in order to
    run on all subsets
    :return:
    """
    if k == picked: #sub set has the needed length
        print_set(cur_set)
        return
    if index == len(cur_set):
        return
    cur_set[index] = True #recursive calls that goes over all options of
                          # cur_set[idx]
    k_subset_helper(cur_set,k,index+1,picked+1)
    cur_set[index] = False
    k_subset_helper(cur_set,k,index+1,picked)

# End print K subsets #




# Fill K subsets #

def fill_k_subsets(n,k,lst):
    """
    similar to the previous function, but instead of printing all subsets,
    the subsets are being added to a lst
    :param n: represents the group of numbers
    :param k: length of a subset from n
    :param lst: lst to which the subsets are being appended
    """
    if n == 0 or k == 0:
        return None
    if k <= n:
        cur_set = [False]*n
        fill_k_subsets_helper(cur_set,k,0,0,lst)


def fill_k_return_set(cur_set):
    """
    converts the cur_list items from boolean to numbers and returns the
    new lst that has been created
    :param cur_set: lst with boolean values
    :return: lst of new values
    """
    lst_of_values = []
    for (idx,in_cur_set) in enumerate(cur_set):
        if in_cur_set:
            lst_of_values.append(idx)
    return lst_of_values


def fill_k_subsets_helper(cur_set,k,index,picked,lst):
    """
    this function is responsible for the recursive calls
    and has the same principle as the previous one
    """
    if k == picked:
        value = fill_k_return_set(cur_set)
        lst.append(value)
        return
    if index == len(cur_set):
        return
    cur_set[index] = True
    fill_k_subsets_helper(cur_set,k,index+1,picked+1,lst)
    cur_set[index] = False
    fill_k_subsets_helper(cur_set,k,index+1,picked,lst)

# fill k subsets end #


# return K subsets #

def return_k_subsets(n,k):
    """
    this function returns the same value as the previous function but
    without having any argument that is a list in it. Has similar
    principles as the previous functions
    """
    if n == 0 or k == 0:
        return None
    if k <= n:
        cur_set = [False]*n
        return_k_subsets_helper(cur_set,k,0,0)
        global_lst_copy = global_lst[:]
        global_lst[:] = []
        return global_lst_copy


def return_k_set(cur_set):
    """
    this function is responsible of creating all the cur_sets and convert
    them from boolean values to numbers
    :param cur_set: sub list composed of truths and false
    :return: lst of new values
    """
    lst_of_values = []
    for (idx,in_cur_set) in enumerate(cur_set):
        if in_cur_set:
            lst_of_values.append(idx)
    return lst_of_values


global_lst = []


def return_k_subsets_helper(cur_set,k,index,picked):
    """
    this function is responsible on adding the values to a list
    using recursive calls
    """
    if k == picked:
        value = return_k_set(cur_set)
        global_lst.append(value)
        return
    if index == len(cur_set):
        return
    cur_set[index] = True
    return_k_subsets_helper(cur_set,k,index+1,picked+1)
    cur_set[index] = False
    return_k_subsets_helper(cur_set,k,index+1,picked)


