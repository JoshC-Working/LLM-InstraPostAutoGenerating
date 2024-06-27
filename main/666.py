from openpyxl import Workbook
from openpyxl.drawing.image import Image

from openpyxl import Workbook
from openpyxl.drawing.image import Image
from PIL import Image as PILImage

def resize_image(image_path, target_size):
    img = PILImage.open(image_path)
    img.thumbnail(target_size, PILImage.LANCZOS)
    return img

def insert_image_into_excel(image_path, excel_path, sheet_name, cell_range):
    img = Image(image_path)
    resized_img = resize_image(image_path, (100, 100))  # 調整圖片大小為 100x100，你可以更改大小
    wb = Workbook()
    ws = wb.active
    ws.append(["Image"])
    cell = ws[cell_range]
    ws.add_image(img, cell.coordinate)
    wb.save(excel_path)

 
insert_image_into_excel("main/photos/img.jpg", "main/photo.xlsx", "Sheet1", "A1")

