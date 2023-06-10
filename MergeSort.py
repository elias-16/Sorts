import tkinter as tk
from tkinter import filedialog
import time

def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = lista[:meio]
    direita = lista[meio:]

    esquerda = merge_sort(esquerda)
    direita = merge_sort(direita)

    return mesclar(esquerda, direita)

def mesclar(esquerda, direita):
    mesclada = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            mesclada.append(esquerda[i])
            i += 1
        else:
            mesclada.append(direita[j])
            j += 1

    while i < len(esquerda):
        mesclada.append(esquerda[i])
        i += 1

    while j < len(direita):
        mesclada.append(direita[j])
        j += 1

    return mesclada


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
        numeros_ordenados = merge_sort(numeros)
        tempo_final = time.time()
        tempo_execução = (tempo_final - tempo_inicial)*1000
        print(numeros_ordenados)
        print("Tempo de execução:", tempo_execução, "milisegundos")

# Chama a função para selecionar o arquivo
selecionar_arquivo()