#https://pythones.net/clases-y-metodos-python-oop/

class Humano(): 
    def __init__(self, edad, nombre, ocupacion): 
        self.edad = edad 
        self.nombre = nombre 
        self.ocupacion = ocupacion

    def presentar(self):
        presentacion = ("Hola soy {}, mi edad es {} y mi ocupación es {}") 
        print(presentacion.format(self.nombre, self.edad, self.ocupacion)) 

Persona1 = Humano(31, "Pedro", "Ingeniero") 

print(Persona1.edad)
print(Persona1.nombre)
print(Persona1.ocupacion)

Persona1.presentar()