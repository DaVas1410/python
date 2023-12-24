# Datos
datos = {
    'Este Curso' : 1.5,
    'Minimo' : 2.5,
    'Crudo Curso' : 3.5,
    'Promedio' : 4,
    'Crudo' : 5,
    'Maximo' : 7
}
print('---------------------------')

print('Para la Parte A del ejercicio 1')

# Parte A
mas_rapido = 100 - (datos.get('Este Curso') / datos.get('Minimo')) * 100

print(f'El curso actual es {mas_rapido}% mejor que el curso mas rapido')

mas_lento = 100 - (datos.get('Este Curso') * 1000 // datos.get('Maximo')) / 10

print(f'El curso actual es {mas_lento}% mejor que el curso mas lento')

promedio = 100 -  (datos.get('Este Curso') / datos.get('Promedio')) *100

print(f'El curso actual es {promedio}% mejor que el promedio de cursos')

print('---------------------------')

print('Para la Parte B ejercicio 1')

#Parte B
perdida_promedio = 100 - (datos.get('Promedio') * 1000 // datos.get('Crudo')) / 10

print(f'En los cursos de afuera se reduce un {perdida_promedio}% del video crudo')

perdida_curso = 100 - (datos.get('Este Curso') * 1000 // datos.get('Crudo Curso')) /10

print(f'En el curso actual se reduce un {perdida_promedio}% del video crudo')

print('---------------------------')
5
print('Para la parte C del ejercicio 1')

#Parte C

equivale = datos.get('Promedio') *100 // datos.get('Este Curso') / 10
print(f'Ver 10 horas de este curso equivale a {equivale} de otros cursos')

equivale_1 = datos.get('Este Curso') * 100 // datos.get('Promedio') /10 
print(f'Ver 10 horas de otros cursos equivale a {equivale_1} horas de este curso')