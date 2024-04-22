#########################################
# Universidad Estatal a Distancia(UNED) #
# Curso: Programación 3                 #
# Autor: Jonathan Arias Román           #
# Archivo: main.py                      #
# Fecha: 21/04/2024                     #
#########################################

# Importaciones necesarias de otros módulos
import tkinter as tk
from app import CalculatorApp

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
