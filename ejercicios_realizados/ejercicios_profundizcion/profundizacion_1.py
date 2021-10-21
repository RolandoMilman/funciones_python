# Funciones [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Este ejercicio representa ya un problema que forma parte de un juego
Lo que se desea realizar es una parte del juego "la generala".
El enunciado está armado a modo de guía, pueden resolver el problemla
de otra forma.
Si tienen dudas sobre el enunciado o alguno de los puntos por favor
comuníquelo por el campus y lo discutiremos entre todos, ya que siempre
puede haber varias interpretaciones de un mismo enunciado.

Deberá realizar una lista para guardar 5 dados, guardar los números
sacados en esa tirada de de dados (son 5 dados, cada uno del número 1 al 6)

1) El jugador tira la dados y saca 5 números aleatorios, puede usar
la función de "lista_aleatoria" para generar dichas lista de números.
Esa lista de datos se llamará "dados_tirados"
Lista "dados_tirados" se utiliza para guardar 5 dados, cada dado es de 6 caras,
es decir que cada dado puede valer un número de 1 a 6.

2) Luego debe analizar los 5 números y ver cual es el número que
más se repitio entre los 5 dados.
Debe usar la función de Python "max" con la "key" de list.count para
determinar cual fue el número que más se repitió en esa tirada. 
Consultar los ejemplos vistos en clase en donde se realizó esta operación con "max"

3) Una vez reconocido el número más repetido entre los 5 dados,
debe guardar en una variable aparte llamda "contador_generala"
cuantas veces se repitió hasta ahora el número más repetido. 
Ese número será el candidato para busscar sacar generala.
Si por ejemplo salió 4-4-2-1-4, debe quedarse con esos tres "4",
por lo canto el "contador_generala" valdrá 3, porque el primer número
más repetido fue 4, y este número salio tres veces en la primera tirada.

4) Debe volver a tira los dados, generar nuevos
números aleatorios.
Si en el contador "contador_generala" tengo 3 dados guardados
significa que ahora deberé tirar solo dos dados (5-3). 
Es decir que en este caso debería generar solo dos números
aleatorios nuevos con "lista_aleatoria"
Ahora tendré una nueva lista de "dados_tirados", en este caso
de dos nuevos números aleatorios entre 1 y 6 representando a los dados
tirados.

5) Luego de tirar nuevamente los datos en el paso anterior,
por ejemplo digamos que salieron los números: 4-1
Debo volver a contar cuantas veces aparece el número "4",
ya que es el número que estoy buscando almacenar para llegar a generala.
Se deberá aumentar el contador por cada cuatro que haya salido en la tirada.
Sino salió el "4" vuelvo a tirar sin aumentar el contador (repetir el punto 4)

5) Debe repetir este proceso hasta que el contador "contador_generala"
haya llegado a 5, es decir, he sacado 5 números iguales

NOTA: Recordar que en este ejemplo se buscó alcanzar la generala con "4" porque
fue el primero número más repetido en la primera tirada. Tener eso en cuenta que el
número que deberá buscar para alcanzar la generala depende de cual fue el más repetido
en la primera tirada.
'''

import random

# --------------------------------
# Dentro de esta sección copiar y crear
# todas las funciones que utilice
# --------------------------------
# Aquí dentro definir la función lista_aleatoria
def tirada(inicio, fin, cantidad):

    # for ... in range(....)
    
    for numero in range(cantidad):
            # Genero el número aleatorio y lo agrego a la lista
            numero_aleatorio = random.randrange(inicio, fin+1)
            lista_numeros.append(numero_aleatorio)
    return lista_numeros
# --------------------------------
# Aquí dentro definir la función contar
def contar_primera_tirada(lista_numeros):

    max_repeticiones = max(lista_numeros, key=lista_numeros.count)
    cuenta = lista_numeros.count(max_repeticiones)
    print( 'con', cuenta, 'veces')
    
    return cuenta

# ------------------------------------------
# Aquí dentro definir la función buscar número que más se repite en la primera tirada
def numero_primera_tirada(lista_numeros):

    max_repeticiones = max(lista_numeros, key=lista_numeros.count)
    print('El número con más valores encontrados es el {}'.format(max_repeticiones))
    
    return max_repeticiones

# ------------------------------------------
# Aquí dentro la función que busca número en la lista de la primera tirada
def busca_valor_en_lista(lista_numeros, numero_a_buscar ):

    if (numero_a_buscar in lista_numeros): 
        print('El número {} existe en la lista' .format(numero_a_buscar))
    
    return numero_a_buscar

# ------------------------------------------
def otras_tirada(inicio, fin, cantidad):

   return cantidad 
# Aquí dentro definir la función contar_otras_tiradas
def contar_otras_tiradas(lista_numeros, valor):

    cuenta = lista_numeros.count(valor)
    if (cuenta>=1):
        print('El número ', valor, 'se repite', cuenta, 'veces')
    else:
        print(valor)
        #lista_numeros.append(numero_aleatorio)
        #       break
    return cuenta


# --------------------------------

if __name__ == '__main__':

    
    inicio = 1
    fin = 6
    cantidad = 5
    lista_numeros= []
    numero_a_buscar = 0
    veces_tirada = 0

    print("¡El juego de la generala!")
    # A partir de aquí escriba el código que
    # invoca a las funciones y resuelve el enunciado
    # Leer el enunciado con atención y consultar cualquier duda
    lista_numeros = tirada(inicio, fin, cantidad)
    #lista_numeros=['1', '2', '3', '5', '6']
    print(lista_numeros)

    #lista_numeros=['1', '1', '3', '3', '3']
    valor_primer_tirada = numero_primera_tirada(lista_numeros)
    cantidad_primer_tirada = contar_primera_tirada(lista_numeros)
    
   
    if(cantidad_primer_tirada>1):
        numero_a_buscar= valor_primer_tirada
    else:                                       # Todos los valores distintos
         # Si no se repite ningún número, habilito para 
        # elegir qué número quiero seguir
        while True:
            numero_a_buscar = int(input('Ingrese el número a seguir:   '))
            try:
                otro_indice = lista_numeros.index(str(numero_a_buscar))
                print("El número {} está en la posición {} de la lista".format(numero_a_buscar, otro_indice+1))
                break
            except:
                print("Lo siento, el número elegido {} no está en la lista" .format(numero_a_buscar))
    veces_tirada += 1
    cantidad -= cantidad_primer_tirada
    while (cantidad>0):
        lista_numeros= []
        lista_numeros = tirada(inicio, fin, cantidad)
        #print(lista_numeros)
        dados_aparece = lista_numeros.count(numero_a_buscar)
        # Muestro los valores de la tirada y lacantidad de veces que aparece el número seguido
        print('Tirada {} .El número {} aparece {} veces en la tirada {}'.format(lista_numeros, numero_a_buscar, dados_aparece, veces_tirada))
        
        veces_tirada += 1
        cantidad -= dados_aparece  

    print("¡FELICITACIONES! Logró la generala en {} tiradas." .format(veces_tirada))


