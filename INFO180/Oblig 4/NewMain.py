'''
 A main file for running the board game with human player
 Programmed by Bjørnar Tessem, Sept-Oct 2022
'''

from PlayBoardGame import PlayBoardGame
from BoardGameTreeNode import BoardGameTreeNode
import Board

# create a game playing object

def playgame():
    complex = 0
    simple = 0
    for k in ['y', 'n']:
        for i in [5, 6, 7]:
            for j in [5, 6, 7]:
                BoardGameTreeNode.MAX_DEPTH = i
                Board.GAMESIZE = j
                game = PlayBoardGame()
                game.select_starter(k)
                while not (game.finished()):
                    game.select_move()
                if game.print_result() == 'Complex':
                    complex += 1
                else:
                    simple += 1
    return f'Complex: {complex}, Simple: {simple}'


score = playgame()
print(score)