import numpy as np
import random
import game.calculations as c


class Rules(object):

    def __init__(self):
        self.board = np.zeros((4,4))

    def init(self):
        # create an empty matrix
        # pick random idx
        idx1 = random.randint(0,15)
        idx2 = random.randint(0,15)
        while idx1 == idx2:
            idx2 = random.randint(0,15)
        # assign either 2 or 4 to generated idx
        val1 = random.choice([2,4])
        val2 = random.choice([2,4])
        # assign values
        self.board = self.board.flatten()
        self.board[idx1] = val1
        self.board[idx2] = val2
        # print board
        self.print_board()


    def left(self):
        # move everything >0 to the left
        self.board = c.move_left(self.board)
        self.board = c.sum_rows(self.board, 'left')
        self.board = c.move_left(self.board)
        self.board = c.add_tile(self.board)

    def right(self):
        self.board = c.move_right(self.board)
        self.board = c.sum_rows(self.board, 'right')
        self.board = c.move_right(self.board)
        self.board = c.add_tile(self.board)

    def up(self):
        self.board = c.move_up(self.board)
        self.board = c.sum_columns(self.board, 'up')
        self.board = c.move_up(self.board)
        self.board = c.add_tile(self.board)

    def down(self):
        self.board = c.move_down(self.board)
        self.board = c.sum_columns(self.board, 'down')
        self.board = c.move_down(self.board)
        self.board = c.add_tile(self.board)

    def print_board(self):
        print (self.board.reshape((4,4)))
        print ('\r')