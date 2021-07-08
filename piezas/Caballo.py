from . import Color, Pieza

class Caballo(Color, Pieza):
    def __init__(self,color, position):
        self.__color = Color(color)
        self.__position = Pieza(position)

    