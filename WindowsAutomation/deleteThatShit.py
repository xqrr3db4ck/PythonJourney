import os

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
