numeros = [2,4,6,8,10]
#creando una funcion lambda para multiplicar por 2
multiplicar_por_2 = lambda x: x*2

print(multiplicar_por_2(2))

#utilizando una funcion comun
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

#usando filter
numero_pares = list(filter(es_par, numeros))
print(numero_pares)

#usando filter con lambda
numero_pares = list(filter(lambda numero: numero % 2 == 0, numeros))
