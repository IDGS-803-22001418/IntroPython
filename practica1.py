'''
Operación de multiplicación de a x b utilizando sumas
a = 3
b = 4
salida: 3+3+3+3=12
'''

a = 3
b = 4
r = 0
x = 0
salida = ''

while x < b:
    salida += str(a)
    if (x+1) != b:
        salida += '+'
    r += 3
    x += 1
    
salida += '='
salida += str(r)
print(salida)
