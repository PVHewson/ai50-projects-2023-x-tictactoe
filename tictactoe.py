"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def deep_copy(arr):
    return copy.deepcopy(arr)

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def emptySquareCount(board):
    """
    Returns the number of empty squares on a board.
    """
    emptySquares = 0
    for row in board:
        for cell in row:
            if cell == EMPTY:
                emptySquares += 1

    return emptySquares

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    player = (O if emptySquareCount(board) % 2 == 0 else X)
    return player    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for col in range(3):
        for row in range(3):
            if board[row][col] == EMPTY:
                actions.append( (row, col) )
    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board[action[0]][action[1]] = player(board)
    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for player in [O, X]:
        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            return player
        if board[0][2] == player and board[1][1] == player and board[2][0] == player:
            return player
        for pos in range(3):
            if board[pos].count(player) == 3:
                return player
            if [row[pos] for row in board].count(player) == 3:
                return player

    return None        


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if emptySquareCount(board) == 0:
        return True
    
    if winner(board)!= None:
        return True
    
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    theWinner = winner(board)
    if theWinner is O:
        return -1
    if theWinner is X:
        return 1
    
    return 0

def minimaxLoop(board):
    """
    Recurses through moves available on a board returning the optimal move and its value.
    """
    localBoard = deep_copy(board)
    options = actions(board)
    if len(options) == 0:
        return None
    best_action = None
    if player(board) is X:
        best_value = -math.inf
    else:
        best_value = math.inf

    for action in options:
        loopBoard = deep_copy(localBoard)
        result(loopBoard, action)
        if  terminal(loopBoard):
            return (action, utility(loopBoard))

        minimaxResult = minimaxLoop(loopBoard)               
        value = minimaxResult[1]
        if (player(localBoard) is X and value > best_value) or (player(localBoard) is O and value < best_value):
            best_value = value
            best_action = action
    
        if (player(localBoard) is X and best_value == 1) or (player(localBoard) is O and best_value == -1):
            break
    
    return (best_action, best_value)
    
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    mmLoop = minimaxLoop(board)
    return mmLoop[0]
