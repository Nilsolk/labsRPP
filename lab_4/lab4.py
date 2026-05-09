import os
import csv


class Person:
    def __init__(self, name):
        self.name = name

    def __setattr__(self, key, value):
        if key == "name" and value == "":
            raise ValueError("Пустое имя")
        object.__setattr__(self, key, value)

    def __repr__(self):
        return self.name


class Patient(Person):
    pass


class Doctor(Person):
    pass


class Visit:
    def __init__(self, number, patient, doctor, reason, duration):
        self.number = number
        self.patient = patient
        self.doctor = doctor
        self.reason = reason
        self.duration = duration

    def __setattr__(self, key, value):
        if key == "number" and value <= 0:
            raise ValueError("Номер должен быть больше 0")
        if key == "duration" and value < 0:
            raise ValueError("Длительность не может быть отрицательной")
        object.__setattr__(self, key, value)

    def __repr__(self):
        return f"{self.number} {self.patient} {self.doctor} {self.reason} {self.duration}"

    @staticmethod
    def from_dict(row):
        return Visit(
            int(row["№"]),
            Patient(row["ФИО пациента"]),
            Doctor(row["ФИО врача"]),
            row["причина обращения"],
            int(row["длительность"])
        )

    def to_dict(self):
        return {
            "№": self.number,
            "ФИО пациента": self.patient.name,
            "ФИО врача": self.doctor.name,
            "причина обращения": self.reason,
            "длительность": self.duration
        }


class Registry:
    def __init__(self):
        self.data = []
        self.i = 0

    def __setattr__(self, key, value):
        object.__setattr__(self, key, value)

    def __repr__(self):
        return f"Записей: {len(self.data)}"

    def add(self, visit):
        self.data.append(visit)

    def __getitem__(self, index):
        return self.data[index]

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i < len(self.data):
            x = self.data[self.i]
            self.i += 1
            return x
        raise StopIteration

    def generator(self, min_duration):
        for visit in self.data:
            if visit.duration > min_duration:
                yield visit

    @staticmethod
    def count_files(path):
        count = 0
        if not os.path.exists(path):
            return 0
        for name in os.listdir(path):
            if os.path.isfile(os.path.join(path, name)):
                count += 1
        return count

    @staticmethod
    def read_csv(filename):
        reg = Registry()
        if not os.path.exists(filename):
            return reg

        with open(filename, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                reg.add(Visit.from_dict(row))
        return reg

    @staticmethod
    def save_csv(filename, reg):
        with open(filename, "w", encoding="utf-8", newline="") as f:
            fields = ["№", "ФИО пациента", "ФИО врача", "причина обращения", "длительность"]
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            for visit in reg:
                writer.writerow(visit.to_dict())


def print_data(data):
    for x in data:
        print(x)


def main():
    folder = "lab_4/count_folder"
    filename = "lab_4/data.csv"

    print("Количество файлов:", Registry.count_files(folder))

    reg = Registry.read_csv(filename)

    print("\nИсходные данные:")
    print_data(reg)

    print("\nСортировка по ФИО пациента:")
    print_data(sorted(reg.data, key=lambda x: x.patient.name))

    print("\nСортировка по длительности:")
    print_data(sorted(reg.data, key=lambda x: x.duration))

    n = int(input("\nВведите минимальную длительность: "))
    print("\nПодходящие записи:")
    print_data(reg.generator(n))


    ans = input("\nДобавить запись? (да/нет): ")
    if ans.lower() == "да":
        number = int(input("№: "))
        patient = Patient(input("ФИО пациента: "))
        doctor = Doctor(input("ФИО врача: "))
        reason = input("Причина обращения: ")
        duration = int(input("Длительность: "))

        reg.add(Visit(number, patient, doctor, reason, duration))
        Registry.save_csv(filename, reg)
        print("Сохранено.")


if __name__ == "__main__":
    main()

