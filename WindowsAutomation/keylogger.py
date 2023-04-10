import pandas as pd
import os
import shutil

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
df['EDIT'] = df.pop('EDIT')
df.insert(0, 'NO.', range(1, len(df) + 1))
df_ordenado = df.copy()
df_ordenado.iloc[:, 1:] = df_ordenado.iloc[:, 1:].sort_values(by=['EDIT'], ascending=[True])
df_ordenado.to_excel('PedidosBMG1a1.xlsx', index=False)
dir12 = pd.read_excel('PedidosBMG1a1.xlsx', usecols=[12])
fil2 = pd.read_excel('PedidosBMG1a1.xlsx', usecols=[2])
print(dir12)
print(fil2)
dest_dir = 'V:/04-ABRIL/BUSCALIBRE/330 PEDIDOS'
print(dest_dir + ' Will be the destiny folder')
root_dir = 'O:'
subdirs = [x[0] for x in os.walk(root_dir)]
#print(subdirs)

for subdir in subdirs:
    for val in dir12.values:
        if str(val[0]) in subdir:
            for filename in os.listdir(subdir):
                for fileval in fil2.values:
                    if str(fileval[0]) in filename and filename.endswith('.pdf'):
                        source_file = os.path.join(subdir, filename)
                        dest_file = os.path.join(dest_dir, filename)
                        if not os.path.exists(dest_file):
                            shutil.copy(source_file, dest_file)
                        else:
                            print(f"{filename} already exists in {dest_dir}, skipping...")
