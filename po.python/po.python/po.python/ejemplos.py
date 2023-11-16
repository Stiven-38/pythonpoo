class Estudiante:
    # Atributos de clase (compartidos por todas las instancias)
    codigo = 0
    nombre = ""
    apellido = ""

    # Metodo constructor (__init__) que se llama al crear una nueva instancia
    def __init__(self, codigo=0, nombre="", apellido=""):
        # Atributos de instancia (pertenece a cada instancia individual)
        self.codigo = codigo
        self.nombre = nombre
        self.apellido = apellido

    # Metodo para imprimir los datos del estudiante
    def imprimir_datos(self):
        print(self.codigo, self.nombre, self.apellido)

# Crear una instancia de la clase Estudiante
estudiante1 = Estudiante(codigo=1, nombre="Stiven", apellido="Ramirez")

# Llamar al metodo imprimir_datos para mostrar los datos del estudiante1
estudiante1.imprimir_datos()


# Crear objeto adso
adso = Estudiante()

# Acceder a traves del objeto adso a los atributos de la clase estudiante y dar valores
adso.codigo = 1
adso.nombre = 'Natalia'
adso.apellido = 'Ramirez'

# Llamar al metodo imprimir_datos para adso
adso.imprimir_datos()


#Clase Constructor

class Estudiante1:
    def __init__(self, codigo, nombre, apellido):
        self.codigo = codigo
        self.nombre = nombre
        self.apellido = apellido

    def imprimir_informacion(self):
        print(self.codigo, self.nombre, self.apellido)

# Crear una instancia de la clase Estudiante1
adso1 = Estudiante1(2, 'Valeria', 'useche')

# Llamar al metodo imprimir_informacion para mostrar los datos de adso1
adso1.imprimir_informacion()
