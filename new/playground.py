from PIL import Image, ImageDraw, ImageFont
from PIL import Image
from openpyxl import Workbook
from openpyxl.drawing.image import Image as XLImage
import pandas as pd
import textwrap
import os
from openpyxl import load_workbook
from PIL import Image as PILImage
import time

from openpyxl.drawing.image import Image as XLImage


def resize_images_in_folder(folder_path, max_width, max_height):
    # 确保输出文件夹存在
    # output_folder = os.path.join(folder_path, "resized")
    # os.makedirs(output_folder, exist_ok=True)
    
    # 遍历文件夹中的所有 PNG 文件
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".png"):
            image_path = os.path.join(folder_path, filename)
            with Image.open(image_path) as img:
                original_width, original_height = img.size
                
                # 计算比例
                ratio = min(max_width / original_width, max_height / original_height)
                new_width = int(original_width * ratio)
                new_height = int(original_height * ratio)
                
                # 调整图像大小
                resized_img = img.resize((new_width, new_height))
                
                # 保存调整大小后的图像到输出文件夹
                resized_image_path = folder_path+"/"+filename
                print(resized_image_path)
                resized_img.save(resized_image_path)
                print(f"Resized {filename} and saved to {resized_image_path}")


resize_images_in_folder("new/output_photos", 300, 300)