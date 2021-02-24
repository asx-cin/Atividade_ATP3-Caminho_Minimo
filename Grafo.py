# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np

# Para Grafo Direcionado usando Lista
class Grafo_Dir:
  def __init__(self, V): # recebe como parâmetro a quantidade de vértices do grafo
    self.grafo = [[] for i in range(0, V)] # criando um grafo formado por uma lista de adjacências vazia para cada nó
    #print(self.grafo)

  def adicionar_aresta(self, u, v, w): # Adicionar o par ordenado (u,v) no grafo com peso w
    self.grafo[u].append((v,w))
    return (u, v)

  def imprimir_grafo(self): # Imprimir o grafo
    return self.grafo
