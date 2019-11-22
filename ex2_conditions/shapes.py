import math


def shape_area():
    """
    calculates a chosen area
    :return: area of a circle/rectangle/triangle
    """
    num = float(input('Choose shape (1=circle, 2=rectangle, 3=triangle): '))
    if num == 1:
        return circle()
    if num == 2:
        return rectangle()
    if num == 3:
        return triangle()
    return


def circle():
    """
    calculates area of a circle
    """
    r = input()
    return math.pi*(float(r)**2)


def rectangle():
    """
        calculates area of a rectangle
        """
    a = input()
    b = input()
    return float(a)*float(b)


def triangle():
    """
        calculates area of a triangle
        """
    a = input()
    return (math.sqrt(3)/4)*(float(a)**2)

