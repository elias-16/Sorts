import tkinter as tk
from tkinter import filedialog
import time

def selection_sort(lista):
    n = len(lista)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j

        lista[i], lista[min_index] = lista[min_index], lista[i]

    return lista


def ler_numeros(arquivo):
    with open(arquivo, 'r') as file:
        numeros = [int(line.strip()) for line in file]

    return numeros


def selecionar_arquivo():
    root = tk.Tk()
    root.withdraw()

    caminho_arquivo = filedialog.askopenfilename(filetypes=[('Arquivos IN', '*.in'), ('Arquivos txt', '*.txt')])

    if caminho_arquivo:
        numeros = ler_numeros(caminho_arquivo)
        tempo_inicial = time.time()
        numeros_ordenados = selection_sort(numeros)
        tempo_final = time.time()
        tempo_execução = (tempo_final - tempo_inicial)*1000
        print(numeros_ordenados)
        print("Tempo de execução:", tempo_execução, "milisegundos")

# Chama a função para selecionar o arquivo
selecionar_arquivo()