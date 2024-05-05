import pandas as pd

df = pd.read_csv('./exemplo.csv')

df_filtrado = df[df['estado'] == 'SP' ]

print(df_filtrado)



df = pd.read_csv('./exemplo2.csv')

df_filtrado = df[df['estado'] == 'DF' ]

print(df_filtrado)