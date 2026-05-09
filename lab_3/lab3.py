import os
import csv


def count_files(folder_path):
    count = 0

    if not os.path.exists(folder_path):
        print("Папка не существует.")
        return 0

    for name in os.listdir(folder_path):
        full_path = os.path.join(folder_path, name)
        if os.path.isfile(full_path):
            count += 1

    return count


def read_csv_file(filename):
    # Читает данные из csv-файла в список словарей
    data = []

    if not os.path.exists(filename):
        print("Файл не найден.")
        return data

    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["№"] = int(row["№"])
            row["длительность"] = int(row["длительность"])
            data.append(row)

    return data


def print_data(data):
    # Выводит список словарей на экран
    if len(data) == 0:
        print("Нет данных.")
        return

    for item in data:
        print(
            item["№"],
            item["ФИО пациента"],
            item["ФИО врача"],
            item["причина обращения"],
            item["длительность"]
        )


def sort_by_string_field(data, field_name):
    # Сортировка по строковому полю
    return sorted(data, key=lambda x: x[field_name])


def sort_by_number_field(data, field_name):
    # Сортировка по числовому полю
    return sorted(data, key=lambda x: x[field_name])


def filter_data(data, min_duration):
    result = []

    for item in data:
        if item["длительность"] > min_duration:
            result.append(item)

    return result


def add_new_record(data):
    # Добавление новой записи
    print("\nВведите новую запись:")

    number = int(input("№: "))
    patient = input("ФИО пациента: ")
    doctor = input("ФИО врача: ")
    reason = input("Причина обращения: ")
    duration = int(input("Длительность: "))

    new_item = {
        "№": number,
        "ФИО пациента": patient,
        "ФИО врача": doctor,
        "причина обращения": reason,
        "длительность": duration
    }

    data.append(new_item)


def save_to_csv(filename, data):
    # Сохраняет данные обратно в csv-файл
    with open(filename, "w", encoding="utf-8", newline="") as file:
        fieldnames = ["№", "ФИО пациента", "ФИО врача", "причина обращения", "длительность"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for item in data:
            writer.writerow(item)


def main():
    # 1. Подсчёт файлов в папке
    files_count = count_files("lab_3/count_folder")
    print("Количество файлов в папке:", files_count)

    # 2. Работа с csv
    filename = "lab_3/data.csv"
    data = read_csv_file(filename)

    print("\nИсходные данные:")
    print_data(data)

    # 2.1 Сортировка по строковому полю
    sorted_by_patient = sort_by_string_field(data, "ФИО пациента")
    print("\nСортировка по ФИО пациента:")
    print_data(sorted_by_patient)

    # 2.2 Сортировка по числовому полю
    sorted_by_duration = sort_by_number_field(data, "длительность")
    print("\nСортировка по длительности:")
    print_data(sorted_by_duration)

    # 2.3 Фильтр по критерию
    min_duration = int(input("\nВведите минимальную длительность для отбора: "))
    filtered = filter_data(data, min_duration)
    print("\nЗаписи, где длительность больше заданного значения:")
    print_data(filtered)

    # 3. Добавление новой записи
    answer = input("\nДобавить новую запись? (да/нет): ")
    if answer.lower() == "да":
        add_new_record(data)
        save_to_csv(filename, data)
        print("Новая запись сохранена в файл.")


main()
