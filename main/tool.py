import shutil
import os
import pandas as pd


def read_excel_rows(file_path, has_header = True):
    if has_header:  
      df = pd.read_excel(file_path)
    else:
      df = pd.read_excel(file_path, header = None )
    
    rows_list = df.values.tolist()
    return rows_list






def copy_file(file_name):
    source_path = file_name
    destination_path = f"copy_{file_name}"
    
    shutil.copy2(source_path, destination_path)
    print(f"File {file_name} copied successfully!")


file_to_copy = "example.txt"


# copy_file("wood.xlsx")