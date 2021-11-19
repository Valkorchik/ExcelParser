#Парсер табличного текста из Excel документа в текстовый файл.
import pandas as pd
print("Hello! Paste the way to your Excel file here:")
way_to_file=input()
print("Enter name of the sheet: ")
name_of_sheet=input()
print("Enter name of the colon or colons:  ")
name_of_colon=input().split()
with open('Excel.txt', 'w') as file:
    pd.concat(pd.read_excel(way_to_file,
                            sheet_name=[name_of_sheet],
                            usecols=name_of_colon)).to_string(file, index=False)
print("File 'Excel.txt' is ready")
print("-------------------------")
input()
