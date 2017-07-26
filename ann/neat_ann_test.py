import pickle
from neat import population, nn
from game import calculations as c
from game.rules import Rules
import numpy as np

ann_filename = "../game/winner_net_left_1024_max_cell"


winner = pickle.load( open( ann_filename, "rb" ) )
winner_net = nn.create_recurrent_phenotype(winner)

r = Rules()
r.init()

previous_board = np.zeros((4,4))

while not np.array_equal(previous_board, r.board):
    output = winner_net.activate(c.normalize_board(r.board.flatten()))

    previous_board = r.board
    output = [1 if (output[0] > 0) else 0, 1 if output[1] > 0 else 0]
    # print (output)
    output = c.decode_output(r.board, output)
    if output == 'left':
        r.left()
    elif output == 'right':
        r.right()
    elif output == 'up':
        r.up()
    elif output == 'down':
        r.down()
    else:
        break

    r.print_board()
#output = winner_net.serial_activate(c.normalize_board(self.rules.board.flatten()))
