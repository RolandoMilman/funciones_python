# Funciones [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con funciones

def imprimir_mayor(numero_1, numero_2):
    print("Funcion imprimir mayor")
    # En esta función debe determinar cual de los dos
    # números ingresados por parámetro es mayor
    # y luego imprimir dicho valor en pantalla
    if(numero_1>numero_2):
        print('El número mayor de los ingresdos es:', numero_1)
    elif(numero_2>numero_1):
        print('El número mayor de los ingresdos es:', numero_2)
    else:
        print('Ambos números ingresdos son iguales:', numero_1, ',', numero_2)

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Alumno: Complete la función "imprimir_mayor"
    imprimir_mayor(12, 12)

    print("terminamos")