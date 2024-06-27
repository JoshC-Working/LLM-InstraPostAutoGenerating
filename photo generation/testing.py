from PIL import Image
from openpyxl import Workbook
from openpyxl.drawing.image import Image as XLImage


def insert_image_to_excel(image_path, excel_path, sheet_name, cell, sizing_percentage = None ):
    # 打開圖片
    image = Image.open(image_path)

    # 打開 Excel 文件
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = sheet_name

    # 將圖片插入到 Excel 中的指定單元格
    sheet[cell] = ""
    img = XLImage(image)
    img.anchor = cell

    if sizing_percentage is not None:
        img.width = int(img.width*sizing_percentage/100)
    
        img.height = int(img.height*sizing_percentage/100)

    sheet.add_image(img)

    # 保存 Excel 文件
    workbook.save(excel_path)
    print(f"圖片已成功插入到 {excel_path} 的 {sheet_name} 中的單元格 {cell}。")

# 執行示例
image_path = "photo generation/photos/photo_1.jpg"  # 替換為你的圖片路徑
excel_path = "photo generation/happy.xlsx"  # 替換為你的 Excel 文件路徑
sheet_name = "Sheet1"  # 替換為你要插入圖片的工作表名稱
cell = "A1"  # 替換為你要插入圖片的目標單元格
insert_image_to_excel(image_path, excel_path, sheet_name, cell, 10)