#ejercicio 2
# Definicion de la clase Animal
class Animal:
    def __init__(self, nombre):
        # Constructor de la clase Animal que inicializa el atributo nombre
        self.nombre = nombre

    def sonido(self):
        # Metodo abstracto sin implementacion sera implementado por las clases derivadas
        pass

# Definicion de la clase Vaca que hereda de Animal
class Vaca(Animal):
    def sonido(self):
        # Implementacion específica para la vaca devuelve el sonido que hace
        return "La vaca hace 'mu mu'."

# Definicion de la clase Pato que hereda de Animal
class Pato(Animal):
    def sonido(self):
        # Implementacion específica para el pato devuelve el sonido que hace
        return "El pato hace 'cua cua'."

# Funcion que muestra el sonido de un animal
def mostrar_sonido(animal):
    # Llama al metodo sonido del animal proporcionado e imprime el resultado
    print(animal.sonido())

# Crear instancias de las clases Vaca y Pato
vaca_instancia = Vaca("Maravilla")
pato_instancia = Pato("Willy")

# Llamar a la funcion mostrar_sonido con las instancias de Vaca y Pato
mostrar_sonido(vaca_instancia)  # Imprime el sonido de la vaca
mostrar_sonido(pato_instancia)  # Imprime el sonido del pato
