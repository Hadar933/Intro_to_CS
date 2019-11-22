def is_it_stable(threshold,p1,p2,p3):
    """
    checks if the difference from each item is lesser then the threshold
    :param threshold: states if item is stable according to prices
    :param p1: price in year 1
    :param p2: price in year 2
    :param p3: price in year 3
    :return: True if stable, false otherwise
    """
    if abs(p1-p2)>threshold or abs(p2-p3)>threshold or abs(p1-p3)>threshold:
        return False
    return True

