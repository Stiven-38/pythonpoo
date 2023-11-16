#El polimorfismo en Python es la capacidad de un objeto para tomar diferentes formas o comportamientos segun el contexto en el que se utilice. Esto se logra mediante el uso de la herencia y la implementacion de metodos con el mismo nombre pero con diferentes implementaciones en las clases hijas.

#ejercicio 1
# Definicion de la clase Vehiculo
class Vehiculo:
    def moverse(self):
        # Metodo abstracto sin implementacion sera implementado por  clases derivadas
        pass

# Definicion de la clase Automovil que hereda de Vehiculo
class Automovil(Vehiculo):
    def moverse(self):
        # Implementacion específica para el automovil
        return "El automóvil se desplaza por la carretera."

# Definicion de la clase Avion que hereda de Vehiculo
class Avion(Vehiculo):
    def moverse(self):
    
        return "El avión vuela por el cielo."

# Funcion que hace que un vehículo se mueva
def hacer_moverse(vehiculo):
    # Llama al metodo moverse del vehículo proporcionado e imprime el resultado
    print(vehiculo.moverse())

# Crear instancias de las clases Automovil y Avion
automovil = Automovil()
avion = Avion()

# Hacer que los vehículos se muevan utilizando la funcion hacer_moverse
hacer_moverse(automovil)  # Imprime el mensaje específico del automovil
hacer_moverse(avion)      # Imprime el mensaje específico del avion
