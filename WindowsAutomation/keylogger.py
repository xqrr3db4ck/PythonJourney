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
                        
os.chdir('V:/04-ABRIL/BUSCALIBRE/330 PEDIDOS')                        
         
def remove_files_with_words(directory, words):
    files = os.listdir(directory)
    for file in files:
        if any(word in file for word in words):
            os.remove(os.path.join(directory, file))

def remove_duplicate_files(directory):
    files = os.listdir(directory)
    tapa_files = {}
    contenido_files = {}
    for file in files:
        if "TAPA" in file:
            name = file.split("_")[0]
            if name not in tapa_files:
                tapa_files[name] = []
            tapa_files[name].append(file)
        elif "CONTENIDO" in file:
            name = file.split("_")[0]
            if name not in contenido_files:
                contenido_files[name] = []
            contenido_files[name].append(file)
    for files_dict in [tapa_files, contenido_files]:
        for name, files in files_dict.items():
            if len(files) > 1:
                files.sort()
                for file in files[:-1]:
                    os.remove(os.path.join(directory, file))

directory = "/home/crxxp919/PycharmProjects/pythonProject"
words = ["MUESTRA", "IMAGEN", "THECAKEISALIE"]
remove_files_with_words(directory, words)

directory = "/home/crxxp919/PycharmProjects/pythonProject"
remove_duplicate_files(directory)

### check if the files match with the variable fil2, and make a report if the names doesnt match, then, send an email to report the files, with the code
### of the file and the number of the column 0 of the excel converted.

os.mkdir('V:/04-ABRIL/BUSCALIBRE/330 PEDIDOS/CONTENIDOS')
os.mkdir('V:/04-ABRIL/BUSCALIBRE/330 PEDIDOS/MONTAJES')
os.mkdir('V:/04-ABRIL/BUSCALIBRE/330 PEDIDOS/TAPAS')
os.mkdir('V:/04-ABRIL/BUSCALIBRE/330 PEDIDOS/TAPAS/BRILLANTE')
os.mkdir('V:/04-ABRIL/BUSCALIBRE/330 PEDIDOS/TAPAS/MATE')
os.system('gci -filter *.pdf -include *tapa* |mv -destination .\\TAPAS')
os.system('gci -filter *.pdf -include *contenidos* |cp -destination .\\CONTENIDOS')
os.system('gci -filter *.pdf -include *contenidos* |mv -destination .\\MONTAJES')




                        
