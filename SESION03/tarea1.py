'''
Tarea para antes de la  próxima clase:
Crear un programa en Python que cree una clase denominada CuentaBancaria. Agregar encapsulamiento y sobrecarga del constructor de clase, asi como los métodos get y set requeridos para gestionar los atributos de dicha clase.
Los atributos de la clase debern ser: __numeroCta, __nombreCliente, __fechaApertura, __saldo.
Agregar metodos para aperturar cuentas, realizar consignaciones y retiros controlados (es decir, no permitir consignaciones negativas, ni retiros superiores al saldo, las aperturas deben exigir un valor inicial mínimo de 100 mil pesos).
Crear un menú para crear objetos y realizar las diversas operaciones referidas.

'''
class CuentaBancaria:
    def __init__(self, numeroCta, nombreCliente, fechaApertura, saldo=100000):
        self.__numeroCta = numeroCta
        self.__nombreCliente = nombreCliente
        self.__fechaApertura = fechaApertura
        self.__saldo = saldo

    def get_numeroCta(self):
        return self.__numeroCta

    def get_nombreCliente(self):
        return self.__nombreCliente

    def get_fechaApertura(self):
        return self.__fechaApertura

    def get_saldo(self):
        return self.__saldo

    def set_numeroCta(self, numeroCta):
        self.__numeroCta = numeroCta

    def set_nombreCliente(self, nombreCliente):
        self.__nombreCliente = nombreCliente

    def set_fechaApertura(self, fechaApertura):
        self.__fechaApertura = fechaApertura

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def aperturar_cuenta(self, saldo_inicial):
        if saldo_inicial >= 100000:
            self.__saldo = saldo_inicial
            print("Cuenta aperturada con éxito.")
        else:
            print("El saldo inicial debe ser al menos 100,000 pesos.")

    def consignar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"Consignación exitosa. Nuevo saldo: {self.__saldo}")
        else:
            print("El monto de la consignación debe ser positivo.")

    def retirar(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
            print(f"Retiro exitoso. Nuevo saldo: {self.__saldo}")
        else:
            print("El monto del retiro es inválido o excede el saldo disponible.")

    def menu():
    cuentas = {}
        while True:
        print("\nMenú de opciones:")
        print("1. Aperturar cuenta")
        print("2. Consignar")
        print("3. Retirar")
        print("4. Consultar saldo")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

    if opcion == "1":
        numeroCta = input("Ingrese el número de cuenta: ")
        nombreCliente = input("Ingrese el nombre del cliente: ")
        fechaApertura = input("Ingrese la fecha de apertura (DD/MM/AAAA): ")
        saldo_inicial = float(input("Ingrese el saldo inicial: "))
        cuenta = CuentaBancaria(numeroCta, nombreCliente, fechaApertura)
        cuenta.aperturar_cuenta(saldo_inicial)
        cuentas[numeroCta] = cuenta

    elif opcion == "2":
        numeroCta = input("Ingrese el número de cuenta: ")
            if numeroCta in cuentas:
                monto = float(input("Ingrese el monto a consignar: "))
                cuentas[numeroCta].consignar(monto)
            else:
                print("Cuenta no encontrada.")

    elif opcion == "3":
        numeroCta = input("Ingrese el número de cuenta: ")
            if numeroCta in cuentas:
                monto = float(input("Ingrese el monto a retirar: "))
                cuentas[numeroCta].retirar(monto)
            else:
                print("Cuenta no encontrada.")

    elif opcion == "4":
        numeroCta = input("Ingrese el número de cuenta: ")
            if numeroCta in cuentas:
                print(f"Saldo actual: {cuentas[numeroCta].get_saldo()}")
            else:
                print("Cuenta no encontrada.")

    elif opcion == "5":
        print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")
menu()
