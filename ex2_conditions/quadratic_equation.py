import math


def quadratic_equation(a,b,c):
    """
    solves the quadratic equation
    :param a: coefficient of x^2
    :param b: coefficient of x
    :param c: real number
    :return: solution/s to the equation
    """
    delta = (b**2-4*a*c)
    if delta<0:
        return None,None
    x1,x2 = (-b+math.sqrt(delta))/(2*a),(-b-math.sqrt(delta))/(2*a)
    if x1: # there is a solution for x1
        if x1 == x2 or not x2:
            return x1, None
        return x1,x2
    if not x1: # there isn't a solution for x1
        if not x2:
            return None, None
        if x2:
            return None, x2


def quadratic_equation_user_input():
    """
    solves the quadratic equation according to a user's input
    :return: printed solution
    """
    a,b,c = input("Insert coefficients a, b, and c: ").split(' ')
    x1,x2 = quadratic_equation(float(a),float(b),float(c))
    if x1 and x2:
        print('The equation has 2 solutions:',x1,'and',x2)
    elif x1 and not x2:
        print('The equation has 1 solution:',x1)
    elif x2 and not x1:
        print('The equation has 1 solution:', x2)
    else:
        print('The equation has no solutions')

