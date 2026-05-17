'''Busqueda binaria
Entrada: lista ordenada(list), objeto(cualquier tipo comparable)
Salida: indice donde se encontró el objeto, o -1 si no existe
Restircciones: la lista debe ser si o si ordenada'''

def busquedaBinaria(lista, objeto):
    izq, der = 0, len(lista) -1
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == objeto:
            return medio
        elif lista[medio] < objeto:
            izq = medio + 1
        else:
            der = medio -1
    return -1