# creando una funcion simple
def saludar():
    print("Hola mundo")
    
# llamando la funcion
saludar()

# creando una funcion con parametros

def saludar(nombre, sexo):
    sexo = sexo.lower()
    if (sexo == "hombre"):
        print(f"Hola Sr.",nombre)
    elif (sexo == "mujer"):
        print(f"Hola Sra.",nombre)
    print(f"Hola",nombre)
    
saludar("Juan", 'hombre')

#crear una funcion que retorne valores

def caculo(num_):
    listado = 'abdcasidja'
    numero_entero = str(num_)
    num_= int(numero_entero[0])
    c1 = num_  - 2
    c2 = num_ 
    c3 = num_ * 2
    contrasena = f"{listado[c1]}{listado[c2]}{listado[c3]}"
    return contrasena

password =  caculo(1)
frase = f"Tu contraseña es: {password}"
print(frase)


#crear una funcion que nos retorne multiples valores
def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña,num
    
#desempaquetando la funciòn
password,primer_numero = crear_contraseña_random(981)

#mostrando los resultados obtenidos y los datos utilizados para obtenerlo
print(f"Tu contraseña nueva es: {password}")
print(f"El nùmero utilizado para crearla fue: {primer_numero}")
