import os

def funcion1():
    os.system('clear')
    print('IDGS803 - Desarrollo Web Profesional')

def funcion2(nombre):
    print('Hola ', nombre)

def funcion3(num1,num2):
    suma = num1 + num2
    return suma

def main():
    funcion1()
    funcion2('Melchor')
    resultado = funcion3(2,3)
    print('El resultado de las sumas es:', resultado)

if __name__ == "__main__":
    print("Ejecutando el modulo 05-funciones.py")
    main()