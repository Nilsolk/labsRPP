import random


def input_int(num:int):
    while True:
        try:
            return int(input(num))
        except ValueError:
            print("Error not num")


def create_list(name):
    print(f"\nСписок {name}:")
    print("1 - ввод с клавиатуры")
    print("2 - случайная генерация")

    while True:
        choice = input("Ваш выбор: ")
        if choice in ("1", "2"):
            break
        print("Ошибка! Введите 1 или 2.")

    n = input_int(f"Введите количество элементов списка {name}: ")
    while n < 0:
        print("Ошибка! Количество не может быть отрицательным.")
        n = input_int(f"Введите количество элементов списка {name}: ")

    lst = []

    if choice == "1":
        for i in range(n):
            lst.append(input_int(f"{name}[{i}] = "))
    else:
        left = input_int("Левая граница случайных чисел: ")
        right = input_int("Правая граница случайных чисел: ")
        while left > right:
            print("Ошибка! Левая граница больше правой.")
            left = input_int("Левая граница случайных чисел: ")
            right = input_int("Правая граница случайных чисел: ")
        for _ in range(n):
            lst.append(random.randint(left, right))

    return lst


def print_list(name, lst):
    print(f"{name}[{len(lst)}]:", *lst)


def in_list_manual(lst, x):
    for elem in lst:
        if elem == x:
            return True
    return False


def method_without_std(A, B):
    """
    Метод без стандартных функций.
    Удаляет цепочки нечетных элементов, если в них нет элементов из B.
    """
    result = []
    i = 0

    while i < len(A):
        if A[i] % 2 == 0:
            result.append(A[i])
            i += 1
        else:
            start = i
            found = False

            while i < len(A) and A[i] % 2 != 0:
                if in_list_manual(B, A[i]):
                    found = True
                i += 1

            if found:
                j = start
                while j < i:
                    result.append(A[j])
                    j += 1

    return result


def method_with_std(A, B):
    result = []
    i = 0

    while i < len(A):
        if A[i] % 2 == 0:
            result.append(A[i])
            i += 1
        else:
            start = i
            while i < len(A) and A[i] % 2 != 0:
                i += 1

            part = A[start:i]
            keep = False
            for x in part:
                if x in B:
                    keep = True
                    break

            if keep:
                result += part

    return result


def main():
    A = create_list("A")
    B = create_list("B")

    print("\nИсходные списки:")
    print_list("A", A)
    print_list("B", B)

    print("\nВыберите метод:")
    print("1 - без стандартных функций")
    print("2 - со стандартными функциями")

    while True:
        choice = input("Ваш выбор: ")
        if choice in ("1", "2"):
            break
        print("Ошибка! Введите 1 или 2.")

    if choice == "1":
        A_new = method_without_std(A, B)
    else:
        A_new = method_with_std(A, B)

    print("\nРезультат:")
    print_list("A", A_new)


main()
