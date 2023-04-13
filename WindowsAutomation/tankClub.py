import os
import datetime
import pandas as pd
import glob
import shutil
import re

os.chdir("Y:/XPRESS FOTO FOTO")
now = datetime.datetime.now()
month_year = now.strftime("%B %Y")
if not os.path.exists(month_year):
    os.makedirs(month_year)
    print("Directory succesfully created.")
else:
    print("The directory of the month already exists.")
os.chdir(month_year)
if not os.path.exists("_FOTOS_PENDIENTES_"):
    os.mkdir("_FOTOS_PENDIENTES_")
else:
    print("The directory '_FOTOS_PENDIENTES_' already exists.")
if not os.path.exists("_REPOSICIONES_"):
    os.mkdir("_REPOSICIONES_")
else:
    print("The directory '_REPOSICIONES_' already exists.")
newday = input("Ready Lets Go: ")
os.makedirs(os.path.join(newday, "CONTENIDOS"))
os.makedirs(os.path.join(newday, "CONTENIDOS", "TAPAS"))
os.makedirs(os.path.join(newday, "CONTENIDOS", "TAPAS_BLANDAS"))
os.makedirs(os.path.join(newday, "CONTENIDOS", "PHOTOBOOK_HD"))
os.makedirs(os.path.join(newday, "FOTOS"))
os.makedirs(os.path.join(newday, "FOTOS", "10X15"))
os.makedirs(os.path.join(newday, "FOTOS", "13X18"))
os.makedirs(os.path.join(newday, "FOTOS", "16X23"))
os.makedirs(os.path.join(newday, "MONTAJES_4X0"))
os.makedirs(os.path.join(newday, "LIENZOS"))
os.chdir(newday)
os.chdir("../..")
xl = glob.glob("*.xlsx")[0]
df = pd.read_excel(xl, usecols=[0])
print(df)
src_fr = "Z:/FOTOFOTO/Fotopresentes"
dst_fr = "Y:/XPRESS FOTO FOTO/" + newday
for filename in os.listdir(src_fr):
    for index, row in df.iterrows():
        if str(row[0]) in filename:
            try:
                shutil.copy(os.path.join(src_fr, filename), dst_fr)
            except PermissionError as e:
                print(f"Permission denied: {e}")
                continue
