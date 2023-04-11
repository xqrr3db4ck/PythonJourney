import os
import pandas as pd

df = pd.read_excel('PedidosBMG1a1.xlsx', names=['COD_PUB'])
print(df)

files = os.listdir('path/to/directory')
for file_name in files:
    if any(df['column_name'].str.startswith(file_name)):
        pass
    else:
        print(f"Missed name: {file_name}")
        with open('missed_names.txt', 'a') as f:
            f.write(file_name + '\n')