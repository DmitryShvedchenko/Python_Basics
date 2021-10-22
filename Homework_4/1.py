from sys import argv


def salary():
    try:
        time, rate, bonus = map(float, argv[1:])
        print(f"Salary - {time * rate + bonus}")
    except ValueError:
        print("Введите 3 числа. Не строки и Не пустой ввод")


if __name__ == '__main__':
    salary()
