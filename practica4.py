"""
Pediar al usario que ingres 20 numeros repetidos y sin repetir
los almacene en una lista y luego muestre la lista ordenada
de menor a mayor, tambien nos diga cuantos son repetidos
y cuantas veces se repitieron
seperarlos entre pares e impares
"""


def obtener_lista():
    print("Ingresa numeros repetidos y sin repetir")
    return [int(input(f"Número {i+1}: ")) for i in range(4)]


def imprimirNumerosOrdenados(lista):
    print("\nLista Ordenada")
    numeros = lista[:]
    numeros.sort()
    print(numeros)


def imprimirNumerosRepetidos1(lista):
    print("\nNumeros repetidos")
    numeros = lista[:]
    numeros.sort()
    r = 1
    for i, n in enumerate(numeros[1:]):
        if n == numeros[i]:
            r += 1
        if (n != numeros[i] or i+2==len(numeros)) and r > 1:
            print(f"{numeros[i]} - {r}")
            r = 1


def imprimirNumerosRepetidos2(lista):
    print("\nNumeros repetidos")
    for n in set(lista):
        r = lista.count(n)
        if r > 1:
            print(f"{n} - {r}")


def imprimirNumeroPares(lista):
    print("\nNumeros pares")
    print([n for n in set(lista) if (n % 2) == 0])


def imprimirNumeroImpares(lista):
    print("\nNumeros impares")
    print([n for n in set(lista) if (n % 2) == 1])


def main():
    lista = obtener_lista()
    imprimirNumerosOrdenados(lista)
    imprimirNumerosRepetidos2(lista)
    imprimirNumeroPares(lista)
    imprimirNumeroImpares(lista)


if __name__ == "__main__":
    main()
