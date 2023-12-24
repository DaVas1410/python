diccionario = {
    'nombre' : 'Juan',
    'Apellido' : 'Vasconez',
    'edad' : '21'
}

# nos da una tupla de los keys del diccionario

claves = diccionario.keys()

# get nos da un elemento del diccionario, no da excepciones si no existe

valor_elemento = diccionario.get('Juan')

# eliminando todo del diccionario, solo con keys

borrar_el_diccionario = diccionario.clear()

# eliminando un elemento del diccionario, keys

diccionario.pop('nombre')  # si se desea borrar varios, se usa item,item

# obteniendo un elemento dict_items iterable

diccionario_iterable = diccionario.items()


print(valor_elemento)