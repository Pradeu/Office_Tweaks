import pdf2docx
import docx2pdf
import os
from PIL import Image


def pdf2docx_convert(pdf_list, convert_choice):
    pdf_path = f'{os.getcwd()}' + r"/" + f"{pdf_list[convert_choice - 1]}"
    docx_path = f'{os.getcwd()}' + r"/" + f"{pdf_list[convert_choice - 1].replace('.pdf', '.docx')}"
    return pdf2docx.parse(pdf_path, docx_path)


def docx2pdf_convert(docx_list, convert_choice):
    docx_path = f'{os.getcwd()}' + r"/" + f"{docx_list[convert_choice - 1]}"
    pdf_path = f'{os.getcwd()}' + r"/" + f"{docx_list[convert_choice - 1].replace('.docx', '.pdf')}"
    return docx2pdf.convert(docx_path, pdf_path)


def file_delete(file_name):
    os.remove(f'{os.getcwd()}' + r"/" + f"{file_name}")
    print(f'Файл: {os.getcwd()}' + r"/" + f"{file_name} успешно удалён!")


choice = 0
while choice != 5:
    file_number = 1
    files_list = os.listdir(f"{os.getcwd()}")
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
        pdf_list = list()
        print("Список файлов с расширением .pdf в данном каталоге:\n\n")
        for i in range(len(files_list)):
            if files_list[i].endswith(".pdf"):
                print(f"{file_number}. {files_list[i]}")
                pdf_list.append(files_list[i])
                file_number += 1
        convert_choice = int(
            input("Введите номер файла для преобразования (чтобы преобразовать все файлы, введите 0): "))
        if convert_choice == 0:
            for i in range(len(pdf_list)):
                pdf2docx_convert(pdf_list, i)
        else:
            pdf2docx_convert(pdf_list, convert_choice)
    elif choice == 2:
        docx_list = list()
        print("Список файлов с расширением .docx в данном каталоге:\n\n")
        for i in range(len(files_list)):
            if files_list[i].endswith(".docx"):
                print(f"{file_number}. {files_list[i]}")
                docx_list.append(files_list[i])
                file_number += 1
        convert_choice = int(
            input("Введите номер файла для преобразования (чтобы преобразовать все файлы, введите 0): "))
        if convert_choice == 0:
            for i in range(len(docx_list)):
                docx2pdf_convert(docx_list, i)
        else:
            docx2pdf_convert(docx_list, convert_choice)
    elif choice == 3:
        pic_list = list()
        print("Список файлов с расширением .jpeg, .gif, .png, .jpg в данном каталоге:\n\n")
        for i in range(len(files_list)):
            if files_list[i].endswith(".jpeg") or files_list[i].endswith(".jpg") \
                    or files_list[i].endswith(".png") or files_list[i].endswith(".gif"):
                print(f"{file_number}. {files_list[i]}")
                pic_list.append(files_list[i])
                file_number += 1
        convert_choice = int(
            input("Введите номер файла для преобразования (чтобы преобразовать все файлы, введите 0): "))
        compress_choice = int(input("Введите процент сжатия (от 0 до 100%): "))
        pic_format = ".jpg"
        if files_list[convert_choice].endswith(".jpeg"):
            pic_format = ".jpeg"
        elif files_list[convert_choice].endswith(".png"):
            pic_format = ".png"
        elif files_list[convert_choice].endswith(".gif"):
            pic_format = ".gif"
        pic_path = f'{os.getcwd()}' + r"/" + f"{pic_list[convert_choice - 1]}"
        pic = Image.open(pic_path)
        pic.save(f'{os.getcwd()}' + r"/" + f"decompressed_image_{convert_choice}{pic_format}",
                 quality=100 - compress_choice, optimize=True)
    elif choice == 4:
        files_list_2 = list()
        print("Выберите действие:\n\n"
              "1. Удалить все файлы, начинающиеся на определенную подстроку\n"
              "2. Удалить все файлы, заканчивающиеся на определенную подстроку\n"
              "3. Удалить все файлы, содержащие определенную подстроку\n"
              "4. Удалить все файлы по расширению\n")
        action_choice = int(input("Введите номер действия: "))
        stroke_choice = input("Введите подстроку: ")
        if action_choice == 1:
            for i in range(len(files_list)):
                if files_list[i].startswith(stroke_choice):
                    file_delete(files_list[i])
        elif action_choice == 2:
            for i in range(len(files_list)):
                files_list_2.append(files_list[i])
            print(files_list_2)
            for i in range(len(files_list_2)):
                while True:
                    if not files_list_2[i].endswith("."):
                        files_list_2[i] = files_list_2[i][:len(files_list_2[i]) - 1]
                    else:
                        files_list_2[i] = files_list_2[i][:len(files_list_2[i]) - 1]
                        break
            print(files_list_2)
            for i in range(len(files_list)):
                if files_list_2[i].endswith(stroke_choice):
                    file_delete(files_list[i])
        elif action_choice == 3:
            for i in range(len(files_list)):
                if files_list[i].find(stroke_choice) != -1:
                    file_delete(files_list[i])
        elif action_choice == 4:
            for i in range(len(files_list)):
                if files_list[i].endswith(stroke_choice):
                    file_delete(files_list[i])
    elif choice != 5:
        print("Вы ввели неверный аргумент, попробуйте ещё раз\n")
        continue
