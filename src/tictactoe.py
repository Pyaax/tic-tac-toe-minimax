"""
Tic Tac Toe Player
"""
import math
import copy


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
    x = 0
    o = 0
    
    for row in range(3):
        for column in range(3):
            if board[row][column] == "X":
                x += 1
            if board[row][column] == "O":
                o += 1

    
    if x == 0 and o == 0:
        return "X"
    if x == o:
        return "X"
    else:
        return "O" 


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    for row in range(3):
        for column in range(3):
            if board[row][column] == EMPTY:
                possible_actions.add((row, column))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Check if the action is valid
    valid_action = False
    for t_action in actions(board):
        if t_action == action:
            valid_action = True
    
    if valid_action == False:
        raise ValueError  
    
    # Makes a copy of the whole board in its current state
    resulting_board = copy.deepcopy(board)

    if player(board) == "X":
        resulting_board[action[0]][action[1]] = "X"
    if player(board) == "O":
        resulting_board[action[0]][action[1]] = "O"

    return resulting_board
    

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Check horizontally for a winner
    if board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] != EMPTY:
        return board[0][0]
    
    if board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] != EMPTY:
        return board[1][0]
    
    if board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] != EMPTY:
        return board[2][0]

    # Check vertically for a winner
    if board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] != EMPTY:
        return board[0][0]

    if board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] != EMPTY:
        return board[0][1]

    if board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] != EMPTY:
        return board[0][2]

    # Check diagonally for a winner
    if board[0][0] == board [1][1] and board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]

    if board[0][2] == board [1][1] and board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) != None:
        return True

    # Keeps track of the state of the board. If the board is a terminal board it will remain true.
    terminal = True
    
    # Looks for empty fields on the board. If an empty field is found it changes the terminal variable to false.
    for row in range(3):
        for column in range(3):
            if board[row][column] == EMPTY:
                terminal = False

    return terminal 


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1
    if winner(board) == "O":
        return -1

    return 0


def min_value(board):
    """
    Returns the best action for the player who tries to minimize the value
    """
    if terminal(board):
        return utility(board), None

    v = +math.inf
    best_choice = None
    
    for action in actions(board):
        
        v_tmp, choice = max_value(result(board, action))
        if v_tmp < v:
            v = v_tmp
            best_choice = action

            if v == -1:
                return v, best_choice
    
    return v, best_choice


def max_value(board):
    """
    Returns the best action for the player who tries to maximize the value
    """
    if terminal(board):
        return utility(board), None

    v = -math.inf
    best_choice = None
    
    for action in actions(board):
        
        v_tmp, choice = min_value(result(board, action))
        if v_tmp > v:
            v = v_tmp
            best_choice = action

            if v == 1:
                return v, best_choice
    
    return v, best_choice


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    if player(board) == "X":
        v, best_choice = max_value(board)
        return best_choice

    if player(board) == "O":
        v, best_choice = min_value(board)
        return best_choice          
            
