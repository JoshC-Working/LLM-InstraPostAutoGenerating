from openpyxl import Workbook

def save_to_excel(string_data, file_path, row, column):
    # 創建一個新的Workbook
    wb = Workbook()
    
    # 選擇第一個工作表
    ws = wb.active
    
    # 將字符串放入指定的單元格
    ws.cell(row=row, column=column, value=string_data)
    
    # 儲存Workbook到指定的路徑
    wb.save(file_path)
    print(f"Data saved to {file_path}")

save_to_excel("3333","photo generation/test.xlsx", 2, 3 )