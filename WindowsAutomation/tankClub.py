import os
import datetime
import pandas as pd
import glob
import shutil
import re

now = datetime.datetime.now()
month_year = now.strftime("%B %Y")
if not os.path.exists(month_year):
    os.makedirs(month_year)
    print("Directory succesfully created.")
else:
    print("The directory already exists.")
os.chdir(month_year)
os.mkdir("_FOTOS_PENDIENTES_")
os.mkdir("_REPOSICIONES_")
newday = input("Ready Lets Go: ")
os.mkdir(newday)
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
dst_folder = os.getcwd()
os.chdir("..")
xl = glob.glob("*.xlsx")[0]
df = pd.read_excel(xl, usecols=[0])
print(df)
wk_files = df
src_folder = "Z:/FOTOFOTO/Fotopresentes"
for root, dirs, files in os.walk(src_folder):
    for file in files:
        if file.endswith(".pdf"):
            for pattern in wk_files:
                if pattern in file:
                    shutil.copy(os.path.join(root, file), dst_folder)
                    break
for root, dirs, files in os.walk(src_folder):
    for file in files:
        if file.endswith(".pdf"):
            for pattern in wk_files:
                if pattern in file:
                    shutil.copy(os.path.join(root, file), dst_folder)
                    break
src_folder = "Z:/FOTOFOTO/Fotos/10x15"
for root, dirs, files in os.walk(src_folder):
    for file in files:
        for pattern in wk_files:
            if pattern in file:
                shutil.copy(os.path.join(root, file), dst_folder)
                break
src_folder = "Z:/FOTOFOTO/Fotos/13x18"
for root, dirs, files in os.walk(src_folder):
    for file in files:
        for pattern in wk_files:
            if pattern in file:
                shutil.copy(os.path.join(root, file), dst_folder)
                break
src_folder = "Z:/FOTOFOTO/Fotos/16x23"
for root, dirs, files in os.walk(src_folder):
    for file in files:
        for pattern in wk_files:
            if pattern in file:
                shutil.copy(os.path.join(root, file), dst_folder)
                break
src_folder = "Z:/FOTOJAPON"
for root, dirs, files in os.walk(src_folder):
    for file in files:
        if file.endswith(".pdf"):
            for pattern in wk_files:
                if pattern in file:
                    shutil.copy(os.path.join(root, file), dst_folder)
                    break
os.chdir(month_year + "/" + newday)
os.chdir(".\\CONTENIDOS\\PHOTOBOOK_HD\\")
for file in os.listdir("."):
    if "cuero" in file:
        shutil.move(file, "..\\..\\CONTENIDOS\\PHOTOBOOK_HD\\")
os.chdir(".\\CONTENIDOS\\TAPAS_BLANDAS\\")
for file in os.listdir("."):
    if "cover_photobook_clasico_tapablanda" in file:
        shutil.move(file, "..\\..\\CONTENIDOS\\TAPAS_BLANDAS\\")
os.chdir(".\\CONTENIDOS\\TAPAS\\")
for file in os.listdir("."):
    if "cover" in file:
        shutil.move(file, "..\\..\\CONTENIDOS\\TAPAS\\")
os.chdir(".")
for file in os.listdir("."):
    if "calendario_pared_mp" in file:
        shutil.move(file, "..\\CONTENIDOS\\")
os.chdir(".")
for file in os.listdir("."):
    if "photobook" in file:
        shutil.move(file, "..\\CONTENIDOS\\")
os.chdir(".")
for file in os.listdir("."):
    if "fotorevista" in file:
        shutil.move(file, "..\\CONTENIDOS\\")
os.chdir(".")
for file in os.listdir("."):
    if "escritorio" in file:
        shutil.move(file, "..\\CONTENIDOS\\")
os.chdir(".\\MONTAJES_4X0\\")
for file in os.listdir("."):
    if "pared" in file or "poster" in file or "retablo" in file or "retrato" in file or "pack" in file:
        shutil.move(file, "..\\..\\MONTAJES_4X0\\")
os.chdir(".\\LIENZOS\\")
for file in os.listdir("."):
    if "lienzo" in file:
        shutil.move(file, "..\\..\\LIENZOS\\")
for root, dirs, files in os.walk(".", topdown=False):
    for dir in dirs:
        if not os.listdir(os.path.join(root, dir)):
            os.rmdir(os.path.join(root, dir))
os.chdir("FOTOS")
for root, dirs, files in os.walk(".", topdown=False):
    for file in files:
        match = re.search(r"_x(\d+)_", file)
        if match:
            multiplier = int(match.group(1))
            for i in range(multiplier-1):
                shutil.copy(file, os.path.join(root, f"{os.path.splitext(file)[0]}_{i+1}{os.path.splitext(file)[1]}"))
src_path = "Y:\\XPRESS FOTO FOTO\\_INDEX_"
files1 = ["INDEX_1.pdf", "INDEX_2.pdf"]
files2 = ["INDEX_3.pdf", "INDEX_4.pdf"]
files3 = ["INDEX_5.pdf", "INDEX_6.pdf"]
#dst_path1 = f"Y:\\XPRESS FOTO FOTO\\{directory}\\{newday}\\FOTOS\\10X15"
#dst_path2 = f"Y:\\XPRESS FOTO FOTO\\{directory}\\{newday}\\FOTOS\\13X18"
#dst_path3 = f"Y:\\XPRESS FOTO FOTO\\{directory}\\{newday}\\FOTOS\\16X23"
'''
os.chdir(src_path)
for file in files1:
    shutil.move(file, dst_path1)
for file in files2:
    shutil.move(file, dst_path2)
for file in files3:
    shutil.move(file, dst_path3)
'''