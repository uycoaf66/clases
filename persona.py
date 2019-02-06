# Crear una carpeta que se llame clases y adentro poner los 
#archivos dino.py persona.py 

#Crear una clase Persona () en el archivo persona.py que tenga como atributos 
#nombre, edad y profesion. 

#Al instanciar la clase tiene que saludar igual que el dino diciendo sus atributos 

class persona: 

    def __init__(self, su_nombre, su_edad, su_profesion):
        self.nombre = su_nombre
        self.edad = su_edad
        self.profesion = su_profesion
        print("Hola soy un humano, mi nombre es", self.nombre, "tengo", self.edad, "anhos", "trabajo como", self.profesion)

humano = persona("Carlos", "40", "Pombero")    