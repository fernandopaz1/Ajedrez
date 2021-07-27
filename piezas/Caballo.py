from tablero import Posicion
from . import Pieza


class Caballo(Pieza):
    def __init__(self, position, color):
        Pieza.__init__(self, position, color)

    def mover(self, position):
        self.set_position(position)

    def calcular_casillas_amenazadas(self):
        amenazadas = []
        amenazadas.append(self.position)
