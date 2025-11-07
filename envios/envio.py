class Envio:
    """Representa un envío con sus datos."""
    def __init__(self, id_envio, tipo, destino, estado, costo, tiempo):
        self.id_envio = id_envio
        self.tipo = tipo
        self.destino = destino
        self.estado = estado
        self.costo = costo
        self.tiempo = tiempo
