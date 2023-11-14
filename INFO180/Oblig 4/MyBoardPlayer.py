'''
Class that represent the features and methods for a Simple Computer Board game player
 Programmed by Bjørnar Tessem, Sept-Oct 2022
'''

from Board import CROSS, RING, EMPTY
import Board
from BoardComputerPlayer import BoardComputerPlayer


class MyBoardPlayer(BoardComputerPlayer):
    ADVANTAGE_PER_PIECE = 1
    def __init__(self, the_mark):
        '''
        Constructor
        :param compatibility_score_set:
        '''
        super(MyBoardPlayer, self).__init__(the_mark)
        self.name = "Complex"

    def evaluate_game_status(self, a_board):
        max_cross_row = 0
        max_ring_row = Board.GAMESIZE - 1
        Xadvantage = 0
        for i in range(Board.GAMESIZE):
            for j in range(Board.GAMESIZE):

                if a_board.the_grid[i][j] == CROSS:
                    if i > max_cross_row:
                        max_cross_row = i
                    if self.can_be_hit(a_board, i, j, -1):
                        Xadvantage += MyBoardPlayer.ADVANTAGE_PER_PIECE

                if a_board.the_grid[i][j] == RING:
                    if i < max_ring_row:
                        max_ring_row = i
                    if not self.can_be_hit(a_board, i, j, 1):
                        Xadvantage -= MyBoardPlayer.ADVANTAGE_PER_PIECE

        score = 0
        if self.mark == CROSS:
            score = max_cross_row - (Board.GAMESIZE - 1 - max_ring_row) + Xadvantage
        if self.mark == RING:
            score = (Board.GAMESIZE - 1 - max_ring_row) - max_cross_row - Xadvantage
        return score

    def can_be_hit(self, board, i, j, direction):
        prev_row = i + direction
        next_row = i - direction
        if board.the_grid[i][j] == board.to_play:
            return False
        if i == 0 or i == Board.GAMESIZE - 1:
            return False
        if j == 0 or j == Board.GAMESIZE - 1:
            return False
        if board.the_grid[prev_row][j - 1] == EMPTY and board.the_grid[next_row][j + 1] == board.to_play:
            return True
        if board.the_grid[prev_row][j + 1] == EMPTY and board.the_grid[next_row][j - 1] == board.to_play:
            return True

        return False
