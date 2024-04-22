#########################################
# Universidad Estatal a Distancia(UNED) #
# Curso: Programación 3                 #
# Autor: Jonathan Arias Román           #
# Archivo: advanced_ops.py              #
# Fecha: 21/04/2024                     #
#########################################

# Importaciones necesarias de otros módulos
import tkinter as tk
import numpy as np

# Agrega las operaciones al historial en el archivo de texto
def appendHistory(text):
    with open("calculation_history.txt", "a") as file:
        file.write(text)

# Lectura del archivo de texto con el historial de operaciones
def readHistory():
    try:
        with open("calculation_history.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        return "No history data found."

# Realiza operaciones aritmeticas con vectores
def performVectorAddition(entry1, entry2, label):
    try:
        vector1 = list(map(float, entry1.get().split()))
        vector2 = list(map(float, entry2.get().split()))
        if len(vector1) != len(vector2):
            raise ValueError("Vectors must be of the same length")
        result = [x + y for x, y in zip(vector1, vector2)]
        label.config(text=f"Result: {result}")
        appendHistory(f"Vector Addition: {vector1} + {vector2} = {result}\n")
    except Exception as e:
        label.config(text=f"Error: {str(e)}")

# Realiza operaciones aritmeticas con matrices
def performMatrixAddition(entry1, entry2, label):
    try:
        matrix1 = [list(map(float, row.split())) for row in entry1.get().split(';')]
        matrix2 = [list(map(float, row.split())) for row in entry2.get().split(';')]
        if len(matrix1) != len(matrix2) or any(len(row1) != len(row2) for row1, row2 in zip(matrix1, matrix2)):
            raise ValueError("Matrices must be of the same dimensions")
        result = [[x + y for x, y in zip(row1, row2)] for row1, row2 in zip(matrix1, matrix2)]
        label.config(text=f"Result: {result}")
        appendHistory(f"Matrix Addition: {matrix1} + {matrix2} = {result}\n")
    except Exception as e:
        label.config(text=f"Error: {str(e)}")

# Ventana con operaciones aritmeticas avanzadas: listas, vectores, matrices
def openAdvancedOperations(root):
    adv_ops_window = tk.Toplevel(root)
    adv_ops_window.title("Advanced Operations + Jonathan Arias Román")
    adv_ops_window.geometry("500x400")

    # Vector addition interface
    tk.Label(adv_ops_window, text="Enter vectors separated by space:").pack()
    vector_entry1 = tk.Entry(adv_ops_window, width=50)
    vector_entry1.pack()
    vector_entry2 = tk.Entry(adv_ops_window, width=50)
    vector_entry2.pack()
    vector_result_label = tk.Label(adv_ops_window, text="")
    vector_result_label.pack()
    tk.Button(adv_ops_window, text="Add Vectors", command=lambda: performVectorAddition(vector_entry1, vector_entry2, vector_result_label)).pack()

    # Matrix addition interface
    tk.Label(adv_ops_window, text="Enter matrices (semicolon separated rows):").pack()
    matrix_entry1 = tk.Entry(adv_ops_window, width=50)
    matrix_entry1.pack()
    matrix_entry2 = tk.Entry(adv_ops_window, width=50)
    matrix_entry2.pack()
    matrix_result_label = tk.Label(adv_ops_window, text="")
    matrix_result_label.pack()
    tk.Button(adv_ops_window, text="Add Matrices", command=lambda: performMatrixAddition(matrix_entry1, matrix_entry2, matrix_result_label)).pack()
