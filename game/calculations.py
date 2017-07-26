import numpy as np
import random
import copy

def move_left(board):
    mask = board > 0
    mask = mask.reshape((4, 4))
    justified_mask = np.sort(mask, 1)[:, ::-1]
    out = np.zeros_like(board).reshape((4, 4))
    out[justified_mask] = board.reshape((4, 4))[mask]
    return out

def move_right(board):
    mask = board > 0
    mask = mask.reshape((4, 4))
    justified_mask = np.sort(mask, 1)
    out = np.zeros_like(board).reshape((4, 4))
    out[justified_mask] = board.reshape((4, 4))[mask]
    return out

def move_down(board):
    board_changed = True
    board = board.reshape((4,4))
    while board_changed:
        board_changed = False
        for i in (range(board.shape[0]-1, -1, -1)):         # rows
            for j in (range(board.shape[1]-1, -1,-1)):     # cols
                if i < board.shape[0] - 1 and board[i][j] > 0 and board[i + 1][j] == 0:
                    board[i + 1][j] = board[i][j]
                    board[i][j] = 0
                    board_changed = True
    return board


def move_up(board):
    board_changed = True
    board = board.reshape((4, 4))
    while board_changed:
        board_changed = False
        for i in (range(board.shape[0])):  # rows
            for j in (range(board.shape[1])):  # cols
                if i < board.shape[0] - 1 and board[i + 1][j] > 0 and board[i][j] == 0:
                    board[i][j] = board[i+1][j]
                    board[i + 1][j] = 0
                    board_changed = True
    return board


def sum_rows(board, side):
    score = 0
    if (side == 'left'):
        for i in range(board.shape[0]):  # rows
            for j in range(board.shape[1]):  # cols
                if j < board.shape[1] - 1 and board[i][j] == board[i][j + 1] and board[i][j] != 0:
                    board[i][j + 1] += board[i][j]
                    score += 2*board[i][j]
                    board[i][j] = 0
    elif (side == 'right'):
        for i in range(board.shape[0]-1,-1,-1):  # rows
            for j in range(board.shape[1]-1,-1,-1):  # cols
                if j < board.shape[1] - 1 and board[i][j] == board[i][j + 1] and board[i][j] != 0:
                    board[i][j + 1] += board[i][j]
                    score += 2*board[i][j]
                    board[i][j] = 0

    return board, score

def sum_columns(board, side):
    score = 0
    if (side == 'up'):
        for i in range(board.shape[0]):
            for j in range(board.shape[1]):
                if i < board.shape[0] - 1 and board[i][j] == board[i + 1][j]:
                    board[i][j] += board[i + 1][j]
                    score += 2*board[i + 1][j]
                    board[i + 1][j] = 0
    elif (side == 'down'):
        for i in range(board.shape[0]-1,-1,-1):
            for j in range(board.shape[1]-1,-1,-1):
                if i < board.shape[0] - 1 and board[i][j] == board[i + 1][j]:
                    board[i][j] += board[i + 1][j]
                    score += 2*board[i + 1][j]
                    board[i + 1][j] = 0

    return board, score

def add_tile(board):
    board = board.flatten()
    zeros_idx = np.where(board == 0)[0]
    if len(zeros_idx) > 0:
        idx = random.choice(zeros_idx)
        board[idx] = random.choice([2,4])
        board = board.reshape((4,4))
    return board


def decode_output(board, output):
    legal_moves = find_legal_moves(board)
    # if all moves are illegal
    if all(v == 0 for v in legal_moves.values()):
        return 'illegal'
    legal = []
    for direction, state in legal_moves.items():
        if state == 1:
            legal.append(direction)
    if (len(legal) == 4):
        if output == [0,0]:
            output = legal[0]
        elif output == [0,1]:
            output = legal[1]
        elif output == [1,0]:
            output = legal[2]
        elif output == [1,1]:
            output = legal[3]
    elif(len(legal) == 3):
        if output == [0,0]:
            output = legal[0]
        elif output == [0,1]:
            output = legal[1]
        elif output == [1,0] or output == [1,1]:
            output = legal[2]
    elif (len(legal) == 2):
        if output == [0, 0] or output == [0, 1]:
            output = legal[0]
        elif output == [1, 0] or output == [1, 1]:
            output = legal[1]
    elif (len(legal) == 1):
        output = legal[0]
    return output

def find_legal_moves(board):
    # if row contains zero or two elements
    # that are next to each other are the same
    # left and right is legal
    legal_moves = {'left':0, 'right':0, 'up':0, 'down':0}
    board = board.reshape((4,4))
    test_board = board.copy()
    #test left
    test_board = move_left(test_board)
    test_board = sum_rows(test_board, 'left')[0]
    test_board = move_left(test_board)
    if not np.array_equal(test_board, board):
        legal_moves['left'] = 1
    test_board = board.copy()
    # test right
    test_board = move_right(test_board)
    test_board = sum_rows(test_board, 'right')[0]
    test_board = move_right(test_board)
    if not np.array_equal(test_board, board):
        legal_moves['right'] = 1
    test_board = board.copy()
    # test up
    test_board = move_up(test_board)
    test_board = sum_columns(test_board, 'up')[0]
    test_board = move_up(test_board)
    if not np.array_equal(test_board, board):
        legal_moves['up'] = 1
    test_board = board.copy()
    # test down
    test_board = move_down(test_board)
    test_board = sum_columns(test_board, 'down')[0]
    test_board = move_down(test_board)
    if not np.array_equal(test_board, board):
        legal_moves['down'] = 1
    # print (legal_moves)
    return legal_moves

def normalize_board(board):
    board[board==0] = 0.0001
    board = np.log2(board)
    max_val = np.max(board)
    return board/max_val


