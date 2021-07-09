import pytest
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from piezas.Caballo import Caballo
from tablero.Posicion import Posicion

@pytest.mark.xfail(raises=Exception)
def test_caballo_fila_erronea():
        pos = Posicion(10,"g")
        cab = Caballo(pos, False)
