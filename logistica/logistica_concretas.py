from .logistica_base import Logistica
from .transporte import Camion, Barco, Avion

class LogisticaTerrestre(Logistica):
    def crear_transporte(self):
        return Camion()

class LogisticaMaritima(Logistica):
    def crear_transporte(self):
        return Barco()

class LogisticaAerea(Logistica):
    def crear_transporte(self):
        return Avion()
