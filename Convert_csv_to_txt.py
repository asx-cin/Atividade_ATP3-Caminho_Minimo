# -*- coding: UTF-8 -*-

import pandas as pd

df = pd.read_csv('rotas-potenciais.csv', sep=';') # header=None

print(df)

output = df.to_csv("rotas-potenciais.txt", sep=';', index=False)

output = pd.read_csv('rotas-potenciais.txt', sep=';') # ,header=None

print(output)
