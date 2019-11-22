from screen import Screen
import sys
import random
from ship import *
from asteroid import *
from torpedo import *
import math

DEFAULT_ASTEROIDS_NUM = 5
SCREEN_SIZE = 500
INITIAL_AST_SIZE = 3
ship_x_pos = random.randint(-SCREEN_SIZE, SCREEN_SIZE)
ship_y_pos = random.randint(-SCREEN_SIZE, SCREEN_SIZE)
MAX_AST_VELOCITY = 4
MIN_AST_VELOCITY = 1

class GameRunner:
    """
    this class is responsible for the entire game run
    """

    def __init__(self, asteroids_amount):
        """
        Generator for the main program. responsible for the creation
        of the ship. Also stores the asteroids and the torpedoes data,
        and some other various constants
        :param asteroids_amount:
        """
        self.__screen = Screen()
        self.__ship = Ship(ship_x_pos,ship_y_pos,0,0,0)
        self.__asteroids = []
        self.__torpedoes = []
        self.__screen_max_x = Screen.SCREEN_MAX_X
        self.__screen_max_y = Screen.SCREEN_MAX_Y
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_y = Screen.SCREEN_MIN_Y
        self.asteroid_helper()
        self.asteroid_registration()
        self.__points = 0
        self.__asteroid_amount = asteroids_amount

    def all_purpose_move(self):
        """
        moves all objects of the game
        """
        self.objects_mover(self.__ship) # move ship
        for asteroid in self.__asteroids:
            self.objects_mover(asteroid) # move all asteroids
        for torpedo in self.__torpedoes:
            self.objects_mover(torpedo) # move all torpedoes

    def objects_mover(self,obj):
        """
        creates a new coordinate and changes the old one.
        :param obj: ship torpedo or asteroid
        """
        delta_x = self.__screen_max_x - self.__screen_min_x
        delta_y = self.__screen_max_y - self.__screen_min_y
        old_coord_x = obj.get_x_pos() # X axis data
        x_vel = obj.get_x_vel()
        old_coord_y = obj.get_y_pos() # Y axis data
        y_vel = obj.get_y_vel()
        new_coord_x = (x_vel+old_coord_x-self.__screen_min_x)\
                      % delta_x+self.__screen_min_x
        new_coord_y = (y_vel+old_coord_y-self.__screen_min_y)\
                      % delta_y+self.__screen_min_y
        obj.set_x_pos(new_coord_x) # setting new values to the position
        obj.set_y_pos(new_coord_y)

    def ship_direction(self):
        """
        changes the direction of the ship (changes are in radians)
        """
        prev_dir = self.__ship.get_direction()
        movement = 7
        if self.__screen.is_left_pressed():
            self.__ship.set_direction(prev_dir + movement)
        elif self.__screen.is_right_pressed():
            self.__ship.set_direction(prev_dir - movement)

    def ship_acceleration(self):
        """
        accelerates the ship according to provided equation
        """
        prev_x_vel = self.__ship.get_x_vel()
        prev_y_vel = self.__ship.get_y_vel()
        dir = self.__ship.get_direction()
        dir_in_rad = math.radians(dir)
        if self.__screen.is_up_pressed():
            new_x_vel = prev_x_vel + math.cos(dir_in_rad)
            new_y_vel = prev_y_vel + math.sin(dir_in_rad)
            self.__ship.set_x_vel(new_x_vel)
            self.__ship.set_y_vel(new_y_vel)

    def asteroid_helper(self):
        """
        provides the amount of asteroids to be created to the
        asteroid generator function
        """
        if len(sys.argv) == 1:
            self.asteroid_generator(DEFAULT_ASTEROIDS_NUM)
        else:
            self.asteroid_generator(int(sys.argv[1]))

    def asteroid_generator(self,asteroid_amount):
        """
        this function generates asteroids and adds them to the list in
        the generator. Furthermore, the function makes sure that the
        position isnt equal to the position of the ship.
        if so, a new position is being assigned
        """
        for num in range(asteroid_amount):
            x_pos = random.randint(-SCREEN_SIZE, SCREEN_SIZE)
            y_pos = random.randint(-SCREEN_SIZE, SCREEN_SIZE)
            x_vel = random.randint(MIN_AST_VELOCITY,MAX_AST_VELOCITY)
            y_vel = random.randint(MIN_AST_VELOCITY,MAX_AST_VELOCITY)
            while x_pos == ship_x_pos and y_pos == ship_y_pos: #same position
                new_x_pos = random.randint(-SCREEN_SIZE, SCREEN_SIZE)
                if new_x_pos != ship_x_pos:
                    x_pos = new_x_pos
                    break
                else:
                    continue
            asteroid = Asteroid(x_pos,y_pos,x_vel,y_vel,INITIAL_AST_SIZE)
            self.__asteroids.append(asteroid) # adds new asteroid to lst

    def asteroid_registration(self):
        """
        this function registers the created asteroids to the screen
        """
        for asteroid in self.__asteroids:
            self.__screen.register_asteroid(asteroid,INITIAL_AST_SIZE)

    def life_taker(self):
        """
        if a collision has been occurred, life mana will decrease by one.
        an informative message will appear to the user
        """
        for asteroid in self.__asteroids:
            if asteroid.has_intersection(self.__ship):
                self.__screen.remove_life()
                self.__screen.show_message\
                    ('You were hit!','Your life has been decreased by 1.')
                self.__asteroids.remove(asteroid)
                self.__screen.unregister_asteroid(asteroid)
                break

    def torpedo_generator(self):
        """
        creating a torpedo when space is pressed.
        creation is made only if there are no more than 10 torpedoes on the
        screen.
        creation is according to given speed equations
        """
        if self.__screen.is_space_pressed() and len(self.__torpedoes) <= 9:
            x_pos = self.__ship.get_x_pos()
            y_pos = self.__ship.get_y_pos()
            direction = self.__ship.get_direction()
            cur_x_vel = self.__ship.get_x_vel()
            cur_y_vel = self.__ship.get_y_vel()
            new_x_vel = cur_x_vel + (2 * math.cos(math.radians(direction)))
            new_y_vel = cur_y_vel + (2 * math.cos(math.radians(direction)))
            torpedo = Torpedo(x_pos,y_pos,new_x_vel,new_y_vel,direction)
            self.__torpedoes.append(torpedo)
            self.__screen.register_torpedo(torpedo)

    def game_points(self,asteroid):
        """
        adds point according to the size of the asteroid
        :param asteroid: object of type asteroid
        """
        if asteroid.get_size() == 3:
            self.__points += 20
            self.__screen.set_score(self.__points)
        if asteroid.get_size() == 2:
            self.__points += 50
            self.__screen.set_score(self.__points)
        if asteroid.get_size() == 1:
            self.__points += 100
            self.__screen.set_score(self.__points)

    def split_ast_generator(self,size,asteroid,torpedo):
        """
        deletes the asteroid that was hit and creates a new one with
        size smaller by one. creation is based on given speed equations
        :param size: size of asteroid
        :param asteroid: object of type asteroid
        :param torpedo: object of type torpedo
        """
        x_pos = asteroid.get_x_pos()
        y_pos = asteroid.get_y_pos()
        cur_x_vel = asteroid.get_x_vel()
        cur_y_vel = asteroid.get_y_vel()
        new_size = size-1
        x_vel = (torpedo.get_x_vel()+cur_x_vel)/\
                (math.sqrt(cur_x_vel**2+cur_y_vel**2))
        y_vel = (torpedo.get_y_vel()+cur_y_vel)/\
                (math.sqrt(cur_y_vel**2+cur_x_vel**2))
        # first asteroid creation
        ast_1 = Asteroid(x_pos,y_pos,x_vel,y_vel,new_size)
        self.__asteroids.append(ast_1)
        self.__screen.register_asteroid(ast_1,new_size)
        # second asteroid creation
        ast_2 = Asteroid(x_pos,y_pos,(-1) * x_vel,(-1) * y_vel,new_size)
        self.__asteroids.append(ast_2)
        self.__screen.register_asteroid(ast_2,new_size)

    def destruction_helper(self, size, asteroid, torpedo):
        """
        according to given size, this function decides how the creation of
        the new asteroids and the deletion of the old asteroid should be done.
        :param size: size of asteroid
        :param asteroid: object of type asteroid
        :param torpedo: object of type torpedo
        """
        if size > 1:
            self.split_ast_generator(size, asteroid, torpedo)
            self.__asteroids.remove(asteroid)
            self.__screen.unregister_asteroid(asteroid)
        else: # no size decrease available - deletes
            self.__asteroids.remove(asteroid)
            self.__screen.unregister_asteroid(asteroid)

    def collision_total(self):
        """
        this function sums up all that is to happen while a collision takes
        place
        """
        for asteroid in self.__asteroids:
            size = asteroid.get_size()
            for torpedo in self.__torpedoes:
                if asteroid.has_intersection(torpedo):
                    self.game_points(asteroid)
                    self.destruction_helper(size,asteroid,torpedo)
                    break

    def torpedo_life(self):
        """
        if 200 game laps have passes - the torpedo will vanish.
        """
        MAX_GAME_LAPS = 200
        for torpedo in self.__torpedoes:
            torpedo.set_life()
            if torpedo.get_life() == MAX_GAME_LAPS:
                self.__torpedoes.remove(torpedo)
                self.__screen.unregister_torpedo(torpedo)

    def teleporter(self):
        """
        by clicking 't', the ship will be teleported to an EMPTY space on
        the screen.(spot with no asteroid in it)
        """
        x_pos = random.randint(-SCREEN_SIZE, SCREEN_SIZE)
        y_pos = random.randint(-SCREEN_SIZE, SCREEN_SIZE)
        for asteroid in self.__asteroids:
            if x_pos==asteroid.get_x_pos() and y_pos==asteroid.get_y_pos():
                new_x_pos = random.randint(-SCREEN_SIZE, SCREEN_SIZE)
                x_pos = new_x_pos
                break
            if x_pos != asteroid.get_x_pos():
                continue

        self.__ship.set_x_pos(x_pos)
        self.__ship.set_y_pos(y_pos)

    def game_ending(self):
        """
        this function is responsible for exiting the game wheneven needed:
        win - no asteroids left
        lose - no life left
        Q - user presses q(quit)
        """
        if len(self.__asteroids) == 0:
            self.__screen.show_message('No asteroids left','You win!')
            self.__screen.end_game()
            sys.exit()
        if len(self.__screen._lives) == 0 :
            self.__screen.show_message('No life left','You Lose!')
            self.__screen.end_game()
            sys.exit()
        if self.__screen.should_end():
            self.__screen.show_message('pressed Q - quitting'
                                       ,'Nobody loves a quitter :(')
            self.__screen.end_game()
            sys.exit()

    def run(self):
        self._do_loop()
        self.__screen.start_screen()

    def _do_loop(self):
        # You don't need to change this method!
        self._game_loop()
        # Set the timer to go off again
        self.__screen.update()
        self.__screen.ontimer(self._do_loop, 5)

    def _game_loop(self):
        """
        This function runs all of the methods that are being executed
        in a single game loop.
        """
        self.all_purpose_move() # moves all objects
        self.ship_direction() # moves the angle of the ship's head
        self.ship_acceleration() # accelerates the ship
        self.__screen.draw_ship(self.__ship.get_x_pos() # draws ship
                                ,self.__ship.get_y_pos(),
                                self.__ship.get_direction())
        for asteroid in self.__asteroids:
            self.__screen.draw_asteroid(asteroid, # draws asteroids
                                        asteroid.get_x_pos(),
                                        asteroid.get_y_pos())
        self.life_taker()
        for torpedo in self.__torpedoes:
            self.__screen.draw_torpedo(torpedo, # draws torpedoes
                                       torpedo.get_x_pos(),
                                       torpedo.get_y_pos(),
                                       torpedo.get_direction())
        self.torpedo_generator() # creates torpedoes
        self.collision_total() # all collision operations
        self.torpedo_life() # sets torpedo life to 200 loops
        self.game_ending() # ends the game when needed
        if self.__screen.is_teleport_pressed(): # teleports the ship
            self.teleporter()


def main(amount):
    runner = GameRunner(amount)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
