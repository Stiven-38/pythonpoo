#una clase es una estructura que se utiliza para crear objetos.
# Una clase define las propiedades y comportamientos de un objeto. 
# Las propiedades se definen como variables dentro de la clase, y los comportamientos
#se definen como metodos (funciones)

#ejercicio 1
# Definicion de la clase Persona
class Persona:
    # Constructor de la clase
    def __init__(self, nombre, edad):
        # Inicializacion de los atributos de la instancia
        self.nombre = nombre
        self.edad = edad

    # Metodo de la clase para saludar
    def saludar(self):
        # Imprime un mensaje de saludo utilizando los atributos de la instancia
        print(f"Hola mi nombre es {self.nombre} y tengo {self.edad} años")

# Crear una instancia de la clase Persona con nombre "Stiven" y edad 18
persona1 = Persona("Stiven", 18)

# Llamar al metodo saludar en la instancia persona1
persona1.saludar()