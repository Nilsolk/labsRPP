import numpy as np


def input_size(text):
    while True:
        try:
            x = int(input(text))
            if x > 0:
                return x
            else:
                print("Введите число больше 0")
        except ValueError:
            print("Ошибка ввода")


def create_matrix(n, m):
    return np.random.randint(-10, 11, (n, m))


def make_result_matrix(a):
    n, m = a.shape

    b = np.zeros((n + 1, m + 1), dtype=int)
    b[:n, :m] = a

    for i in range(n):
        count = 0
        for j in range(m):
            if a[i][j] < 0:
                count += 1
        b[i][m] = count

    for j in range(m):
        count = 0
        for i in range(n):
            if a[i][j] < 0:
                count += 1
        b[n][j] = f"count"

    total = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] < 0:
                total += 1
    b[n][m] = total

    return b


def save_to_file(a, b, filename):
    # Сохранение в файл с выравниванием по столбцам
    with open(filename, "w", encoding="utf-8") as f:
        f.write("Исходная матрица:\n")
        for row in a:
            for x in row:
                f.write(f"{x:4d}")
            f.write("\n")

        f.write("\nРезультат:\n")
        for row in b:
            for x in row:
                f.write(f"{x:4d}")
            f.write("\n")


def print_matrix(name, matrix):
    print(name)
    for row in matrix:
        for x in row:
            print(f"{x:4d}", end="")
        print()



def main():
    n = input_size("Введите количество строк N: ")
    m = input_size("Введите количество столбцов M: ")

    a = create_matrix(n, m)
    b = make_result_matrix(a)

    print_matrix("\nИсходная матрица:", a)
    print_matrix("\nРезультирующая матрица:", b)


    save_to_file(a, b, "lab_2/result.txt")

main()
