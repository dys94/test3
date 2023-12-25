from os.path import exists
from csv import DictReader, DictWriter

class LenNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt

class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt

def get_info():
    print("Введите данные")

    is_valid_name = False
    while not is_valid_name:
        try:
            first_name = input("Имя: ")
            if len(first_name) < 2:
                raise NameError("Длина имени должна быть больше 1.")
            else:
                is_valid_name = True
        except NameError as err:
            print(err)
            continue

    last_name = input("Фамилия: ")

    is_valid_phone = False
    while not is_valid_phone:
        try:
            phone_number = int(input("Телефон: "))
            if len(str(phone_number)) != 11:
                raise LenNumberError("Неверная длина номера.")
            else:
                is_valid_phone = True
        except ValueError:
            print("Не валидный номер.")
            continue
        except LenNumberError as err:
            print(err)
            continue

    return [first_name, last_name, phone_number]

def create_file(file_name):
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, ["Имя", "Фамилия", "Телефон"])
        f_writer.writeheader()

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8', newline='') as data:
        f_reader = DictReader(data)
        return list(f_reader)

def write_file(file_name, my_list):
    res = read_file(file_name)
    for line in res:
        if line["Телефон"] == str(my_list[2]):
            print("Телефон уже записан.")
            return
    obj = {'Имя': my_list[0], 'Фамилия': my_list[1], 'Телефон': my_list[2]}
    res.append(obj)
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, ["Имя", "Фамилия", "Телефон"])
        f_writer.writeheader()
        f_writer.writerows(res)

def copy_data(source_file, destination_file, row_number):
    source_data = read_file(source_file)
    if 1 <= row_number <= len(source_data):
        obj = source_data[row_number - 1]
        dest_data = read_file(destination_file)
        dest_data.append(obj)
        with open(destination_file, 'w', encoding='utf-8', newline='') as data:
            f_writer = DictWriter(data, ["Имя", "Фамилия", "Телефон"])
            f_writer.writeheader()
            f_writer.writerows(dest_data)
        print(f"Данные из строки {row_number} успешно скопированы.")
    else:
        print("Неверный номер строки.")

file_name = 'phone.csv'
def main():
    while True:
        command = input("Введите команду: ")
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name, get_info())
        elif command == 'r':
            if not exists(file_name):
                print("Файл отсутствует.")
                continue
            print(read_file(file_name))
        elif command == 'c':
            source_file = input("Введите имя исходного файла: ")
            destination_file = input("Введите имя файла назначения: ")
            row_number = int(input("Введите номер строки для копирования: "))
            copy_data(source_file, destination_file, row_number)

main()