"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai
import pandas as pd
import time 
import openpyxl
from bs4 import BeautifulSoup
from markdown import markdown
from tool import copy_file

# def remove_markdown(text):
#     html = markdown.markdown(text)
#     plain_text = ''.join(plain_text for plain_text in html.itertext())
#     return plain_text

genai.configure(api_key="AIzaSyD2gXw17sww_XhHCmDFdxbyUAaYnsrDYtA")

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 600,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE"
  },
]
# safety_settings = [
#   {
#     "category": "HARM_CATEGORY_HARASSMENT",
#     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
#   },
#   {
#     "category": "HARM_CATEGORY_HATE_SPEECH",
#     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
#   },
#   {
#     "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
#     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
#   },
#   {
#     "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
#     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
#   },
# ]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
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

##
def cross_check(topic:str, response:str, check_prompt1 ,check_prompt2,check_prompt3 ) -> int: 
  flag = False
  while (flag is False):
    time.sleep(time_stop)
    eval = model.generate_content(check_prompt1+topic+check_prompt2+str(response)+check_prompt3)
    time.sleep(time_stop)
    value = markdown_format_off(eval.text)
    print(value)
    if(len(value)<=3 ):
      flag = True

  print("Check_percentage: "+ eval.text)
  if int(value) >= 70:
     return 1
  else: 
     return 0
   
   


## Hyperparameter Initialization ## 

responses = []

comp_prompt_1 = '''Could you please write a description about the following topic?'''
comp_prompt_2 = '''Only output the description.'''

titles = read_excel_rows("target.xlsx", has_header = False)
titles = [(i[0] if (len(i)>=1) else "") for i in titles]
# titles = ["How to launch a startup?", "Startup Funding Rounds", "Startup Funding Options"]
target_file = "target.xlsx"
time_stop = 4




# comp_prompt = '''Give me an short introduction of the following country. Only incliude the introduction in the response.'''








print("### Titles")
print(titles)
print("\n\n")




## Generatingq Response ## 
counter = 0
check_values= [[],]
i = 0
while i < len(titles):
  counter += 1
  print("### Prompt: "+ str(i+1) +"_" +str(counter))
  

  ## Prompt
  response = model.generate_content(comp_prompt_1+" "+ titles[i]+" "+comp_prompt_2)
  time.sleep(time_stop)

  ## Response Information Checking
  print(response)
  print(response.prompt_feedback)
  print(response.candidates[0].finish_reason)
  print(response.candidates[0].safety_ratings)
  print("response valid: "+ str(len(response.parts))) # 1: non-empty response, 0: emtpy response


  ## Check if the return response has a text part
  if(len(response.parts)!=0):
    text = markdown_format_off(response.text)
    print(type(text))
    responses.append(text)
    time.sleep(time_stop)
    check_value = cross_check(titles[i],
                              text, 
                              '''The title: ''',
                              '''\nThe description: ''',
                              '''\nCould you give me a accuracy rate out of 100 of 
                              how correlated the description and the title are. Only output the the accuracy rate, which is in integer''' )
    time.sleep(time_stop)
    print("Check_value_"+str(i)+": "+str(check_value))
    check_values[i].append(check_value) 

    if (check_value) ==1:
        i += 1
        check_values.append([])
        counter = 0


  
  print("--"*30)
    
     
copy_file(target_file)
write_excel_to_rows("copy_"+ target_file, responses, 2)

for i in responses:
   print(i)

