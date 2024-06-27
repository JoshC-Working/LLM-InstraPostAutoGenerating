"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai
import pandas as pd
import time 
import openpyxl
# from IPython.display import Markdown 

from bs4 import BeautifulSoup
from markdown import markdown

# def remove_markdown(text):
#     html = markdown.markdown(text)
#     plain_text = ''.join(plain_text for plain_text in html.itertext())
#     return plain_text

genai.configure(api_key="AIzaSyBuwNQsR6Br8vknez_bAVpl0ANGmw_ko-Y")

# Set up the model
generation_config = {
  "temperature": 0.5,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 200,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
])


## Read Excel files
def read_excel_rows(file_path, has_header = True):
    if has_header:  
      df = pd.read_excel(file_path)
    else:
      df = pd.read_excel(file_path, header = None )
    
    rows_list = df.values.tolist()
    return rows_list

## Write the result in 

def write_excel_to_rows(file_path, data_list, col_index):
    # Load the Excel file
    workbook = openpyxl.load_workbook(file_path)

    # Select the first sheet
    sheet = workbook.active

    # Iterate through each row and write the list
    for row_index, row_data in enumerate(data_list):
        cell = sheet.cell(row=row_index + 1, column=col_index)
        cell.value = str(row_data)

    # Save the modified file
    workbook.save(file_path)

## Clean Blank Data
def clean_blank(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            pass

## 
def markdown_format_off(markdown_format_string):

  html = markdown(markdown_format_string)
  text = "".join(BeautifulSoup(html, features="html.parser").findAll(text=True))
  return text

# prompts = ["Hi? what can I do to become handsome? Give me three options"]


## Start


comp_prompt = '''I am currently trying to post Instagram posts for some titles. 
Please help me create content for the following titles that fit the title. 
Please only reply me the content that I am going to post for the title'''

titles = ["How to launch a startup?", "Startup Funding Rounds", "Startup Funding Options"]
# titles = read_excel_rows("target.xlsx", has_header = False)
print(titles)
# titles = ["Angry",]

responses = []
input_path = ""


titles = [(i[0] if (len(i)>=1) else "") for i in titles]
for i in range(len(titles)):
  response = model.generate_content(comp_prompt+" "+ titles[i])
  responses.append(markdown_format_off(response.text))
  time.sleep(2)

write_excel_to_rows("target_return.xlsx", responses, 2)
print(responses)
print(responses[0])

