import matplotlib.pyplot as plt
from random import shuffle

# Buble sort skelleton con estos titulos de funciones crea funciones para hacer un programa bubllesort

def createRandomList(length):
    assert isinstance(length,int), "No es una lista"
    lista = [i for i in range(length)]
    # Shuffle devuelve none, cambia la lista in place
    # por que la listas son objetos mutables
    shuffle(lista)
    assert len(lista) == length, "La Lista no tiene la longitud indicada"
    assert isinstance(lista,list),"No es una lista"
    return lista
    # recibe como parametro la longitud de la lista
    # crea una lista de numero enteros
    # la "mezcla" = desordena
    # devuelve la lista


def display(lista):
    plt.clf()
    plt.bar(range(len(lista)), lista)
    plt.draw()


def less(a, b):
    return a<b
    # comprueba si a es menor que b
    # devuelve un boolean
    # recibe dos elementos
    # ojo a si el algoritmo de ordenacion es estable o inestable


def exchange(lista, i, j):
    assert isinstance(lista,list), "No es una lista"
    lista[i], lista[j] = lista[j], lista[i]
    assert isExchanged(lista,i,j)   
    # intercambia dos elementos de posicion en la lista
    # recibe la lista, la posicion i y la posicion j
    # devuelve None
    # comprueba que se han intercambiado los elementos


def isExchanged(lista, i, j):
    return (bool(lista[i]<lista[j]))
    # comprueba si el elemento en la posicion i
    # es menor que el elemento en la posicion j
    # devuelve un boolean


def isSorted(lista):
    for (offset, element) in enumerate(lista[:-1]):
        if element > lista[offset +1]:
            return False
    return True
    # comprueba si la lista esta oredenada
    # devuelve un boolean
    # offset , si despues de un for le das una tupla, crea un objeto que considera como un offset que acumula el valor del indice por el que va.



def bubbleSort(lista):
    isSwapped = True
    while isSwapped:
        isSwapped = False
        for i in range(len(lista-1)):
            if less(lista[i + 1], lista [1]):
                exchange(lista, i,i+1)
                isSwapped = True
    assert isSorted(lista), "La lista no esta ordenada"
    return lista
 
    # ordena la lista segun el algoritmo de ordenacion
    # bubble sort
    # cada vez que se intercambian dos elementos se dibuja la lista:
    # llama a display(lista)
    # devuelve None
    # Comprueba que la lista esta ordenada
    # Crear una lista de dentro a fuera, primero mirar que es lo mas basico que quiero hacer
    # y luego ir creando los for y whiles que lo anidan.


if __name__ == "__main__":

    plt.ion()
    lista = createRandomList(15)
    bubbleSort(lista)
    isSorted(lista)
    plt.show(block=True)

    # Listas de strings como casos test #
    # desactivar display() en bubbleSort()

    for test in open("stringTestCases.txt", 'r'):
        testList = list(test.replace(' ', ''))
        bubbleSort(testList)
        assert isSorted(testList), "Test %s " % (str(test))

    print("string test cases passed")
