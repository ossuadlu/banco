from Classes.Cliente import Cliente
from Classes.Cuenta import Cuenta
#registrar cliente nuevo/crea cuenta

Opcion=1
print("Bancolombia")
print("1. Registrar Cliente")
print("0. Salir")
print("***********************")

while(opcion!=0):
    opcion=int(input("Digita una opcion: "))
    if (opcion==1):
        nombre=input("Digite nombre del usuario: ")
        apellido=input("Digite apellido del usuario: ")
        cedula=input("Digite cedula del usuario: ")
        saldoInicial=0
        numeroCuenta=input("digite el numero: ")

        cuenta= Cuenta(numeroCuenta,numeroCuenta)
        cliente= Cliente(nombre,apellido,cedula,cuenta)
