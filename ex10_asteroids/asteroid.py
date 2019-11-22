import math

class Asteroid:
    def __init__(self,x_pos,y_pos,x_vel,y_vel,size):
        """
        constructor for asteroid object
        :param x_pos: position on x axis
        :param y_pos: position on y axis
        :param x_vel: velocity in direction of x axis
        :param y_vel: velocity in direction of y axis
        :param size: size of the ship (1, 2 or 3)
        """
        self.__x_pos = x_pos
        self.__y_pos = y_pos
        self.__x_vel = x_vel
        self.__y_vel = y_vel
        self.__size = size

    """
    the following functions are setters and getters for the init arguments:
    x and y position, x and y velocity and size
    """

    def get_x_pos(self):
        return self.__x_pos

    def get_y_pos(self):
        return self.__y_pos

    def get_x_vel(self):
        return self.__x_vel

    def get_y_vel(self):
        return self.__y_vel

    def get_size(self):
        return self.__size

    def set_x_pos(self,x_pos):
        self.__x_pos = x_pos

    def set_y_pos(self,y_pos):
        self.__y_pos = y_pos

    def set_x_vel(self,x_vel):
        self.__x_vel = x_vel

    def set_y_vel(self,y_vel):
        self.__y_vel = y_vel

    def set_size(self,new_size):
        self.__size = new_size

    def get_radius(self):
        radius = 10 * self.get_size() - 5
        return radius

    def has_intersection(self,obj):
        """
        this function determines if a collision between the asteroid and
        an object (ship or torpedo) has happened.
        :param obj: ship or torpedo objects
        :return: True if so, false otherwise.
        """
        x_dist = (obj.get_x_pos()-self.get_x_pos())**2
        y_dist = (obj.get_y_pos()-self.get_y_pos())**2
        distance = math.sqrt(x_dist + y_dist)
        if distance <= self.get_radius() + obj.get_radius():
            return True
        else:
            return False

