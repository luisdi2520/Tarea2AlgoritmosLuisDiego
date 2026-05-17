'''' Swap
intercambia elementos dentro de una lista
Entrada: lista a, indice i, indice j
Salida: ninguna( modifica la lista en sitio)
Restriccion: i y j  deben ser indices validos de a '''

def swap(a, i, j):
    a[i], a[j] = a[j], a[i]



'''particion
Elige a[hi] como pivote  y reorganiza la sublista a[lo..hi]
para que todos los elementos menores o iguales al pivote  queden en su izquierda
y los mayores a su derecha.
Entrada: lista a, indice inicial lo, indice final hi
Salida: indice final donde quedó el pivote
Restriccion: lo y hi deben de ser indices validos de a, lo <= hi'''

def particion(a, lo, hi):
    pivot = a[hi]
    i = lo
    for j in range(lo, hi):
        if a[j] <= pivot:
            swap(a,i,j)
            i += 1
    swap(a, i, hi)
    return i

'''ordenamiento rapido o quick sort
Entrada: lista a, indice lo, indice hi
Salida: ninguna (ordena la lista de menor a mayor)
Restriccion: lo y hi deben ser indices validos de a.
Llamar como quicksort(lista, 0, len(lista)-1)
Listas muy grandes pueden exceder el limite de recursion'''

def quickSort(a, lo, hi):
    if lo >= hi:
        return
    p = particion(a, lo, hi)
    quickSort(a, lo, p - 1)
    quickSort(a, p + 1, hi)
