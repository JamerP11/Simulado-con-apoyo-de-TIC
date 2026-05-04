from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, Asesoria
from reserva import Reserva, registrar_log

def simulacion():
    clientes = []
    reservas = []

    try:
        # Cliente válido
        c1 = Cliente("Juan", "juan@mail.com")
        clientes.append(c1)

        # Cliente inválido
        try:
            Cliente("", "")
        except Exception as e:
            registrar_log(e)

        # Servicios
        s1 = ReservaSala("Sala VIP", 50)
        s2 = AlquilerEquipo("Laptop", 30)
        s3 = Asesoria("Consultoría", 100)

        # Reserva válida
        r1 = Reserva(c1, s1, 2)
        print("Costo reserva sala:", r1.procesar())
        reservas.append(r1)

        # Reserva inválida
        try:
            Reserva(c1, s2, -1)
        except Exception as e:
            registrar_log(e)

        # Otra reserva válida
        r3 = Reserva(c1, s3, 3)
        print("Costo asesoría:", r3.procesar())

    except Exception as e:
        registrar_log(e)
    finally:
        print("Simulación finalizada")

if __name__ == "__main__":
    simulacion()
