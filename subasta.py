
# ==========================================
# PROYECTO: SISTEMA DE SUBASTAS ONLINE
# ARCHIVO: subasta.py
# ==========================================

from puja import Puja


class Subasta:

    def __init__(self, id_subasta, producto, fecha_inicio, fecha_fin):
        self.__id_subasta = id_subasta
        self.__producto = producto
        self.__fecha_inicio = fecha_inicio
        self.__fecha_fin = fecha_fin
        self.__pujas = []
        self.__activa = True

    def obtener_producto(self):
        return self.__producto

    def obtener_pujas(self):
        return self.__pujas

    def registrar_puja(self, comprador, monto):
        if not self.__activa:
            print("La subasta esta cerrada.")
            return False

        if monto <= self.__producto.obtener_precio():
            print("La puja debe superar el precio inicial.")
            return False

        if self.__pujas and monto <= self.__pujas[-1].obtener_monto():
            print("La puja debe superar la oferta anterior.")
            return False

        if monto > comprador.obtener_saldo():
            print("El comprador no tiene saldo suficiente.")
            return False

        nueva_puja = Puja(len(self.__pujas) + 1, comprador, monto)
        self.__pujas.append(nueva_puja)

        print("Puja registrada correctamente.")
        return True

    def obtener_puja_ganadora(self):
        if not self.__pujas:
            return None

        return max(self.__pujas, key=lambda puja: puja.obtener_monto())

    def cerrar_subasta(self):
        self.__activa = False
        ganadora = self.obtener_puja_ganadora()

        print("Subasta cerrada.")

        if ganadora:
            print("Ganador:", ganadora.obtener_comprador().obtener_nombre())
            print("Oferta ganadora: $", ganadora.obtener_monto())
        else:
            print("No se recibieron pujas.")
