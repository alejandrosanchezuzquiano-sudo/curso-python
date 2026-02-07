###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

nombre = input("Ingresa tu nombre: ")
ciudad = input("Ingresa tu ciudad: ")
print(f'Tu ciudad es {ciudad}', end = '\n')
print(f'Tu nombre es {nombre}', end = '\n')

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

print(type(a), type(b), type(c), type(d), type(e), sep = '\n')

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

cadena = "12345"
cadena_entero = int(cadena)
cadena_float = float(cadena)
print(cadena_entero, cadena_float, sep = '\n')
valor = 3.99
valor_entero = int(valor)
print(valor_entero)

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")
nombre, edad, altura = input('Ingresa tu nombre, edad y altura: ').split()
print(f'Hola me llamo {nombre} tengo {edad} anos y mido {altura}')

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

print('El resultado de la division entera de el redondeo de pi y 2 es: ',int(round(3.1416)/2))