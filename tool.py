import shutil
import os


class GeminiResponse:

    def __init__(self, text:str = "", cross_check_index = [],   ):

        pass 


    pass
        







def copy_file(file_name):
    source_path = file_name
    destination_path = f"copy_{file_name}"
    
    shutil.copy2(source_path, destination_path)
    print(f"File {file_name} copied successfully!")


file_to_copy = "example.txt"


# copy_file("wood.xlsx")