import tkinter as tk
from tkinter import filedialog
import time

def insertion_sort(lista):
    n = len(lista)

    for i in range(1, n):
        key = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > key:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = key

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
        numeros_ordenados = insertion_sort(numeros)
        tempo_final = time.time()
        tempo_execução = (tempo_final - tempo_inicial)*1000
        print(numeros_ordenados)
        print("Tempo de execução:", tempo_execução, "milisegundos")

# Chama a função para selecionar o arquivo
selecionar_arquivo()