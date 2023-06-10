import tkinter as tk
from tkinter import filedialog
import time

def quicksort(lista):
    if len(lista) <= 1:
        return lista

    pivot = lista[len(lista) // 2]
    menores = [x for x in lista if x < pivot]
    iguais = [x for x in lista if x == pivot]
    maiores = [x for x in lista if x > pivot]

    return quicksort(menores) + iguais + quicksort(maiores)


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
        numeros_ordenados = quicksort(numeros)
        tempo_final = time.time()
        tempo_execução = (tempo_final - tempo_inicial)*1000
        print(numeros_ordenados)
        print("Tempo de execução:", tempo_execução, "milisegundos")

# Chama a função para selecionar o arquivo
selecionar_arquivo()