import numpy as np
from player import Player

class ConnectFour:
    def __init__(self, boardShape=(6,7)):
        self._boardShape = boardShape
        self._board = np.zeros(boardShape)
        self._player_A = Player('red', +1, self)
        self._player_B = Player('blue', -1, self)
        self._maxIter = boardShape[0] * boardShape[1]
        self._nbRw = boardShape[0]
        self._nbCl = boardShape[1]

    def freePositions(self):
        free = []   
        for j in range(0, self._nbCl):
            free_rows = []
            for i in range(0, self._nbRw):
                if self._board[i,j] == .0:
                    free_rows.append(i)
            if len(free_rows) != 0:
                free.append((min(free_rows),j)) 
        return free

    def placeDisc(self, pos, player):
        if pos not in self.freePositions():
            raise Exception('{0} is not free!'.format(pos))
        else:
            self._board[pos[0],pos[1]] = player.Sign



    def finished(self):
        if len(self.freePositions()) == 0 or self._player_A.HasWon or self._player_B.HasWon:
            return True
        else:
            return False  

    def play(self):
        var = self._nbRw
        
        for i in range(0, self._maxIter):
            if not self.finished():
                self._player_A.makeMove()
            if not self.finished():
                self._player_B.makeMove()

    def four(self):
        pass

connect_four = ConnectFour()
connect_four.play()





    