# Ejercicio 1 : Definicion de la clase Vehiculo

# Definicion de la clase Vehiculo
class Vehiculo:
    # Constructor de la clase que inicializa los atributos marca, modelo y color
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    # Metodo para simular la accion de acelerar
    def acelerar(self):
        # Imprime un mensaje indicando que el vehículo esta acelerando
        print(f"El vehículo {self.marca} {self.modelo} está acelerando.")

    # Metodo para simular la acción de frenar
    def frenar(self):
        # Imprime un mensaje indicando que el vehículo esta frenando
        print(f"El vehículo {self.marca} {self.modelo} está frenando.")

# Crear una instancia de la clase Vehiculo
auto = Vehiculo("Toyota", "Corolla", "Rojo")

# Llamar al metodo acelerar en la instancia auto
auto.acelerar()

# Llamar al metodo frenar en la instancia auto
auto.frenar()
