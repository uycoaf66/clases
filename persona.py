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
    
    def cumpleanhos(self):
        self.edad += 1 
        return self.edad 

Carlos = persona("Carlos", 40, "Pombero loco")
Eduardo = persona("Edu", 35, "plomero de plomo") 
Jean = persona("Mr. Jean", 65, "oficinista de dia, ninja de noche")

Carlos.cumpleanhos()
Eduardo.cumpleanhos()
Jean.cumpleanhos()

#agregar un metodo a la clase "persona" que se llame cumpleanhos y que aumente la edad de la 
#persona en un anho y retorne la edad nueva 
