import modulo1
saludo = modulo1.saludar("Juan")
print(saludo)

import modulo1 as md 
saludo = md.saludar("Juan")
print(saludo)

from modulo1 import saludar #puedes importar mas de una funcion con una , entre ellas
saludo = saludar("Juan")
print(saludo)