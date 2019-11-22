HORIZONTAL = 1
VERTICAL = 0


class Car:

    """
    this class is responsible for the car creation. It creates the car
    coordinates, provides the possible moves, the movement requirement
    and performs a move if possible
    """

    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's color
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col)
         location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        self.__name = name
        self.__length = length
        self.__location = location
        self.__orientation = orientation

    def get_name(self):
        """
        :return: The name of the car.
        """
        return self.__name

    def get_orientation(self):
        return self.__orientation

    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        coord_list = [self.__location]
        if self.__orientation == 0: # vertical
            for i in range(self.__length-1):
                new_coord = (self.__location[0]+i+1, self.__location[1])
                coord_list.append(new_coord)
        elif self.__orientation == 1:  # horizontal
            for i in range(self.__length-1):
                new_coord = (self.__location[0],self.__location[1]+i+1)
                coord_list.append(new_coord)
        return coord_list

    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements
         permitted by this car.
        """
        if self.__orientation == HORIZONTAL:
            hor_dic = {'l': 'causes the car to go left',
                       'r': 'causes the car to go right'}
            return hor_dic
        elif self.__orientation == VERTICAL:
            ver_dic = {'u': 'causes the car to go up',
                       'd': 'causes the car to go down'}
            return ver_dic

    def movement_requirements(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for
        this move to be legal.
        """
        empty_req_cell = []
        coord_list = self.car_coordinates()
        last_cell = coord_list[-1]
        first_cell = coord_list[0]
        if self.__orientation == HORIZONTAL:
            if movekey == 'r':
                empty_req_cell = [(last_cell[0],last_cell[1]+1)]
            elif movekey == 'l':
                empty_req_cell = [(first_cell[0],first_cell[1]-1)]
        elif self.__orientation == VERTICAL:
            if movekey == 'u':
                empty_req_cell = [(first_cell[0]-1,first_cell[1])]
            elif movekey == 'd':
                empty_req_cell = [(last_cell[0]+1,last_cell[1])]
        return empty_req_cell

    def move(self, movekey):
        """
        moves the car
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        car_coord = self.car_coordinates()
        relevant_cell = self.movement_requirements(movekey)
        if relevant_cell == []:
            return False
        else:
            avail_cell = relevant_cell[0]
        if movekey == 'r' or movekey == 'd':
            del car_coord[0]
            car_coord.append(avail_cell)
            self.__location = car_coord[0]
            return True
        elif movekey == 'u' or movekey == 'l':
            del car_coord[-1]
            car_coord.insert(0,avail_cell)
            self.__location = car_coord[0]
            return True
        else:
            return False

