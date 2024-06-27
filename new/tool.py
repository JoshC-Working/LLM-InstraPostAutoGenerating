import shutil
import os
import re 



# class GeminiResponse:

#     def __init__(self, text:str = "", cross_check_index = [],   ):

#         pass 


#     pass
        

def split_response(text):
    # Initialize the dictionary to store extracted information
    info = {"caption": "", "Main Points1": "", "Main Points2": "", "Main Points3": ""}

    # Define the regex patterns for capturing the required sections
    caption_pattern = r"## Caption:(.*?)## Main Points:"
    main_points_pattern = r"## Main Points:\s*1\.\s*(.*?)\s*2\.\s*(.*?)\s*3\.\s*(.*)"

    # Search for the patterns in the text
    caption_match = re.search(caption_pattern, text, re.DOTALL)
    main_points_match = re.search(main_points_pattern, text, re.DOTALL)

    # Check if caption is found
    if caption_match:
        info["caption"] = caption_match.group(1).strip()
    else:
        return None
    
    # Check if main points are found
    if main_points_match:
        info["Main Points1"] = main_points_match.group(1).strip()
        info["Main Points2"] = main_points_match.group(2).strip()
        info["Main Points3"] = main_points_match.group(3).strip()
    else:
        return None

    # Return the information as a list
    return [info["caption"], info["Main Points1"], info["Main Points2"], info["Main Points3"]]





def copy_file(file_name):
    source_path = file_name
    destination_path = f"copy_{file_name}"
    
    shutil.copy2(source_path, destination_path)
    print(f"File {file_name} copied successfully!")


file_to_copy = "example.txt"


# copy_file("wood.xlsx")
