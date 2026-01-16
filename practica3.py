"""
Pedir un número al usuario 
mostrar la tabla de multiplicar del número
"""

def main():
    num = int(input("Ingresa un numero para obtener su tabla de multiplicar: "))
    for i in range(1, 11):
        print("{} x {} = {}".format(num, i, num * i))
    
if __name__ == "__main__":
    main()