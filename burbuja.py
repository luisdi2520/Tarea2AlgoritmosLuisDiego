'''Ordenamiento de burbuja compra elementos de una lista para ver cual es mayor o menor entre ellos.
Entrada: lista (list) de elementos comparables
Salida: lista ordenada de menor a mayor
Restriccion: modifica la lista original'''

def burbuja(lista):
    lista = lista.copy()
    n = len(lista)
    for i in range(n):
            for j in range(0, n-i-1):
             if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista
