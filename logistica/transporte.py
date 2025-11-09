from abc import ABC, abstractmethod

# ----- Producto abstracto -----
class Transporte(ABC):
    """Interfaz común para todos los transportes."""

    @abstractmethod
    def entregar(self):
        pass

    @abstractmethod
    def obtener_costo(self):
        pass

    @abstractmethod
    def obtener_tiempo(self):
        pass


# ----- Productos concretos -----
class Camion(Transporte):
    def entregar(self):
        return "Camion"

    def obtener_costo(self):
        return 50000

    def obtener_tiempo(self):
        return "2 días"


class Barco(Transporte):
    def entregar(self):
        return "Barco"

    def obtener_costo(self):
        return 120000

    def obtener_tiempo(self):
        return "7 días"


class Avion(Transporte):
    def entregar(self):
        return "Avion"

    def obtener_costo(self):
        return 200000

    def obtener_tiempo(self):
        return "12 horas"
