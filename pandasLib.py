# Script to learn the pandas library functionality

import pandas as pd
import os

script_path = os.path.abspath(__file__)                # to obtain the script absolute path
script_dir = os.path.dirname(script_path)              # to extract the directory containing the script
# print("The script absolute path is:", script_path)
# print("The directory containing the script is:", script_dir)

files_path = os.path.join(script_dir, "Pokemon")
csv_file = pd.read_csv(os.path.join(files_path, "pokemon.csv"))
print("All CSV:\n", csv_file)
print("\nFirst 3 rows:\n", csv_file.head(3))
print("\nLast 3 rows:\n", csv_file.tail(3))
print("\nAll name:\n", csv_file["Name"])
print("\nAll name, generation and legendary:\n", csv_file[["Name", "Generation", "Legendary"]])

for index, row in csv_file.iterrows():  # to loop on all rows
    print("Pokèmon:", row["Name"])

for item in csv_file.columns:   # to loop on all columns
    print("Item:", item)

excel_file = os.path.join(files_path, "pokemon.xlsx")
csv_file.to_excel(excel_file, index=False)  # to transform a csv to a excel