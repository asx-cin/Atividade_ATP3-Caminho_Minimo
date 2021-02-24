# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np
import PySimpleGUI as sg
from Dijkstra import dijkstra
from Grafo import Grafo_Dir
import time

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
  inicio = time.time()
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
      return ('Não existe translado de {} para {}.'.format(cidades[origem], cidades[destino]))
    return ('O melhor trajeto com Origem em {} e Destino em {} é:\n{} \nDistância total: {} Km \nTempo de atendimento: {}'.format(origem+1, destino+1, rota, distancias[destino], time.time()-inicio))


def main():
  #Gerando Grafo
  grafo = Grafo_Dir(len(cidades))

  for i in range(0,len(entrada)):
    grafo.adicionar_aresta(entrada[i], saida[i], distancias[i])

  Grafo = grafo.imprimir_grafo()
  #print(Grafo)
  #print(len(Grafo))
  
  class InterfaceGrafica:
    def __init__(self):
      layout=[[sg.Text('Origem'), sg.Input()],
              [sg.Text('Destino'), sg.Input()],
              [sg.Button('Buscar Rota')],
              [sg.Output(size=(80,5))]]

      self.janela = sg.Window('Informe sua rota').layout(layout)

    def Iniciar(self, Grafo):
      while True:
        self.button, self.OriDest = self.janela.Read()
        PosOrigem=self.OriDest[0]
        PosDestino=self.OriDest[1]
        if (PosOrigem in cidades) and (PosDestino in cidades):
          CamMin = tracar_menor_caminho(Grafo, cidades.index(PosOrigem)+1, cidades.index(PosDestino)+1)
          print(CamMin)
          print('=====================================================================')
        elif (PosOrigem not in cidades):
          print('Por favor, digite uma Origem válida!')
          print('')
        else:
          print('Por favor, digite um Destino válido!')
          print('')
        
  tela = InterfaceGrafica()
  print(tela.Iniciar(Grafo))

if __name__ == '__main__':
    main()
