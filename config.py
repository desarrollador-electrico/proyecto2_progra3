#########################################
# Universidad Estatal a Distancia(UNED) #
# Curso: Programación 3                 #
# Autor: Jonathan Arias Román           #
# Archivo: config.py                    #
# Fecha: 21/04/2024                     #
#########################################

# Importaciones necesarias de otros módulos
"""
Este código incorpora los patrones de diseño Singleton y Factory en
una aplicación de calculadora básica utilizando Tkinter. El patrón Singleton
se usa para manejar configuraciones globales, mientras que el patrón Factory
facilita la expansión de la aplicación al añadir más operaciones sin modificar
el código existente. La ventana principal muestra cómo puedes organizar los widgets
en Tkinter y prepararte para una funcionalidad más rica.  """

class SingletonConfig:
    _instance = None

    @classmethod
    def getInstance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        if SingletonConfig._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.configuration = {"theme": "Light"}

    def setConfig(self, key, value):
        self.configuration[key] = value

    def getConfig(self, key):
        return self.configuration.get(key, "Unknown key")
