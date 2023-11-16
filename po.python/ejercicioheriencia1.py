#En Python la herencia es un mecanismo que permite que una clase adquiera propiedades y metodos de otra clase conocida como clase padre o superclase. Esto facilita la reutilizacion de codigo y la creacion de jerarquías de clases.

#ejercicio 1
# Definicion de la clase animal
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f"{self.nombre} está comiendo.")

# Definicion de la clase perro que hereda de animal
class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau! ¡Guau!")

# Crear una instancia de la clase Perro llamada perro1 con nombre "Max" y raza "Labrador"
perro1 = Perro("Max", "Labrador")

# Acceder a los atributos y metodos de la clase base (Animal) y la clase derivada 
print(perro1.nombre)    # Acceder al atributo de la clase base (Animal)
print(perro1.raza)      # Acceder al atributo de la clase derivada (Perro)
perro1.comer()          # Llamar al método de la clase base (Animal)
perro1.ladrar()         # Llamar al método de la clase derivada (Perro)
