import random
GAME_OVER_OPTIONS = [1, 2, 0]


class AI:

    def __init__(self, game, player):
        """
        The constructor for the AI class. each object of type AI holds two
        attributes.
        :param game: an object of type game, which holds the board and the
        rules.
        :param player: Which player the AI represents. could either 1 or 2.
        """
        self.game = game
        self.player = player

    def find_legal_move(self, timeout=None):
        """
        This method iterates over the board and find an empty spot to place
        a disc on. This method uses the get_player_at method, if there is no
        player at the spot it means it is empty.
        :return: a list of columns which putting a disc into is considered a
        legal move. The list is limited to length of 6 to prevent the method
        from returning the same row several times.
        """
        move_lst = []
        for i in range(self.game.row):
            for j in range(self.game.columns):
                # runs over the board.
                    if not self.game.get_player_at(i, j) and j \
                            not in move_lst:
                        move_lst.append(j)
        if not move_lst:
            raise Exception("No possible AI moves")
        return random.choice(move_lst)

    def get_last_found_move(self):
        pass
