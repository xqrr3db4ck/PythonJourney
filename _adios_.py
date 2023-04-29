        try:
            if len(str(cell.value)) > max_length:
                max_length = len(str(cell.value))
        except:
            pass
    adjusted_width = (max_length + 2) * 1.1
    ws.column_dimensions[column].width = adjusted_width
wb.save('_1a1BMG_.xlsx')
fil1 = pd.read_excel('_1a1BMG_.xlsx', usecols=[1])
names = fil1.values.flatten().tolist()
dir_path = "./"
files = os.listdir(dir_path)
wb = openpyxl.load_workbook('_1a1BMG_.xlsx')
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
        ws.cell(row=i+2, column=2).fill = red_fill
wb.save('_1a1BMG_.xlsx')
