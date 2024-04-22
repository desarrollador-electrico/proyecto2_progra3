#########################################
# Universidad Estatal a Distancia(UNED) #
# Curso: Programación 3                 #
# Autor: Jonathan Arias Román           #
# Archivo: app.py                       #
# Fecha: 21/04/2024                     #
#########################################

# Importaciones necesarias de otros módulos
import tkinter as tk
from tkinter import simpledialog, messagebox
from config import SingletonConfig
from operations import OperationFactory
from advanced_ops import openAdvancedOperations, readHistory

# Definicion de la clase calculadora
class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.config = SingletonConfig.getInstance()
        self.root.title("Jonathan Arias Román - Basic Calculator")
        self.root.geometry("650x400")

        self.createWidgets()

    # Funcion con los botones, entradas de texto y demas
    def createWidgets(self):
        self.display = tk.Entry(self.root, font=("Arial", 16), borderwidth=2, relief="ridge")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        buttons = ['7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', '*', 'C', '0', '=', '/']
        row = 1
        col = 0
        for button in buttons:
            action = lambda x=button: self.onButtonClick(x)
            tk.Button(self.root, text=button, command=action, height=2, width=6).grid(row=row, column=col, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1

        advanced_ops_button = tk.Button(self.root, text="Advanced Operations", command=lambda: openAdvancedOperations(self.root), height=2, width=18)
        advanced_ops_button.grid(row=6, column=0, columnspan=4, sticky="nsew")

        history_button = tk.Button(self.root, text="View History", command=self.showHistory, height=2, width=18)
        history_button.grid(row=7, column=0, columnspan=4, sticky="nsew")

    # Metodo que invoca al realizar click al boton
    def onButtonClick(self, char):
        if char == 'C':
            self.display.delete(0, tk.END)
        elif char == '=':
            self.calculateResult()
        else:
            self.display.insert(tk.END, char)

    # Abre el archivo de texto y agrega la nueva operacion al historial
    def appendHistory(self, text):
        with open("calculation_history.txt", "a") as file:
            file.write(text)

    # Con este metodo realiza el calculo artimetico de la operacion basica
    def calculateResult(self):
        expression = self.display.get().split()
        try:
            a, operator, b = int(expression[0]), expression[1], int(expression[2])
            operation = OperationFactory.getOperation(operator)
            result = operation.execute(a, b)
            self.appendHistory(f"{a} {operator} {b} = {result}\n")
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
        except Exception:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")

    # Accede al archivo de texto con el historial de operaciones
    def showHistory(self):
        history = readHistory()
        messagebox.showinfo("Operation History", history)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
