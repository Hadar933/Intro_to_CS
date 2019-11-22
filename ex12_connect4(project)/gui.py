import tkinter as tk
from game import *
from ai import *


GAME_OVER_OPTIONS = [1, 2, 0]
SEG_SIZE = 80  # the dimensions will be based on this constant segment size
COL = 7
ROW = 6
SIZE = '720x560'  # dimensions of the game
WAIT_TIME = 400

# GAME MODES #
PCVPC = 1
PCVP = 2
PVPC = 3
PVP = 4


class GUI:
    """
    this class is responsible for the creation of the GUI - the graphics
    of the game
    """

    def __init__(self):
        """
        a constructor for GUI object
        """
        self.width = (COL + 2) * SEG_SIZE
        self.height = (ROW + 1) * SEG_SIZE
        self.font = 'Times'
        self.root = tk.Tk()  # root for the main menu
        self.nroot = None  # root of the game window
        self.canv = None  # canvas for the game window
        self.wroot = None  # root for end game window
        self.game = Game()
        self.ai1 = AI(self.game, 1)
        self.ai2 = AI(self.game, 2)
        # self.root.protocol("WM_DELETE_WINDOW", self.del_window)
        self.game_mode = None  # will be assigned with values from 1 to 4
        # describing the game-mode

    def del_window(self):
        exit()

    def set_flag(self):
        """
        Sets the exit flag to True, meaning someone pressed the exit button.
        """
        self.ex_flag = True

    def set_game_mode(self, new_game_mode):
        """
        setter for the chosen game mode
        """
        self.game_mode = new_game_mode

    def set_game(self):
        """
        a setter for a new game
        """
        self.game = Game()

    def set_wroot(self, new_wroot):
        """
        a setter for a new end game window
        :param new_wroot: new end game window(wroot)
        """
        self.wroot = new_wroot

    def set_canv(self, new_canv):
        """
        a setter for a new canvas
        """
        self.canv = new_canv

    def set_root(self, new_root):
        """
        a setter for a new main menu root
        :param new_root: new main menu root
        """
        self.root = new_root

    def start_screen(self):
        """
        this function creates and opens the main screen with the game options
        """
        # MAIN WINDOW DISPLAY #
        self.root.geometry(SIZE)
        title = tk.Label(self.root, text='Welcome to connect-4!',
                         font=(self.font, 20))
        title.pack(side=tk.TOP)
        sub_title = tk.Label(self.root, text='Please choose mode:',
                             font=(self.font, 15))
        sub_title.pack(side=tk.TOP)

        # BUTTONS (Coordinates are based on the screen Symmetry) #

        # COMPUTER VS COMPUTER #
        b_pcvpc = tk.Button(self.root, text='Pc VS Pc',
                            command=self.pc_vs_pc_redirect,
                            font=(self.font, 10))
        b_pcvpc.pack()
        b_pcvpc.place(x=15, y=200, height=140, width=162)

        # COMPUTER VS PERSON #
        b_pcvp = tk.Button(self.root, text='Pc VS Person',
                           command=self.pc_vs_p_redirect,
                           font=(self.font, 10))
        b_pcvp.pack()
        b_pcvp.place(x=192, y=200, height=140, width=162)

        # PERSON VS COMPUTER #
        b_pvpc = tk.Button(self.root, text='Person VS Pc',
                           command=self.p_vs_pc_redirect,
                           font=(self.font, 10))
        b_pvpc.pack()
        b_pvpc.place(x=369, y=200, height=140, width=162)

        # PERSON VS PERSON #
        b_pvp = tk.Button(self.root, text='Person VS Person',
                          command=self.p_vs_p_redirect,
                          font=(self.font, 10))
        b_pvp.pack()
        b_pvp.place(x=546, y=200, height=140, width=162)

        self.root.mainloop()

    def pc_vs_pc_redirect(self):
        """
        redirects to pc_vs_pc game mode
        """
        self.set_game_mode(PCVPC)
        self.root.destroy()
        self.main_game()

    def pc_vs_p_redirect(self):
        """
        redirects to pc_vs_person game mode
        """
        self.set_game_mode(PCVP)
        self.root.destroy()
        self.main_game()

    def p_vs_pc_redirect(self):
        """
        redirects to person_vs_pc game mode
       """
        self.set_game_mode(PVPC)
        self.root.destroy()
        self.main_game()

    def p_vs_p_redirect(self):
        """
        redirects to person_vs_person game mode
        """
        self.set_game_mode(PVP)
        self.root.destroy()
        self.main_game()

    def mboard_graphics(self):
        """
        creates the graphics of the main game
        :return:
        """
        # CANVAS #
        ncanv = tk.Canvas(width=self.width, height=self.height)  # canvas
        self.set_canv(ncanv)
        self.canv.pack()

        # SHAPES #
        C = 5  # size constant - part of a disc's size
        self.canv.configure(bg='yellow2')
        self.canv.create_rectangle(0, 0, SEG_SIZE, self.height, fill='tomato')
        self.canv.create_rectangle(self.width - SEG_SIZE, 0, self.width,
                                   self.height, fill='tomato')
        self.canv.create_rectangle(SEG_SIZE, 0, self.width - SEG_SIZE,
                                   SEG_SIZE, fill='white')
        self.canv.create_rectangle(SEG_SIZE, SEG_SIZE + 3,
                                   self.width - SEG_SIZE, SEG_SIZE,
                                   fill='black')
        for c in range(1, COL + 1):  # creating the board sockets
            for r in range(1, ROW + 1):
                self.canv.create_oval(SEG_SIZE * c + C, SEG_SIZE * r + C,
                                      SEG_SIZE * c + SEG_SIZE - C,
                                      SEG_SIZE * r + SEG_SIZE - C,
                                      fill='black')

    def pc_vs_pc(self):
        """
        this function executes the automatic game - pc vs pc
        """
        # MOVE IS EXECUTED #
        if self.game.get_current_player() == 1:
            try:
                good_moves1 = self.ai1.find_legal_move()
                self.game.make_move(good_moves1)
            except Exception:
                pass
            self.update_game()
        else:
            good_moves2 = self.ai2.find_legal_move()
            try:
                self.game.make_move(good_moves2)
                self.update_game()
            except Exception:
                pass
        self.declare_winner()

    def main_game(self):
        """
        runs all of the games depending on the user's choice
        """

        # BOARD #
        mroot = tk.Tk()  # main menu root
        self.set_root(mroot)
        self.root.geometry(SIZE)
        self.mboard_graphics()

        # GAME-PLAY #
        if self.game_mode == PCVPC:  # COMPUTER VS COMPUTER
            while self.root and self.game.get_winner() \
                    not in GAME_OVER_OPTIONS:
                self.pc_vs_pc()
                mroot.update()
                mroot.after(WAIT_TIME)

        if self.game_mode == PCVP:  # COMPUTER VS PERSON
            while self.root and self.game.get_winner() \
                    not in GAME_OVER_OPTIONS:
                if self.game.get_current_player() == 1:
                    # self.root.unbind("<Motion>")
                    # self.root.unbind("<Button-1>")
                    try:
                        good_moves = self.ai1.find_legal_move()
                        self.game.make_move(good_moves)
                    except Exception:
                        pass
                    mroot.update()
                    mroot.after(WAIT_TIME)
                    self.update_game()
                    self.declare_winner()
                else:
                    self.root.bind('<Motion>', self.move_towards_mouse)
                    self.root.bind('<Button-1>', self.fall_to_pos)
                    mroot.update()

        if self.game_mode == PVPC:  # PERSON VS COMPUTER
            while self.root and self.game.get_winner() \
                    not in GAME_OVER_OPTIONS:
                if self.game.get_current_player() == 1:
                    self.root.bind('<Motion>', self.move_towards_mouse)
                    self.root.bind('<Button-1>', self.fall_to_pos)
                    mroot.update()
                else:
                    try:
                        good_moves = self.ai2.find_legal_move()
                        self.game.make_move(good_moves)
                    except Exception:
                        pass
                    mroot.update()
                    mroot.after(WAIT_TIME)
                    self.update_game()
                    self.declare_winner()

        if self.game_mode == PVP:  # PERSON VS PERSON
            self.root.bind('<Motion>', self.move_towards_mouse)
            self.root.bind('<Button-1>', self.fall_to_pos)


        mroot.mainloop()

    def update_game(self):
        """
        updates the board after a move has been made
        """
        C = 5  # will be used to decrease disc radius
        clr_idx_lst = self.get_color_idx()
        for item in clr_idx_lst:
            color = item[0]
            if color == 'R':
                new_clr = 'red'
            else:
                new_clr = 'blue'
            col = (item[1] + 1) * SEG_SIZE
            row = (item[2] + 1) * SEG_SIZE
            self.canv.create_oval(col + C, row + C, col + SEG_SIZE - C,
                                    row + SEG_SIZE - C, fill=new_clr)

    def move_towards_mouse(self, event):
        """
        creates a circle with the color of the player that tracks the
        mouse in order to indicate a the wanted dropping place
        :param event: mouse movement
        """
        X_RANGE = []  # event in these positions will trigger object following
        C = 1.5  # constant the makes sure circle wont cross edges
        l_range = int(C * SEG_SIZE)
        r_range = int(self.width - C * SEG_SIZE)
        [X_RANGE.append(i) for i in range(l_range, r_range)]
        turn = self.game.get_current_player()
        if event.x in X_RANGE:
            self.canv.create_rectangle(SEG_SIZE, 0, self.width - SEG_SIZE,
                                       SEG_SIZE, fill='white')
            # deletes prev circle
            if turn == 1:  # Red's turn
                self.canv.create_oval(event.x - 0.5 * SEG_SIZE, 2
                                      , event.x + 0.5 * SEG_SIZE,
                                      SEG_SIZE - 2, fill='red')
            if turn == 2:  # Blue's turn
                self.canv.create_oval(event.x - 0.5 * SEG_SIZE, 2
                                      , event.x + 0.5 * SEG_SIZE - 2,
                                      SEG_SIZE - 2, fill='blue')

    def fall_to_pos(self, event):
        """
        this functions runs the process of the game: "drops" the disc into
        the event's position and declares the winner.
        :param event: mouse click
        """

        cols = []  # represents the event.x indexes of every column
        for i in range(1, COL + 1):
            col = list(range(i * SEG_SIZE, (i + 1) * SEG_SIZE))
            cols.append(col)
        for column in cols:
            if event.x in column:
                col_idx = cols.index(column)
                self.game.make_move(col_idx)
                self.update_game()
        # WINNER #
        self.declare_winner()

    def get_color_idx(self):
        """
        gets all the positions of a disc from the board
        :return: list of lists in the format [[color,column,row]..[]]
        """
        color_idx_lst = []
        for c in range(len(self.game.board[0])):
            for r in range(len(self.game.board)):
                color = self.game.board[r][c]
                if color == '_':
                    continue
                else:
                    color_idx_lst.append([color, c, r])
        return color_idx_lst

    def winner_window(self, winner):
        """
        declares the winner and creates the end-of-game window pop up
        """
        self.winning_discs()
        if winner == 1:  # red wins
            wroot = tk.Tk()
            self.set_wroot(wroot)
            self.wroot.geometry('100x100')
            title = tk.Label(self.wroot, text='Red wins!',
                             font=(self.font, 20))
            title.pack(side=tk.TOP)
            b_exit = tk.Button(self.wroot, text='Exit',
                               command=self.exit, font=(self.font, 10))
            b_play_again = tk.Button(self.wroot, text='Play again!',
                                     command=self.play_again,
                                     font=(self.font, 10))
            b_exit.pack()
            b_play_again.pack()

        elif winner == 2:  # blue wins
            wroot = tk.Tk()
            self.set_wroot(wroot)
            self.wroot.geometry('100x100')
            title = tk.Label(self.wroot, text='Blue wins!',
                             font=(self.font, 20))
            title.pack(side=tk.TOP)
            b_exit = tk.Button(self.wroot, text='Exit',
                               command=self.exit, font=(self.font, 10))
            b_play_again = tk.Button(self.wroot, text='Play again!',
                                     command=self.play_again,
                                     font=(self.font, 10))
            b_exit.pack()
            b_play_again.pack()

        elif winner == 0:  # Tie
            wroot = tk.Tk()
            self.set_wroot(wroot)
            wroot.geometry('100x100')
            title = tk.Label(self.wroot, text='Tie!',
                             font=(self.font, 20))
            title.pack(side=tk.TOP)
            b_exit = tk.Button(self.wroot, text='Exit',
                               command=self.exit, font=(self.font, 10))
            b_play_again = tk.Button(self.wroot, text='Play again!',
                                     command=self.play_again,
                                     font=(self.font, 10))
            b_exit.pack()
            b_play_again.pack()
            self.wroot.mainloop()

    def declare_winner(self):
        """
        calls the winner function to finally declare the winner to the players
        """
        winner = self.game.get_winner()
        if winner == 1 or winner == 2 or winner == 0:
            if self.wroot is None:  # only one pop up window will show
                self.winner_window(winner)

    def winning_discs(self):
        """
        marks the winning discs in gold
        """
        C = 15  # constant to decrease disc size
        discs = self.game.win_disc_lst
        for disc in discs:
            r, c = disc[0], disc[1]
            row = SEG_SIZE + r * SEG_SIZE
            col = SEG_SIZE + c * SEG_SIZE
            self.canv.create_oval(col + C, row + C, col + SEG_SIZE - C,
                                  row + SEG_SIZE - C,
                                  fill='gold')
        print(discs)

    def exit(self):
        """
        exits the game(button function)
        """
        self.wroot.destroy()
        self.root.destroy()

    def play_again(self):
        """
        plays again(buttons function) and restarts the roots
        """
        self.wroot.destroy()
        self.root.destroy()
        self.set_game()
        self.set_wroot(None)
        self.set_root(tk.Tk())
        self.start_screen()
        self.game.set_winner(None)



