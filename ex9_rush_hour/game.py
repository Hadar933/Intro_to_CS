from helper import *
from board import *
from car import *


class Game:
    """
    Add class description here
    """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        self.__board = board

    def input_receiver(self):
        """
        checks the user input
        :return: valid user input
        """
        VALID_COLORS = ['Y', 'B', 'O', 'G', 'W', 'R']
        VALID_DIRECTIONS = ['u', 'd', 'l', 'r']

        user_inp = input('Provide a car to move and a direction'
                           ' seperated by a comma and without spaces: ')
        user_input = user_inp.split(',')
        color = user_input[0]
        direction = user_input[1]
        while color not in VALID_COLORS or direction not in VALID_DIRECTIONS:
            user_inp = input('Invalid color or direction. Try again: ')
            user_input = user_inp.split(',')
            color = user_input[0]
            direction = user_input[1]
            if color in VALID_COLORS and direction in VALID_DIRECTIONS:
                break
        possible_directions = self.__board.possible_moves()
        for item in possible_directions:
            if item[1] == direction:
                return user_input
        return

    def __single_turn(self):
        """
        All operations thar are performed in a single turn
        """
        print(self.__board)
        valid_input = self.input_receiver()
        name = valid_input[0]
        movekey = valid_input[1]
        if valid_input is not None:
            self.__board.move_car(name,movekey) #valid move
        else:
            print('Invalid Move!')

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        while True:
            winning_index = self.__board.target_location()
            if self.__board.cell_content(winning_index) is not None:
                print('You win!')
                break
            self.__single_turn()


def json_loader(filename):
    """
    checks if the json file content suits the game
    :param filename: name of json file
    :return:
    """
    VALID_NAMES = ['Y','B','O','W','G','R']
    lst_of_cars = []
    json_file = load_json(filename)
    for item in json_file:
        content = json_file[item]
        length = content[0]
        location = tuple(content[1])
        orientation = content[2]
        if 2<=length<=4:
            if orientation == 1 or orientation == 0:
                if item in VALID_NAMES:
                    car = Car(item, length, location, orientation)
                    lst_of_cars.append(car)
    for i in range(len(lst_of_cars)):
        for j in range(i+1,len(lst_of_cars)):
            if lst_of_cars[i] == lst_of_cars[j]:
                del lst_of_cars[i]
    return lst_of_cars


def car_adder(filename):
    """
    adds a car to the board
    :param filename: json file
    """
    lst_of_cars = json_loader(filename)
    for car in lst_of_cars:
        board1.add_car(car)


if __name__ == "__main__":
    board1 = Board()
    game1 = Game(board1)
    car_adder('car_config.json')
    game1.play()
