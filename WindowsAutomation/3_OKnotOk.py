import pandas as pd
import os
from openpyxl import load_workbook
from openpyxl.styles import PatternFill
#from openpyxl.utils import rows_from_range

df = pd.read_excel('pedidos.xlsx')
df.drop(df.columns[[1, 2, 3, 4, 8, 17, 18, 19]], axis=1, inplace=True)
df.iloc[:, 0] = df.iloc[:, 0].str[5:]
df.iloc[:, 1] = df.iloc[:, 1].str[5:]
df.iloc[:, 3] = df.iloc[:, 3].str[6:]
df['COD_PUB'] = df['COD_PUB'].str.lstrip('0') + '_'
df['TITULO'] = df['TITULO'].str.slice(stop=30)
df['TITULO'] = df['TITULO'].astype(str) + '  -'
df['EDIT'] = df['EDIT'].str.slice(stop=-3)
df.replace({'BNAHU080': 'HOL.', 'BNOBR080': 'B70', 'COOBR090': 'B90', 'BNOBR090': 'B90', 'BNILM115': 'E115',
            'COAHU080': 'HOL.', 'TAILU270': 'ESM300', 'ENCBIN': 'RÚST.', 'ENCACA': 'CABA.', 'LAMMAT': 'MAT',
            'LAMBTE': 'BTE'}, regex=True, inplace=True)
#df['EDIT'] = df.pop('EDIT')
df.insert(0, 'NO.', range(1, len(df) + 1))
#df_ordenado = df.copy()
#df_ordenado.iloc[:, 1:] = df_ordenado.iloc[:, 1:].sort_values(by=['EDIT'], ascending=[True])
#df_ordenado.to_excel('PedidosBMG1a1.xlsx', index=False)
#dir12 = pd.read_excel('PedidosBMG1a1.xlsx', usecols=[12])
#fil2 = pd.read_excel('PedidosBMG1a1.xlsx', usecols=[2])
#names = fil2.values.flatten().tolist()
#dir_path = "D:/temporal"
#files = os.listdir(dir_path)
df['EDIT'] = df.pop('EDIT')
wb = load_workbook('PedidosBMG1a1.xlsx')
ws = wb.active
red_fill = PatternFill(start_color='FFFF0000', end_color='FFFF0000', fill_type='solid')
for i, name in enumerate(names):
    found = False
    for file in files:
        if name in file and file.startswith(name.split('_')[0]):
            found = True
            break
    if not found:
        print(f'{name} not found in directory')
        ws.cell(row=i+2, column=3).fill = red_fill
wb.save('PedidosBMG1a1.xlsx')

