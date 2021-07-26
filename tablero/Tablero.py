from . import Posicion


class Tablero:
    def __init__(self):
        self.__tablero = {}

    @property
    def tablero(self):
        return self.__tablero

    def agregar(self, pieza, posicion):
        if self.tablero[posicion] is not None:
            self.tablero[posicion] = pieza
            pieza.set_position(posicion)

    def quitar(self, posicion):
        self.tablero[posicion] = None

    def mover(self, pieza, posicion):
        if pieza.puede_moverse_a(posicion):
            aux = self.pieza_en(posicion)
            if aux is None or not pieza.mismo_color(aux):
                self.quitar(posicion)
                self.agregar(pieza, posicion)

    def pieza_en(self, posicion):
        return self.tablero.get(posicion, None)


if __name__ == '__main__':
    print("Este es el tablero")

