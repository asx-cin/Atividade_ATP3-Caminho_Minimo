**Autores:** Amanda Silva (asx@cin.ufpe.br) e Andersson Alves (aas9@cin.ufpe.br)

# Atividade_ATP3-Caminho_Minimo

# Base de dados: Matriz de Origem/Destino real de deslocamentos de pessoas, elaborada a partir de Big Data da telefonia móvel
A Secretaria Nacional de Aviação Civil do Ministério da Infraestrutura em parceria com a Universidade Federal de Santa Catarina (UFSC), desenvolveram uma matriz de deslocamentos origem-e-destino de pessoas pelo transporte aéreo/não aéreo no país com base nos dados de telefonia móvel.

Objetivo do trabalho: compreender a verdadeira origem e destino dos viajantes.

O resultado permite a identificação de rotas potenciais para o transporte aéreo, estudo este feito em conjunto com a Universidade de Brasília (UnB).
Eles disponibilizaram este estudo de rotas potenciais para o transporte aéreo de passageiros[1].

No dataset contém um código para cada cidade, o nome de cada origem e destino correspondente, a latitude e longitude, distância, custo, demanda, receita total, vôos comerciais 2019, entre outros. 

# Contextualização do Problema
O dataset utilizado nesta atividade contém listas de possíveis novas rotas de aeroportos brasileiros com suas respectivas distâncias entre cidades. Cada cidade foi modelado como um vértice do grafo, e cada conexão entre duas cidades como uma aresta. Para o peso de cada aresta foi considerado o valor da distância entre as cidades. Dessa forma, o problema considerado consiste em como ir de uma cidade a outra pelo menor caminho, visto que não há rotas de vôos diretos entre todos os aeroportos das cidades.

# Tratamento dos Dados
Os dados estavam indexados em uma planilha no formato .ods, então foi necessário a conversão, para o tipo .csv e posteriormente para .txt.
Entre os dados apresentados na planilha, foram considerados apenas aqueles referentes à origem, ao destino e à distância aérea, por se tratarem dos mais relevantes para a resolução do problema.

No tratamento dos dados foram eliminados as conexões que apresentavam distâncias nulas.
Os dados foram importados para a linguagem de programação Python 3.7 pela biblioteca Pandas.

# Como o problema foi resolvido?
O problema foi tratado como um grafo direcionado por meio de uma lista de adjacências e para cada cidade foi atribuído uma numeração iniciando em 0 até o número total de cidades (vértices).

O uso do algoritmo de Dijkstra foi utilizado para encontrar o caminho mínimo a partir de um nó origem, que representa a cidade de Origem para todos os demais pontos e em seguida usado uma função que a partir da lista de antecessores determina o percurso potencial da cidade Origem até a cidade Destino.

# Ferramentas utilizadas
O trabalho foi implementado em linguagem de programação Python 3.7 e particionado em 5 arquivos:
- Convert_csv_to_txt: para converter os dados;
- Dijkstra: para encontrar o menor caminho;
- Grafo: para gerar o grafo utilizado no modelo;
- Main: arquivo principal que chama os arquivos anteriores.
- Testes: usado para testar o tempo de execução para três casos distintos.

**Bibliotecas utilizadas:**

**Pandas:** para manipulação dos dados, pois ficam postos em tabela;

**Numpy:** para manipulação de dados;

**PySimpleGUI:** para a interface gráfica [2].

**Obs:** para utilizar a interface gráfica, é necessário utilizar: <pip install PySimpleGUI>

# Resultados
O tempo médio para 100 resoluções com somente rotas válidas foi de: 2.1973 segundos.

O tempo médio para 100 resoluções com somente rotas inválidas foi de: 2.895 segundos.

O tempo médio para 100 resoluções com rotas válidas e inválidas foi de 2.4142 segundos. 

**Obs.:** Os testes foram escolhendo Origens e Destinos aleatoriamente.


# Referências
[1] Ministério da Infraestrutura. Matriz de origem-destino real de deslocamentos de pessoas por big data da telefonia móvel. Estudo de Rotas Potenciais. Disponível em: <http://dados.transportes.gov.br/ne/dataset/matriz-de-origem-destino-real-de-deslocamentos-de-pessoas-por-big-data-da-telefonia-movel/resource/737d2b5f-3227-4812-be14-ff52c88c05cd>. Acessado em: 19 de fev. 2021.

[2] PySimpleGUI. GUIs Python para humanos. Disponível em: http://www.PySimpleGUI.org. Acessado em: 22 de fev de 2021.
