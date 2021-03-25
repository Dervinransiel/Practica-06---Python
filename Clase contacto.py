'''
Crear una clase Contacto. Esta clase deberá tener los atributos "nombre, apellidos, telefono y direccion". 
También deberá tener una función "SetContacto"  con los parámetros que permita cambiar el valor de los atributos. 
También tendrá una función "Saludar", que escribirá en pantalla "Hola, soy " seguido de sus datos.
'''

class Contacto:

    def __init__(self, nombre, edad, apellidos, telefono, direccion):
       
        self.Nombre = "John eduardo"
        self.Edad = "25"
        self.apellido = "Ramirez acosta"
        self.telefono = "806-556-8795"
        self.direccion = "Calle 10 esq. 5 casa 15"

        SetContacto()

        p1 = Contacto("John  Eduardo","Ramirez acosta", 25, )

        print(p1.nombre)
        print(p1.apellido)
        print(p1.telefono)
        print(p1.direccion)

    def nombre(self):
          print("Hola soy el nuevo el contacto" + self.nombre)
    def Edad(self):
        print("mi edad es:" + self.edad)
    def telefono(self):
         print("mi telefono es:" + self.telefono)
    def direccion(self):
        print("mi direccion es:" + self.direccion)
   


