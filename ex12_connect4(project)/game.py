from ai import *
NUM_OF_COLUMNS = 7
NUM_OF_ROWS = 6

PLAYER_1_C = "R"
PLAYER_2_C = "B"
GAME_OVER_OPTIONS = [1, 2, 0]


class Game:
    """
    This class is in charge enforcing the rules of the game during its run.
    All actions which happen on the board which are related to inserting
    a disc into the game are monitored by the different methods of the class.
    """

    def __init__(self, row=NUM_OF_ROWS, column=NUM_OF_COLUMNS):
        """
        The constructor for the Game class. Contains defaulted values for the
        size of the board. The constructor also holds a list of objects of
        type Disc and the game board itself which is being updated each turn.
        :param row: height of the board, 6 by default.
        :param column: width of the board, 7 by default.
        """
        self.row = row
        self.columns = column
        self.disc = []
        self.__curr_player = 1
        self.board = [["_"] * self.columns for row in range(self.row)]
        self.win_disc_lst = []
        self.winner = None

    def __str__(self):
        """
        this method prints the board into the console, used mostly for
        checking the game before the graphic interface comes into use.
        :return: returns the updated board.
        """
        str_board = "\n".join(" ".join(row) for row in self.board)
        return str_board

    def set_winner(self, winner):
        """
        sets the winner of the game.
        """
        self.winner = winner

    def change_board(self):
        """
        This method appllies all changes that have happend in a single turn
        to the board. runs under make_move method.
        """
        for disc in self.disc:
            if disc not in self.board:
                self.board[disc.get_cor()[0]][disc.get_cor()[1]] = \
                    disc.get_color()

    def make_move(self, column):
        """
        This method is the main method of this class. Most of the game occurs
        within this method. It checks the board and adds the discs into the
        board according to the rules of the game.
        """
        if column not in range(NUM_OF_COLUMNS) or self.get_winner() \
            in GAME_OVER_OPTIONS or not self.check_column_length(column):
                raise Exception("Illegal move")

        curr_player = self.get_current_player()
        if curr_player == 1:
            # checks which player and sets disc color accordingly
            player_color = PLAYER_1_C  # color - red
        else:
            player_color = PLAYER_2_C  # color - blue
        if self.check_column_length(column):
            if self.check_column(column):
                # checks what spot is free and if there is an open spot
                # in the given column
                temp_row = self.check_column(column)[1]
                if self.get_winner() in GAME_OVER_OPTIONS:
                    return
                    # doesnt allow more discs to be added after the games over
                temp_disc = Disc(player_color,
                                 (temp_row, column))
                self.disc.append(temp_disc)  # adds disc to list

                self.change_board()  # updates board accordingly
                self.set_curr_player()  # changes player.
                return
        return

    def get_winner(self):
        """
        This method checks each round for a winning move of one of the players
        it calls on four helper methods that each check on of the possible
        ways to have four in a row. One of the helper methods being True is
        enough to win.
        :return: The number 1 if player 1 won, number 2 if player 2 won.
        """
        if self.check_row_win() or self.check_col_win() or self.check_diag1()\
                or self.check_diag2():
            if self.get_current_player() == 1:
                self.set_winner(2)
                return self.winner
            self.set_winner(1)
            return self.winner
        elif self.check_full_board() == 0:
            self.set_winner(0)
            return self.check_full_board()
        return self.winner

    def check_full_board(self):
        """
        This method checks for a tie in the game. a tie means a full board so
        we run over the board looking for empty spots, if we find one, the
        game goes on, If the board is full its a tie.
        :return: nothing if game there isn't a tie, 0 if there is a tie.
        """
        for i in range(self.row):
            for j in range(self.columns):
                if self.board[i][j] == "_":  # checks for empty spots.
                    return
        return 0

    def get_last_disc_color(self):
        """
        :return: The color of the disc according to the player number.
        """
        if self.get_current_player() == 1:
            color = "B"
        else:
            color = "R"
        return color

    def check_row_win(self):
        """
        This method runs over the board and checks for a win situation in a
        row. Looks for four horizontal discs which are adjacent.
        :return: True if there are four in a row, False otherwise.
        """
        player_color = self.get_last_disc_color()
        for i in range(self.columns):
            for j in range(self.row):
                # runs over all board.
                try:
                    if self.board[i][j] == player_color and \
                            self.board[i][j + 1] == player_color and \
                            self.board[i][j + 2] == player_color and \
                            self.board[i][j + 3] == player_color:
                        for k in range(4):
                            if j == 0:
                                self.win_disc_lst.append((i, k))
                            else:
                                self.win_disc_lst.append((i, j + k))
                        return True
                except IndexError:
                    continue
        return False

    def check_col_win(self):
        """
        This method runs over the board and checks for a series of four discs
        of the same color which are also together. runs over nested loops
        when it reaches the end of the index, throws an index error which we\
        catch here and send it to the next loop.
        :return: returns True if there are four discs in a row,
        False otherwise.
        """
        player_color = self.get_last_disc_color()
        for i in range(self.row):
            for j in range(self.columns):
                # runs over the board.
                try:
                    if self.board[i][j] == player_color and \
                            self.board[i + 1][j] == player_color and \
                            self.board[i + 2][j] == player_color and \
                            self.board[i + 3][j] == player_color:
                        # checks if all conditions for winning are met.
                        for k in range(4):
                            self.win_disc_lst.append((i + k, j))
                        return True
                except IndexError:
                    # runs out of index on list, catches the error and
                    # iterates again.
                    continue
        return False  # no vertical fours are founds.

    def check_diag1(self):  # check the "/" diagonal
        """
        This method checks all diagonals running from left to top right.
        :return: True if it finds a winning four, False otherwise.
        """
        player_color = self.get_last_disc_color()  # the players color.
        for i in range(3, self.row):
            for j in range(self.columns):
                # runs over the board.
                try:
                    if self.board[i][j] == player_color and \
                            self.board[i - 1][j + 1] == player_color and \
                            self.board[i - 2][j + 2] == player_color and \
                            self.board[i - 3][j + 3] == player_color:
                        # moves diagonally.
                        for k in range(4):
                            self.win_disc_lst.append((i - k, j + k))
                        return True
                    # all conditions are met, returns True.
                except IndexError:  # catches error, runs over next iteration.
                    continue
        return False  # no fours are found.

    def check_diag2(self):  # checks the "\" diagonal
        """
        This method checks all diagonals running from left to bottom right.
        :return: True if it finds a winning four, False otherwise.
        """
        player_color = self.get_last_disc_color()
        for i in range(self.row):
            for j in range(self.columns):
                # runs over the board.
                try:
                    if self.board[i][j] == player_color and \
                            self.board[i + 1][j + 1] == player_color and \
                            self.board[i + 2][j + 2] == player_color and \
                            self.board[i + 3][j + 3] == player_color:
                        # moves down to the right diagonally
                        for k in range(4):
                            self.win_disc_lst.append((i + k, j + k))
                        return True
                    # found four of a kind, returns True.
                except IndexError:
                    continue  # catches error, runs over next iteration.
        return False

    def get_player_at(self, row, col):
        """
        this method checks a specific coordinates and returns values which
        indicate if theres a disc on that spot or its empty.
        :param row: to row we would like to check.
        :param col: the column we would like to check.
        :return: returns 1, or 2 to indicate if there is a disc of one of the
        players. if the spot is empty returns None.
        """
        for disc in self.disc:  # checks for each of the discs on board.
            if abs(row) not in range(NUM_OF_ROWS + 1) or col \
                    not in range(NUM_OF_COLUMNS):
                print(abs(row), col)
                raise Exception("Illegal location")
            if self.board[row][col] == disc.get_color():
                # checks if there is even a disc at the given coordinates
                if disc.get_color() == "R":
                    return 1  # if its player 1
                return 2  # if its player 2
        return None  # if the spot is empty

    def get_current_player(self):
        """
        This method returns 1 if its the first players turns, 2 otherwise.
        """
        return self.__curr_player

    def set_curr_player(self):
        """
        this method changes the player between turns.
        """
        if self.get_current_player() == 1:  # changes between the two players.
            self.__curr_player = 2
        else:
            self.__curr_player = 1

    def check_column(self, column):
        """
        checks a given row for empty places by checking if there is a disc on
        that spot.
        :param column: the column we would like to check.
        :return: returns True if the spot there is a free spot, False
        otherwise.
        """
        for i in range(1, NUM_OF_ROWS + 1):
            try:
                # runs over all rows of given column
                if self.get_player_at(-i, column):
                    # if there is a disc, checks next.
                    continue
                if not self.get_player_at(-i, column):
                    # if the spot is empty returns True and the row number.
                    return True, self.row - i
            except IndexError:
                continue

        # no empty rows in the given column, raises an exception

    def check_column_length(self, column):
        """
        this method is made to prevent the user from being able to make
        illegal moves like adding a disc to a full row. it creates a list of
        all objects in the given column and checks the length. if the length
        is less then 6, more discs can be inserted and the method returns True
        otherwise there are 6 discs and the column is full so we return False.
        :param column: the given column we would like to check.
        :return: returns True if a disc can be inserted, False otherwise.
        """
        obj_in_col = []
        for item in self.disc:  # runs over all existing discs.
            if item.get_cor()[1] == column:
                # checks if the disc is in the column we would like to check.
                obj_in_col.append(item)  # if it is, appends it.
        if len(obj_in_col) < 6:  # checks if the list has 6 items.
            return True
        return False


class Disc:
    def __init__(self, color, coordinates):
        """
        The constructor of the Disc class, holds two fields, the color of the
        disc and its location on the board which is represented by a tuple
        (x_cor, y_cor).
        :param color: color of the disc, indicates the player.
        :param coordinates: the discs location on the board.
        """
        self.__color = color
        self.__coordinates = coordinates

    def get_cor(self):
        """
        this method returns the coordinates of the disc on the board.
        """
        disc_r = self.__coordinates[0]
        disc_c = self.__coordinates[1]
        return disc_r, disc_c

    def get_color(self):
        """
        returns the color of the disc which indicates which player owns
         the disc.
        """
        return str(self.__color)


