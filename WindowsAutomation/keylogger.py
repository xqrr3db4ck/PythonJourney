import pandas as pd
import os
import shutil

df = pd.read_excel('pedidos.xlsx')
df.drop(df.columns[[1, 2, 3, 4, 8, 17, 18, 19]], axis=1, inplace=True)
df.iloc[:,0] = df.iloc[:,0].str[5:]
df.iloc[:,1] = df.iloc[:,1].str[6:]
df.iloc[:,3] = df.iloc[:,3].str[6:]
df['COD_PUB'] = df['COD_PUB'].str.lstrip('0') + '_'
df['TITULO'] = df['TITULO'].str.slice(stop=30)
df['EDIT'] = df['EDIT'].str.slice(stop=-4)
df['CONT'] = df['CONT'].replace({'BNOBR090': 'B90', 'BNOBR080': 'HOL.'})
df['TAPA'] = df['TAPA'].replace({'TAILU270': 'ESM300'})
df['ENC'] = df['ENC'].replace({'ENCBIN': 'RÚST.'})
df['LAM'] = df['LAM'].replace({'LAMMAT': 'MATE', 'LAMBTE': 'BTE'})
df.to_excel('pedidos.xlsx', index=False)