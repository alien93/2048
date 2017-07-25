import numpy as np
import random

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
    if (side == 'left'):
        for i in range(board.shape[0]):  # rows
            for j in range(board.shape[1]):  # cols
                if j < board.shape[1] - 1 and board[i][j] == board[i][j + 1] and board[i][j] != 0:
                    board[i][j + 1] += board[i][j]
                    board[i][j] = 0
    elif (side == 'right'):
        for i in range(board.shape[0]-1,-1,-1):  # rows
            for j in range(board.shape[1]-1,-1,-1):  # cols
                if j < board.shape[1] - 1 and board[i][j] == board[i][j + 1] and board[i][j] != 0:
                    board[i][j + 1] += board[i][j]
                    board[i][j] = 0

    return board

def sum_columns(board, side):
    if (side == 'up'):
        for i in range(board.shape[0]):
            for j in range(board.shape[1]):
                if i < board.shape[0] - 1 and board[i][j] == board[i + 1][j]:
                    board[i][j] += board[i + 1][j]
                    board[i + 1][j] = 0
    elif (side == 'down'):
        for i in range(board.shape[0]-1,-1,-1):
            for j in range(board.shape[1]-1,-1,-1):
                if i < board.shape[0] - 1 and board[i][j] == board[i + 1][j]:
                    board[i][j] += board[i + 1][j]
                    board[i + 1][j] = 0

    return board

def add_tile(board):
    board = board.flatten()
    zeros_idx = np.where(board == 0)[0]
    if len(zeros_idx) > 0:
        idx = random.choice(zeros_idx)
        board[idx] = random.choice([2,4])
        board = board.reshape((4,4))
    return board




