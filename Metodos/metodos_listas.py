# creando una lista 

lista = list(['hola','davas',34])

# len() cuenta la cantidad de elementos de una lista

resultado = len(lista)

# agrega elementos a la lista

lista.append('omg')

# agregando un elemento  a la lista con un indice especifico

lista.insert(2,'yachay')

# agregando varios elementos a la lista, se agregan lista a la lista

lista.extend([False,23423,'Daniel'])

# eliminar un elemento de la lista por su indice

lista.pop(0)    # -1 para eliminar el ultimo, -2 anteultimo, sucesivamente

# removiendo un elemento de la lista por su valor

lista.remove('davas')

# ordenar la lista de manera ascendente

lista.sort()  # solo funciona con listas de datos numericos o booleanos

# si usamos .sort(reverse=true) ordena de manera reversa, de manera descendente

# invertir los elementos de una lista

lista.reverse()

print(lista)

# eliminando todos los elementos de la lista

lista.clear()