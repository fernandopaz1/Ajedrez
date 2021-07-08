from . import Pieza

class Caballo(Pieza):
    def __init__(self, position, color):
        Pieza.__init__(self, position, color)

    def mover(self, position):
        pass

    def calcular_casillas_amenazadas(self):
        pass