import pdf2docx
import docx2pdf
import os
from PIL import Image
choice = 0
while choice != 5:
    print(f"Текущий каталог: {os.getcwd()}\n\n"
          f"Выберите действие:\n\n"
          f"0. Сменить рабочий каталог\n"
          f"1. Преобразовать PDF в Docx\n"
          f"2. Преобразовать Doc/Docx в PDF\n"
          f"3. Произвести сжатие изображений\n"
          f"4. Удалить группу файлов\n"
          f"5. Выход\n\n")
    choice = int(input("Ваш выбор: "))
    if choice == 0:
        os.chdir(input("Введите нужную директорию: "))
    elif choice == 1:
        file_number = 1
        files_list = os.listdir(f"{os.getcwd()}")
        print("Список файлов с расширением .pdf в данном каталоге:\n\n")
        for i in range(len(files_list)):
            if files_list[i].endswith(".pdf"):
                print(f"{file_number}. {files_list[i]}")
                file_number += 1
        convert_choice = int(input("Введите номер файла для преобразования (чтобы преобразовать все файлы, введите 0): "))
#        # cv.convert(os.path.join(f"{os.getcwd()}", f"{files_list[convert_choice].rstrip('.pdf') + '.docx'})"))
        pdf2docx.parse(r"C:\Users\Student\Downloads\Теоретические материалы.pdf", r"C:\Users\Student\Downloads\Теоретические материалы.docx")
#    elif choice == 2:

#    elif choice == 3:

#    elif choice == 4:

#    else:
#        continue
