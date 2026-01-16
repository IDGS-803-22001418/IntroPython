'''
Realizar un programa que nos permita realizara las operaciones bàsicas 
+,-,*,/ utilizando una función para cada operación y pedir los dos
parámetros, lo primero que se visualizara seraá el menú
1. Suma
2. Resta,
3. Multiplicar,
4. Dividir,
5. Salir
Opcion:

Luego de realizar la operación se debe mostrar el resultado y regresar al menú
'''

def suma():
    a = input('Ingresa el número 1:')
    b = input('Ingresa el número 2:')
    print('El resultado es: {}'.format(int(a)+int(b)))
    input('Presiona enter para continuar')

def resta():
    a = input('Ingresa el número 1:')
    b = input('Ingresa el número 2:')
    print('El resultado es: {}'.format(int(a)-int(b)))
    input('Presiona enter para continuar')

def multiplicacion():
    a = input('Ingresa el número 1:')
    b = input('Ingresa el número 2:')
    print('El resultado es: {}'.format(int(a)*int(b)))
    input('Presiona enter para continuar')

def division():
    a = input('Ingresa el número 1:')
    b = input('Ingresa el número 2:')
    if int(b) == 0:
        print('No es posible dividir entre 0')
    else:
        print('El resultado es: {}'.format(int(a)/int(b)))
    input('Presiona enter para continuar')

def main():
    while True:
        print('')
        print('Ingresa una opción:')
        print('1. Suma, 2. Resta, 3. Multiplicar, 4. Dividir, 5. Salir')
        entrada = input('Opcion:')
        
        if entrada == '1':
            suma()
        elif entrada == '2':
            resta()
        elif entrada == '3':
            multiplicacion()
        elif entrada == '4':
            division()
        elif entrada == '5':
            break
        

if __name__ == "__main__":
    main()