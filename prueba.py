import time
import random
import sys
sys.setrecursionlimit(100000)
from busquedaSecuencial import busquedaSecuencial
from busquedaBinaria import busquedaBinaria
from burbuja import burbuja
from seleccion import seleccion
from rapido import quickSort

tamaños = [10, 100, 1000, 10000]
print ("Busqueda Secuencial")
for n in tamaños:
    lista_orde = list(range(n))
    lista_des = lista_orde.copy()
    random.shuffle(lista_des)
    objeto = n // 2

    t0 = time.perf_counter()
    busquedaSecuencial(lista_des, objeto)
    print(f"desordenada n={n}: {time.perf_counter()-t0: .8f}s")

    t0 = time.perf_counter()
    busquedaSecuencial(lista_orde, objeto)
    print(f"ordenada n={n}: {time.perf_counter()-t0: .8f}s")


print("\n busqueda binaria")
for n in tamaños:
    lista_orde = list(range(n))
    objeto = n // 2
    t0 = time.perf_counter()
    busquedaBinaria(lista_orde, objeto)
    print(f"Ordenada n={n}: {time.perf_counter()-t0:.8f}s")


print("\n Ordenamientos")
for n in tamaños:
    lista_orde = list(range(n))
    lista_des = lista_orde.copy(); random.shuffle(lista_des)
    lista_inv = list(reversed(range(n)))

    for nombre, fn in [("Burbuja", burbuja),
                       ("Seleccion", seleccion),]:
        
        for tipo, lst in [("Ordenada", lista_orde),
                          ("Desordenada", lista_orde),
                          ("Invertida", lista_inv)]:
            t0 = time.perf_counter()
            fn(lst)
            print(f"{nombre} {tipo} n={n}: {time.perf_counter()-t0:.8f}s")
    #Quick Sort        
    for tipo, lst in [("Ordenada", lista_orde),
                          ("Desordenada", lista_orde),
                          ("Invertida", lista_inv)]:         
     copia = lst.copy()
     t0 = time.perf_counter()
     quickSort(copia, 0, len(copia)- 1)
     print(f"Rápido {tipo} n={n}: {time.perf_counter()-t0:.8f}s")