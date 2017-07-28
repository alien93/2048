from __future__ import division
import pickle
from game.rules import Rules
from neat import population, nn
import numpy as np
from game import calculations as c
import copy
from sklearn.preprocessing import normalize

class Neat(object):

    def __init__(self):
        self.rules = Rules()
        self.rules.init()
        self.max_fitness = 0
        self.max_sum = 0
        self.max_cell = 0



    def evaluate_genomes(self, genomes):
        for g in genomes:
            # net = nn.create_recurrent_phenotype(g)
            net = nn.create_feed_forward_phenotype(g)
            # calculate fitness function
            score = 0
            for _ in range(10):
                self.rules.init()
                previous_board = np.zeros((4,4))
                for _ in range(10):
                    while not np.array_equal(previous_board, self.rules.board.reshape((4,4))):
                        c.find_legal_moves(self.rules.board)
                        previous_board = self.rules.board.reshape((4,4))
                        output = net.serial_activate(c.normalize_board(self.rules.board.flatten()))
                        output = [1 if (output[0] > 0) else 0,1 if output[1] > 0 else 0]
                        # print (output)
                        output = c.decode_output(self.rules.board, output)
                        if output == 'left':
                            score += self.rules.left()
                        elif output == 'right':
                            score += self.rules.right()
                        elif output == 'up':
                            score += self.rules.up()
                        elif output == 'down':
                            score += self.rules.down()
                        else:
                            break
                        # print ("Score: ", score)
                        # print (output)
                        # self.rules.print_board()
            #sum_points = np.sum(self.rules.board)
            #board = self.rules.board.reshape((4,4))
            #sum_left_corner = board[2][0] + board[2][1] + board[3][0] + board[3][1]
            #value = np.amax(self.rules.board)# + sum_left_corner
            # value = sum_points + sum_left_corner
            g.fitness = score/100               # / (1 + abs(value))
            if g.fitness > self.max_fitness:
                self.max_fitness = g.fitness
            #if sum_points > self.max_sum:
            #    self.max_sum = sum_points
            if np.amax(self.rules.board) > self.max_cell:
                self.max_cell = np.amax(self.rules.board)

            print ("#################################################")
            print ("Fitness:", g.fitness)
            print("Maximum fitness: ", self.max_fitness)
            #print("Maximum sum: ", self.max_sum)
            print("Maximum cell: ", self.max_cell)
            print("#################################################")


    def run(self):
        # Load the config file
        pop = population.Population('../ann/rnn_config')
        # Create parallel evaluator, 4 threads
        # Evaluate genomes
        pop.run(self.evaluate_genomes, 50)

        print('Number of evaluations: {0}'.format(pop.total_evaluations))

        # Display the most fit genome.
        winner = pop.statistics.best_genome()
        print('\nBest genome:\n{!s}'.format(winner))

        print ("Maximum fitness: ", self.max_fitness)
        print ("Maximum sum: ", self.max_sum)
        print ("Maximum cell: " , self.max_cell)


        # Verify network output against training data.

        #print('\nOutput:')
        #winner_net = nn.create_feed_forward_phenotype(winner)
        #winner_net = nn.create_feed_forward_phenotype(winner)

        #save winning net
        with open('winner_net', 'wb') as f:
            pickle.dump(winner, f)



