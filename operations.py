#########################################
# Universidad Estatal a Distancia(UNED) #
# Curso: Programación 3                 #
# Autor: Jonathan Arias Román           #
# Archivo: operations.py                #
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
class Operation:
    def execute(self, a, b):
        pass

class AddOperation(Operation):
    def execute(self, a, b):
        return a + b

class SubtractOperation(Operation):
    def execute(self, a, b):
        return a - b

class MultiplyOperation(Operation):
    def execute(self, a, b):
        return a * b

class DivideOperation(Operation):
    def execute(self, a, b):
        return a / b if b != 0 else "Error: Division by zero"

class OperationFactory:
    @staticmethod
    def getOperation(operator):
        operations = {'+': AddOperation, '-': SubtractOperation, '*': MultiplyOperation, '/': DivideOperation}
        return operations.get(operator, lambda: None)()
