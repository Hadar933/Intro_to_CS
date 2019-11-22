def calculate_mathematical_expression(n1,n2,op):
    """
    calculates basic mathematical expressions according
    to user input
    :param n1: number 1
    :param n2: number 2
    :param op: type of operation (+,-,*,/)
    :return: result
    """
    if op == '+':
        return n1+n2
    elif op == '-':
        return n1-n2
    elif op == '*':
        return n1*n2
    elif op == '/':
        if n2 == 0: # withdraws before exception
            return
        else:
            return n1/n2
    return


def calculate_from_string(exp):
    """
    converts a string expression to a mathematical expression
    and calculates it using the previous function
    :param exp: mathematical operation as string in format: (num1 op num2)
    :return: result of the expression
    """
    n1, op, n2 = exp.split(' ')
    return calculate_mathematical_expression(float(n1),float(n2),op)



