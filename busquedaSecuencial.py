'''Busqueda secuencial.
Entrada: lista(list), objeto(cualquier tipo comparable)
Salida: indice donde se encontró el objeto, o -1 si no existe
Restriccion: Funciona con listas ordenadas y desordenadas'''

def busquedaSecuencial(lista, objeto):
    for i, elemen in enumerate(lista):
        if elemen == objeto:
            return i
    return -1 