# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np
import PySimpleGUI as sg
from Dijkstra import dijkstra
from Grafo import Grafo_Dir
import Main
import time
import random

# Importando os dados de entrada
df = pd.read_csv('rotas-potenciais.txt', sep=';') 

O, D = df['O'], df['D']  # Origem e Destinos
C_O, C_D = df['Origem'],  df['Destino'] # Nomes das cidades de Origem e Destino
dist = df['Distância aérea'] # As distâncias dos respectivos trajetos

# Transformando de Dataframe para Array
O = np.array(O) # Origem
D = np.array(D) # Destino 
C_O = np.array(C_O) # Nomes das cidades de Origem
C_D = np.array(C_D) # Nomes das cidades de Destino
dist = np.array(dist) # Distâncias aéreas

entrada = [i-1 for i in O]  # Iniciando a indentação em 0 para as Origens
saida = [i-1 for i in D]    # Iniciando a indentação em 0 para os Destinos
distancias = [i for i in dist]

cidades = [None for i in range(0, int(max(D)))]

# Para cada entrada/saida, pegar as cidades exclusivas e incluir na lista cidades
for city in entrada:
  if cidades[int(city)] == None:
    cidades[int(city)] = C_O[entrada.index(int(city))]
for city in saida:
  if cidades[int(city)] == None:
    cidades[int(city)] = C_D[saida.index(int(city))]

#print(cidades)
#print(len(cidades))

def tracar_menor_caminho(Grafo, origem, destino):
  origem, destino = origem-1, destino-1
  if not cidades[origem]:
    return ('A Origem {} não existe no roteiro!'.format(origem+1))
  elif not cidades[destino]:
    return ('O Destino {} não existe no roteiro!'.format(destino+1))
  else:
    print('Origem: {}'.format(cidades[origem]))
    print('Destino: {}'.format(cidades[destino]))
    caminho = list()
    caminho.append(destino)
    atual = destino
    distancias, antecessores = dijkstra(Grafo, origem)
    while caminho[-1] != origem:
      atual = antecessores[atual]
      caminho.append(atual)
    caminho = caminho[::-1]
    rota = [cidades[i] for i in caminho]
    if distancias[destino] == float("+infinity"):
      #print('Não existe translado de {} para {}.'.format(cidades[origem], cidades[destino]))
      return False
    #print('O melhor trajeto com Origem em {} e Destino em {} é:\n{} \nDistância total: {} Km.'.format(origem+1, destino+1, rota, distancias[destino]))
    return True 

def teste1():
  grafo = Grafo_Dir(len(cidades))

  for i in range(0,len(entrada)):
    grafo.adicionar_aresta(entrada[i], saida[i], distancias[i])

  Grafo = grafo.imprimir_grafo()
  tempos_de_atendimento = list()
  rodadas = 0
  while rodadas < 100:
    inicio = time.time()
    PosOrigem = random.choice(cidades)
    PosDestino = random.choice(cidades)
    while PosDestino == PosOrigem:
      PosDestino = random.choice(cidades)
    if (tracar_menor_caminho(Grafo, cidades.index(PosOrigem)+1, cidades.index(PosDestino)+1)):
      tempos_de_atendimento.append(time.time()-inicio)
      rodadas += 1
      print(rodadas)
  print('Tempo médio de atendimento para rotas válidas: %.4f' %(sum(tempos_de_atendimento)/rodadas))  

def teste2():
  grafo = Grafo_Dir(len(cidades))

  for i in range(0,len(entrada)):
    grafo.adicionar_aresta(entrada[i], saida[i], distancias[i])

  Grafo = grafo.imprimir_grafo()
  tempos_de_atendimento = list()
  rodadas = 0
  while rodadas < 100:
    inicio = time.time()
    PosOrigem = random.choice(cidades)
    PosDestino = random.choice(cidades)
    while PosDestino == PosOrigem:
      PosDestino = random.choice(cidades)
    if not (tracar_menor_caminho(Grafo, cidades.index(PosOrigem)+1, cidades.index(PosDestino)+1)):
      tempos_de_atendimento.append(time.time()-inicio)
      rodadas += 1
  print('Tempo médio de atendimento para rotas inválidas: %.4f' %(sum(tempos_de_atendimento)/rodadas))

def teste3():
  grafo = Grafo_Dir(len(cidades))

  for i in range(0,len(entrada)):
    grafo.adicionar_aresta(entrada[i], saida[i], distancias[i])

  Grafo = grafo.imprimir_grafo()
  tempos_de_atendimento = list()
  for i in range(0,100):
    inicio = time.time()
    PosOrigem = random.choice(cidades)
    PosDestino = random.choice(cidades)
    while PosDestino == PosOrigem:
      PosDestino = random.choice(cidades)    
    tracar_menor_caminho(Grafo, cidades.index(PosOrigem)+1, cidades.index(PosDestino)+1)
    tempos_de_atendimento.append(time.time()-inicio)

  print('Tempo médio de atendimento para rotas válidas e inválidas: %.4f' %(sum(tempos_de_atendimento)/100))

teste1()
teste2()
teste3()
