import os
from os import system
import random
from random import randint

class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, saldo_cuenta=0):
        super().__init__(nombre, apellido) 
        self.numero_cuenta = numero_cuenta
        self.saldo_cuenta = saldo_cuenta
    
    def __str__(self):
        return f"Eres {self.nombre + ' ' + self.apellido}\ntu número de cuenta es {self.numero_cuenta} y tienes un balance de {self.saldo_cuenta}."
    
    def depositar(self, monto):
        self.saldo_cuenta += monto
        print("Transacción d emonto aceptada")
    
    def retirar(self, monto_retiro):
        if monto_retiro <= self.saldo_cuenta:
            self.saldo_cuenta -= monto_retiro
            print (f"Su retiro fue exito")
            print (f"Retiraste {monto_retiro}")
            print (f"su saldo actual es de {self.saldo_cuenta} $ ")
        else:
            print("El retiro no se efectúo") 
            print("No tiene suficiente dinero para el monto solicitado a retirar")
            print(f"Monto a retirar {monto_retiro} saldo en cuenta {self.saldo_cuenta} $.")

def crear_cliente():
    nombre = input("ingrese su nombre: ")
    apellido = input("ingresa tu apellido: ")
    numero_cuenta = randint(1000,9999)
    nuevo_cliente = Cliente(nombre, apellido, numero_cuenta)

    return nuevo_cliente


def inicio():
    #os.system('cls')
    mi_cliente = crear_cliente()
    print(mi_cliente)

    transa = False

    while not transa:
        print("*"*50)
        print("Bienvenido a su banco 123")
        print("*"*50 + "\n")
        print("""Qué transacción desea hacer:
            [1] - Depositar
            [2] - Retirar
            [3] - salir
            """)
        menu = int(input())

        if menu == 1:
            # Depositar
            monto = int(input("Monto a depositar: "))
            mi_cliente.depositar(monto)
            
        elif menu == 2: 
            # Retirar
            monto_retiro = int(input("Monto a retirar: "))
            mi_cliente.retirar(monto_retiro)
            
        
        elif menu == 3: 
            transa = True
        
        print(mi_cliente)

inicio()
        






    

