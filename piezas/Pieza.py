from abc import abstractmethod
from . import Color
class Pieza(Color):
    def __init__(self, position, color):
        self.__position = position
        self.__color = Color(color)
        self.__casillas_amenazadas  = []
        pass

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @property
    def casillas_amenazadas(self):
        return self.__casillas_amenazadas

    @abstractmethod
    def mover(self, posicion):
        pass
    
    @abstractmethod
    def calcular_casillas_amenazadas(self):
        pass

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.__position == other.__position and self.__color == other

    def __hash__(self):
        return hash(self.color) + hash(self.position)