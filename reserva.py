import datetime
from excepciones import ErrorReserva

def registrar_log(mensaje):
    with open("logs.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} - {mensaje}\n")

class Reserva:
    def __init__(self, cliente, servicio, duracion):
        if duracion <= 0:
            raise ErrorReserva("Duración inválida")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):
        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"

    def procesar(self):
        try:
            costo = self.servicio.calcular_costo(self.duracion)
            self.confirmar()
            return costo
        except Exception as e:
            registrar_log(str(e))
            raise ErrorReserva("Error al procesar reserva") from e
