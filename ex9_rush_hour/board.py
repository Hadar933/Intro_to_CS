
class Board:
    """
    Add a class description here.
    Write briefly about the purpose of the class
    """

    def __init__(self,height=7,width=7):
        """
        A constructor for Board object
        :param height: 7
        :param width: 7
        """
        self.__cars = []
        self.__height = height
        self.__width = width

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        board_lists = [['_']*self.__width for rows in range(self.__height)]
        for car in self.__cars:
            car_coords = car.car_coordinates()
            for item in car_coords:
                if item == (3,7):
                    pass
                else:
                    board_lists[item[0]][item[1]] = car.get_name()
        board_str = '\n'.join(' '.join(sub) for sub in board_lists)
        return board_str

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        lst_of_idx = []
        height = self.__height
        width = self.__width
        for i in range(width):
            for j in range(height):
                lst_of_idx.append((i,j))
        lst_of_idx.append((3,7))
        return lst_of_idx

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description) 
                 representing legal moves
        """
        lst_of_direcs = []
        for a_car in self.__cars:
            good_moves = a_car.possible_moves()
            new =  [(a_car.get_name(),dire, des) for dire, des\
                    in good_moves.items()]
            lst_of_direcs.append(new[0])
            lst_of_direcs.append(new[1])
        return lst_of_direcs

    def target_location(self):
        """
        This function returns the coordinates of the location which is to be
        filled for victory.
        :return: (row,col) of goal location
        """
        lst = self.cell_list()
        return lst[-1]

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        for car in self.__cars:
            car_coords = car.car_coordinates()
            if coordinate in car_coords:
                return car.get_name()
        return

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        car_coords = car.car_coordinates()
        for coord in car_coords:
            if coord not in self.cell_list():  # not in 7*7 board
                return False
            elif self.cell_content(coord) is not None:
                return False
        for old_car in self.__cars:
            if old_car.get_name() == car.get_name():
                return False
        self.__cars.append(car)
        return True

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        for a_car in self.__cars:
            if name == a_car.get_name() \
                    and movekey in a_car.possible_moves():
                empty_cell = a_car.movement_requirements(movekey)
                lst_of_idx = self.cell_list()
                last_cell = lst_of_idx[-1]
                if empty_cell[0] == last_cell:
                    a_car.move(movekey)
                    return True
                if self.cell_content(empty_cell[0]) is None \
                        and empty_cell[0] in self.cell_list():
                    a_car.move(movekey)
                    return True
        return False

