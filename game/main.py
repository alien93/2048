from game.rules import Rules

if __name__ == "__main__":
    r = Rules()
    r.init()

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
