import random as rd

class Player:
    @property
    def HasWon(self):
        return self._hasWon

    @property
    def Sign(self):
        return self._sign

    def __init__(self, disc_color, sign, game):
        self._disc_color = disc_color
        self._memory = []
        self._hasWon = False
        self._game = game
        self._sign = sign

    def makeMove(self):
        self.tryWinNow()

        if len(self._memory) == 0:
            pass
        else:
            pass

    def tryWinNow(self):
        free_positions = self._game.freePositions()

        for free_position in free_positions:
            self._game.placeDisc(free_position, self)

            if self._game.four() == self._sign:
                return
            else:
                self._game.removeDisc(free_position)

        rnd_pos = rd.randint(0, len(free_positions))
        self._game.placeDisc(free_positions[rnd_pos], self)

        
        