from abc import abstractmethod

class Pieza():
    def __init__(self, position):
        self.__position = position
        self.__casillas_amenazadas  = []
        pass

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