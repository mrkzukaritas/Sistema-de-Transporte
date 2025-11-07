from abc import ABC, abstractmethod

class Logistica(ABC):
    """Clase base que define el Factory Method."""

    @abstractmethod
    def crear_transporte(self):
        pass

    def planificar_entrega(self):
        """Usa el transporte creado para planificar la entrega."""
        transporte = self.crear_transporte()
        print(transporte.entregar())
        print(f"Costo estimado: ${transporte.obtener_costo():,}")
        print(f"Tiempo estimado: {transporte.obtener_tiempo()}")
