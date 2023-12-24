lista = ["Lucas dato","juan", True,1.85]
lista[0]= "DaVas"       # la lista se puede modificar
print(lista)
print(lista [0])  #en python se cuenta dese el numero 0

tupla = ("Lucas dato","juan", True,1.85)       # las tuplas no se pueden modificar como las varibales o listas
print(tupla)
print(tupla [0])


# creando un conjunto con set, aqui podemos intercambiar los lugares de memoria de los elementos, pero no se puede moficar elementos. no se puede mostrar
# si un dato se repite no se moestrara y no se puede acceder a cada elemento por indices, pero se podra por bucles, son datos desordenados

conjunto = {"Lucas dato","juan", True,1.85}   


#creando un diccionario, definimos variables dependientes, la estructura es key: value

diccionario = {
    'nombre' : 'DaVas',
    'canal' : 'gameplay',
    'altura' : 1.8
}

print(diccionario['altura'] + 2)