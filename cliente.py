from abc import ABC, abstractmethod
from excepciones import ErrorValidacion

class Entidad(ABC):
    @abstractmethod
    def mostrar_info(self):
        pass

class Cliente(Entidad):
    def __init__(self, nombre, email):
        if not nombre or not email:
            raise ErrorValidacion("Datos del cliente inválidos")
        self.__nombre = nombre
        self.__email = email

    def mostrar_info(self):
        return f"Cliente: {self.__nombre} - {self.__email}"
