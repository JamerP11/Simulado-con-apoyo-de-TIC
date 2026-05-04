from abc import ABC, abstractmethod

class Servicio(ABC):
    def __init__(self, nombre, precio_base):
        self.nombre = nombre
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self, tiempo):
        pass

    @abstractmethod
    def descripcion(self):
        pass

class ReservaSala(Servicio):
    def calcular_costo(self, horas=1):
        return self.precio_base * horas

    def descripcion(self):
        return "Reserva de sala por horas"

class AlquilerEquipo(Servicio):
    def calcular_costo(self, dias=1):
        return self.precio_base * dias

    def descripcion(self):
        return "Alquiler de equipos"

class Asesoria(Servicio):
    def calcular_costo(self, horas=1):
        return self.precio_base * horas * 1.2

    def descripcion(self):
        return "Asesoría especializada"
