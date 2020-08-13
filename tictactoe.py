"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # raise NotImplementedError
    X_count = 0
    O_count = 0
    for i in board :
        for j in i :
            if j == 'X':
                X_count += 1 
            elif j == 'O':
                O_count += 1
    if X_count == O_count :
        return 'X'
    return 'O'


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # raise NotImplementedError
    possibleSet = set()
    # turn = player(board)
    for i in range(len(board)) :
        for j in range(len(board[i])):
            if board[i][j] == None :
                newBoard = (i,j)
                possibleSet.add(newBoard)
    return possibleSet


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    turn = player(board)
    # print(turn)
    board[action[0]][action[1]] = turn
    # board[1][1] = 'O'
    return board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    possiblewin = [[[0,0],[1,1],[2,2]],[[0,0],[0,1],[0,2]],
    [[1,0],[1,1],[1,2]],
    [[2,0],[2,1],[2,2]],
    [[0,0],[1,0],[2,0]],
    [[0,1],[1,1],[2,1]],
    [[0,2],[1,2],[2,2]],
    [[0,2],[1,1],[2,0]]]
    for i in possiblewin :
        if board[i[0][0]][i[0][1]] is not None and board[i[0][0]][i[0][1]] == board[i[1][0]][i[1][1]] and board[i[0][0]][i[0][1]] == board[i[2][0]][i[2][1]] :
            return board[i[0][0]][i[0][1]]
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    win = winner(board)
    if win is not None :
        return True 
    for i in board :
        for j in i :
            if j is None :
                return False
    return True


def utilityX(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == 'X' :
        return 1
    elif winner(board) == 'O':
        return -1 
    return 0
def utilityO(board):
    if winner(board) == 'X' :
        return -1
    elif winner(board) == 'O':
        return 1 
    return 0

def minmaxhelper(board,isMaximising):
    if terminal(board) :
        return utilityX(board),()
    if isMaximising :
        bestVal = -10
        validMoves = actions(board)
        bestmove = ()
        for i in validMoves:
            newBoard = result(board,i)
            val,move = minmaxhelper(newBoard,False)
            newBoard[i[0]][i[1]] = None
            if bestVal <= val :
                bestVal = val 
                bestmove = i  
            
        return bestVal,bestmove
    else:
        bestVal = 10
        validMoves = actions(board)
        bestmove = ()
        for i in validMoves:
            newBoard = result(board,i)
            val,move = minmaxhelper(newBoard,True)
            newBoard[i[0]][i[1]] = None
            if bestVal >= val :
                bestVal = val 
                bestmove = i  
        return bestVal,bestmove

def minmaxhelperO(board,isMaximising):
    if terminal(board) :
        return utilityO(board),()
    if isMaximising :
        bestVal = -10
        validMoves = actions(board)
        bestmove = ()
        for i in validMoves:
            newBoard = result(board,i)
            val,move = minmaxhelperO(newBoard,False)
            newBoard[i[0]][i[1]] = None
            if bestVal <= val :
                bestVal = val 
                bestmove = i  
            
        return bestVal,bestmove
    else:
        bestVal = 10
        validMoves = actions(board)
        bestmove = ()
        for i in validMoves:
            newBoard = result(board,i)
            val,move = minmaxhelperO(newBoard,True)
            newBoard[i[0]][i[1]] = None
            if bestVal >= val :
                bestVal = val 
                bestmove = i  
        return bestVal,bestmove

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    turn = player(board)
    if turn == 'O':
        val,arr = minmaxhelper(board,False)
        return arr
    val,arr = minmaxhelperO(board,False)
    return arr

