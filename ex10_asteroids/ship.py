
class Ship:
    def __init__(self,x_pos,y_pos,x_vel,y_vel,direction):
        """
        constructor for ship object
        :param x_pos_vel: position and veocity on x axis
        :param y_pos_vel: position and velocity on y axis
        :param direction: direction of the ship in radians
        """
        self.__x_pos = x_pos
        self.__y_pos = y_pos
        self.__x_vel = x_vel
        self.__y_vel = y_vel
        self.__direction = direction

    """
    the following functions are setters and getters for the init arguments:
    x and y position, x and y velocity and direction
    """

    def get_x_pos(self):
        return self.__x_pos

    def get_y_pos(self):
        return self.__y_pos

    def get_x_vel(self):
        return self.__x_vel

    def get_y_vel(self):
        return self.__y_vel

    def get_direction(self):
        return self.__direction

    def set_x_pos(self,x_pos):
        self.__x_pos = x_pos

    def set_y_pos(self,y_pos):
        self.__y_pos = y_pos

    def set_x_vel(self,x_vel):
        self.__x_vel = x_vel

    def set_y_vel(self,y_vel):
        self.__y_vel = y_vel

    def set_direction(self,new_dir):
        self.__direction = new_dir

    def get_radius(self):
        return 1




