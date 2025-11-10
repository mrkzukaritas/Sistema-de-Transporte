from logistica.logistica_concretas import LogisticaTerrestre, LogisticaMaritima, LogisticaAerea
from .envio import Envio

class EnvioManager:
    """Gestor de envíos con CRUD básico."""
    def __init__(self):
        self.envios = []
        self.contador = 1

    def crear_envio(self, tipo, destino):
        """Crea un envío nuevo usando el Factory Method."""
        if tipo == "terrestre":
            logistica = LogisticaTerrestre()
        elif tipo == "maritima":
            logistica = LogisticaMaritima()
        elif tipo == "aerea":
            logistica = LogisticaAerea()
        else:
            print("Tipo de envío no válido.")
            return

        transporte = logistica.crear_transporte()
        envio = Envio(
            self.contador,
            tipo,
            destino,
            "Pendiente",
            transporte.obtener_costo(),
            transporte.obtener_tiempo()
        )
        self.envios.append(envio)
        print(f"Envío #{self.contador} creado correctamente.")
        self.contador += 1

    def listar_envios(self):
        if not self.envios:
            print("No hay envíos registrados.")
            return
        for e in self.envios:
            print(f"ID: {e.id_envio} | Tipo: {e.tipo} | Destino: {e.destino} | "
                  f"Estado: {e.estado} | Costo: ${e.costo:,} | Tiempo: {e.tiempo}")

    def actualizar_envio(self, id_envio, nuevo_estado):
        for e in self.envios:
            if e.id_envio == id_envio:
                e.estado = nuevo_estado
                print("Envío actualizado correctamente.")
                return
        print("Envío no encontrado.")

    def eliminar_envio(self, id_envio):
        for e in self.envios:
            if e.id_envio == id_envio:
                self.envios.remove(e)
                print("Envío eliminado correctamente.")
                return
        print("Envío no encontrado.")
