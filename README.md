# Simulado-con-apoyo-de-TIC
Aprendizaje basado en problemas.
from abc import ABC, abstractmethod
import datetime

# ================== LOGS ==================
def registrar_log(mensaje):
    with open("logs.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} - {mensaje}\n")

# ================== EXCEPCIONES ==================
class ErrorSistema(Exception):
    pass

class ErrorValidacion(ErrorSistema):
    pass

class ErrorReserva(ErrorSistema):
    pass

# ================== CLASE ABSTRACTA ==================
class Entidad(ABC):
    @abstractmethod
    def mostrar_info(self):
        pass

# ================== CLIENTE ==================
class Cliente(Entidad):
    def __init__(self, nombre, email):
        if not nombre or not email:
            raise ErrorValidacion("Datos del cliente inválidos")
        self.__nombre = nombre
        self.__email = email

    def mostrar_info(self):
        return f"Cliente: {self.__nombre} - {self.__email}"

# ================== SERVICIO ABSTRACTO ==================
class Servicio(ABC):
    def __init__(self, nombre, precio_base):
        self.nombre = nombre
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def descripcion(self):
        pass

# ================== SERVICIOS ==================
class ReservaSala(Servicio):
    def calcular_costo(self, horas=1):
        return self.precio_base * horas

    def descripcion(self):
        return "Reserva de sala por horas"

class AlquilerEquipo(Servicio):
    def calcular_costo(self, dias=1):
        return self.precio_base * dias

    def descripcion(self):
        return "Alquiler de equipos tecnológicos"

class Asesoria(Servicio):
    def calcular_costo(self, horas=1):
        return self.precio_base * horas * 1.2

    def descripcion(self):
        return "Asesoría especializada"

# ================== RESERVA ==================
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

# ================== SIMULACIÓN ==================
clientes = []
reservas = []

def simulacion():
    try:
        # Cliente válido
        c1 = Cliente("Juan", "juan@mail.com")
        clientes.append(c1)

        # Cliente inválido
        try:
            c2 = Cliente("", "")
        except Exception as e:
            registrar_log(e)

        # Servicios
        s1 = ReservaSala("Sala VIP", 50)
        s2 = AlquilerEquipo("Laptop", 30)
        s3 = Asesoria("Consultoría", 100)

        # Reserva válida
        r1 = Reserva(c1, s1, 2)
        costo = r1.procesar()
        reservas.append(r1)
        print("Reserva exitosa. Costo:", costo)

        # Reserva inválida
        try:
            r2 = Reserva(c1, s2, -1)
        except Exception as e:
            registrar_log(e)

        # Otra reserva
        r3 = Reserva(c1, s3, 3)
        print("Costo asesoría:", r3.procesar())

    except Exception as e:
        registrar_log(e)
    finally:
        print("Simulación finalizada")

# Ejecutar
simulacion()
