'''
Crear una clase Persona que tenga como atributos el
"cedula, nombre, apellido y la edad (definir las propiedades para poder acceder a dichos atributos)".
Definir como responsabilidad una cuncion para mostrar ó imprimir. 
'''

class Person:
  def __init__(self, nombre, apellido, edad, cedula):
    self.nombre = "Nombre = John Eduardo"
    self.apellido = "Apellido = Ramirez Acosta"
    self.edad = "Edad = 25"
    self.cedula = "Cedula = 402-306-988"
    

p1 = Person("John  Eduardo","Ramirez acosta", 25, 402-306-988,)

print(p1.nombre)
print(p1.apellido)
print(p1.edad)
print(p1.cedula)