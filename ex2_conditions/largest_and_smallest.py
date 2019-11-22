def largest_and_smallest(n1,n2,n3):
    """
    finds the largest and smallest numbers amongst three
    :param n1: first number
    :param n2: second number
    :param n3: third number
    :return: maximum,minimum (in that order)
    """
    if n1 >= n2 and n1 >= n3:
        maxi = n1
    elif n2 >= n1 and n2 >= n3:
        maxi = n2
    else:
        maxi = n3
    if n1 <= n2 and n1 <= n3:
        mini = n1
    elif n2 <= n1 and n2 <= n3:
        mini = n2
    else:
        mini = n3
    return maxi,mini

print(largest_and_smallest(0,0,0))