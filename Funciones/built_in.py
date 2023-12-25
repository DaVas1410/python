numeros = [5, 6, 2, 10, 13]

# encontrando el numero mayor de una lista
numero_mas_alto = max(numeros)
print(numero_mas_alto)

#encontrando el numero menor de una lista
numero_menor = min(numeros)
print(numero_menor)

# redondeando a 6 decimales

numero = 5.12345678993838902409234908
round(numero,6)
print(numero)

#retorna false -> 0, vacio, false, none, true -> 1, cualquier valor o caracter

resultado_booleano = bool(0)
print(resultado_booleano)

#retorna true si todos los valores son verdaderos

resultado_all = all([123, "true", [2392,232 ]])
print(resultado_all)

#suma todos los valores iterables

resultado_suma = sum(numeros)
print(resultado_suma)
