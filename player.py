class Player:
    @property
    def HasWon(self):
        return self._hasWon

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

    def dropDisc(self, pos):
        self._game.placeDisc(pos)

    def tryWinNow(self):
        free_pos = self._game.freePositions()
        