class Posicion:
    def __init__(self, fila, columna):
        self.__fila= fila
        self.__columna=columna
    
    def __str__(self):
        return self.__fila+self.__columna

    @property
    def fila(self):
        return self.__fila

    @property
    def columna(self):
        return self.__columna


    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.fila() == other.fila() and self.columna() == other.columna()
    
    def __hash__(self):
        return hash(self.fila()) + hash(self.columna())