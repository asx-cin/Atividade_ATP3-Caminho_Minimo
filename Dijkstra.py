# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np

# Funcao que extrai o menor elemento
def heapExtractMin(F, S):
  comprimento = len(F)
  if comprimento < 1:
    print("error heap underflow")
  menor = None
  for vertice in range(comprimento):
    if vertice not in S:
      if menor == None:
        menor = vertice
      elif F[vertice] < F[menor]:
        menor = vertice
  return menor

def relaxar(p, ant, u, v, w):
  if p[v] > (p[u]+w):
    ant[v] = u
    p[v] = p[u]+w

def dijkstra(grafo, s): # Dados Grafo G, origem s e Lista de adjacência de s, w
  # Inicializando as variáveis
  ant = [-1 for indice in range(0,len(grafo))]
  p = [float("+infinity") for indice in range(0,len(grafo))]
  #print("ant:", len(ant))  
  p[s] = 0
  #print("p:", len(p))
  S = list()
  F = p # cria fila de prioridade F com vértices do grafo

  for vertice in range(len(grafo)): # insere u em S e relaxa as arestas adjacentes
    u = heapExtractMin(F, S) # retirar vértice de F, reorganizando F
    S.append(u)  # adiciona u a lista de caminho mínimo
    for v, w in grafo[u]: # para cada vertice v adjacente a u faça
      relaxar(p, ant, u, v, w)
  return p, ant
