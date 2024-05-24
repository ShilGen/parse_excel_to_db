from openpyxl import load_workbook

#UPLOAD_FOLDER = '/parse_exel_to_db/uploads/'

def read_excel_file(file_path):
    try:
        workbook = load_workbook(filename=file_path)

        sheet = workbook.active

        data = []

        for row in sheet.iter_rows(values_only=True):
            data.append(row)
        with open("example.txt", "r") as f:
            pattern = f.readline()
        if " ".join(data[0]) != pattern:
            with open("log.txt", "a") as f:
                f.write(f"Шаблон таблицы поменялся.\nПуть до несоответствующего файла: {file_path}\n")
            return False
        return data

    except Exception as e:
        print(f"Ошибка при чтении файла Excel: {e}")
        return None

#read_excel_file(UPLOAD_FOLDER+"0.xlsx")

# file_path = "0.xlsx"  # Укажите путь к вашему файлу Excel
# excel_data = read_excel_file(file_path)
# if excel_data:
#     print("Данные из файла Excel:")
#     # print(*excel_data[0])
#     # with open("example.txt", "w") as f:
#     #     f.write(" ".join(excel_data[0]))
#     for row in excel_data:
#         print(row)
