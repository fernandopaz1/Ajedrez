class Posicion:
    dic_col = {"a" : 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
    dic_col_reverse = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h"}
    def __init__(self, fila, columna):
        if fila<=0 or fila>8:
            raise Exception("Filas fuera de rango")
        if columna.toLower()<"a" or columna.toLower()>"h": 
            raise Exception("Columna fuera de rango")
        self.__fila= fila
        self.__columna=Posicion.dic_col.get(columna)
    
    def __str__(self):
        return Posicion.dic_col.get(self.columna) + self.fila

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