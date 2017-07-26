from game.rules import Rules
from ann import neat_ann

if __name__ == "__main__":
    n = neat_ann.Neat()
    n.run()

    """
    while True:

        key = input()
        if (key.lower() == 'a'):
            r.left()
        elif (key.lower() == 's'):
            r.down()
        elif (key.lower() == 'd'):
            r.right()
        elif (key.lower() == 'w'):
            r.up()
        r.print_board()
    """