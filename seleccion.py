'''Ordenamiento de seleccion
Entrada: lista de elementos comparables
Salida: lista ordenada de menor a mayor
Restriccion: modifica una copia de la lista'''

def seleccion(lista):
    lista = lista.copy()
    n = len(lista)
    for i in range(n):
        min_i = i
        for j  in range(i+1, n):
            if lista[j] < lista[min_i]:
                min_i = j
        lista [i], lista[min_i] = lista [min_i], lista[i]
    return lista
