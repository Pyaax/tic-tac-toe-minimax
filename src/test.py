import unittest
import tictactoe as ttt

X = "X"
O = "O"
EMPTY = None

board_0 = [[EMPTY, EMPTY, EMPTY],
          [EMPTY, EMPTY, EMPTY],
          [EMPTY, EMPTY, EMPTY]]

possible_actions_0 = {(0, 0), (0, 1), (1, 2), (2, 1), (1, 1), (2, 0), (0, 2), (2, 2), (1, 0)}


board_1 = [["X", EMPTY, EMPTY],
          [EMPTY, EMPTY, EMPTY],
          [EMPTY, EMPTY, EMPTY]]

possible_actions_1 = {(0, 1), (1, 2), (2, 1), (1, 1), (2, 0), (0, 2), (2, 2), (1, 0)}


board_2 = [["X", EMPTY, EMPTY],
          [EMPTY, EMPTY, EMPTY],
          [EMPTY, "O", EMPTY]]

possible_actions_2 = {(0, 1), (1, 2), (1, 1), (2, 0), (0, 2), (2, 2), (1, 0)}


board_3 = [[ EMPTY, "X",  "O"],
          [  "O",   "X",  "X"],
          [  "X",  EMPTY, "O"]]

possible_actions_3 = {(0, 0), (2, 1)}


board_4 = [[ EMPTY, "X",   "O"],
          [  "O",   EMPTY, "X"],
          [  "X",   EMPTY, "O"]]


board_5 = [[ "O",   EMPTY, "O"],
          [  EMPTY, "X",   EMPTY],
          [  "X",   "X",   EMPTY]]

board_6 = [[ "O",   EMPTY, "O"],
          [  "X",   "X",   EMPTY],
          [  "X",   "O",   "X"]]

possible_actions_4 = {(0, 0), (1, 1), (2, 1)}

# Boards where the winning condition is fulfilled
board_win_horizontally = [["X", "X", "X"],
                         [EMPTY, EMPTY, EMPTY],
                         [EMPTY, EMPTY, EMPTY]]

board_win_vertically  = [[EMPTY, EMPTY, 'O'],
                        [EMPTY, EMPTY, 'O'],
                        [EMPTY, EMPTY, 'O']]

board_win_diagonally =  [["X", EMPTY, EMPTY],
                        [EMPTY, "X", EMPTY],
                        [EMPTY, EMPTY, "X"]]

# Terminal boards with unfulfilled winning condition
board_tie = [['X', 'O', 'X'],
            [ 'O', 'O', 'X'],
            [ 'X', 'X', 'O']]


class TestGameMethods(unittest.TestCase):

    def testPlayer(self):
        self.assertEqual(ttt.player(board_0), 'X')
        self.assertEqual(ttt.player(board_1), 'O')
        self.assertEqual(ttt.player(board_2), 'X')
        self.assertEqual(ttt.player(board_3), 'O')
        self.assertEqual(ttt.player(board_4), 'X')

    def testActions(self):
        self.assertEqual(ttt.actions(board_0), possible_actions_0)
        self.assertEqual(ttt.actions(board_1), possible_actions_1)
        self.assertEqual(ttt.actions(board_2), possible_actions_2)
        self.assertEqual(ttt.actions(board_3), possible_actions_3)
        self.assertEqual(ttt.actions(board_4), possible_actions_4)

    def testResult(self):
        self.assertEqual(ttt.result(board_0, (0, 0)), board_1)
        self.assertEqual(ttt.result(board_1, (2, 1)), board_2)
    
    def testWinner(self):
        self.assertEqual(ttt.winner(board_win_horizontally), 'X')
        self.assertEqual(ttt.winner(board_win_vertically), 'O')
        self.assertEqual(ttt.winner(board_win_diagonally), 'X')
        self.assertEqual(ttt.winner(board_0), None)
        self.assertEqual(ttt.winner(board_1), None)
        self.assertEqual(ttt.winner(board_2), None)
        self.assertEqual(ttt.winner(board_3), None)
        self.assertEqual(ttt.winner(board_4), None)

    def testTerminal(self):
        self.assertEqual(ttt.terminal(board_tie), True)
        self.assertEqual(ttt.terminal(board_win_horizontally), True)
        self.assertEqual(ttt.terminal(board_win_vertically), True)
        self.assertEqual(ttt.terminal(board_win_diagonally), True)
        self.assertEqual(ttt.terminal(board_0), False)
        self.assertEqual(ttt.terminal(board_1), False)
        self.assertEqual(ttt.terminal(board_2), False)
        self.assertEqual(ttt.terminal(board_3), False)
        self.assertEqual(ttt.terminal(board_4), False)

    def testUtility(self):
        self.assertEqual(ttt.utility(board_tie), 0)
        self.assertEqual(ttt.utility(board_win_horizontally), 1)
        self.assertEqual(ttt.utility(board_win_vertically), -1)
        self.assertEqual(ttt.utility(board_win_diagonally), 1)

    def testMinValue(self):
        self.assertEqual(ttt.min_value(board_3), (0, (2, 1)))
        self.assertEqual(ttt.min_value(board_4), (0, (0, 0)))

    def testMaxValue(self):
        self.assertEqual(ttt.max_value(board_3), (1, (0, 0)))
        self.assertEqual(ttt.min_value(board_4), (0, (0, 0)))


    def testMiniMax(self):
        self.assertEqual(ttt.minimax(board_3), (2, 1))
        self.assertEqual(ttt.minimax(board_4), (0, 0))
        self.assertEqual(ttt.minimax(board_5), (0, 1))
        self.assertEqual(ttt.minimax(board_6), (0, 1))

if __name__ == '__main__':
    unittest.main()