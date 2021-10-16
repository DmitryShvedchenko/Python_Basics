def my_simple_func(x, y):
    try:
        result = float(x) ** int(y)
    except TypeError:
        return "Ошибка"
    return str(result)


def my_complicated_func(x, y):
    x, y = float(x), int(y)
    try:
        if x <= 0 or y >= 0:
            return 'Ошибка x должен быть больше 0, а y должен быть меньше 0'
        else:
            result = 1
            for i in range(abs(y)):
                result *= 1 / x
            return str(result)
    except ValueError:
        return 'Введены некорректные данные'


def main():
    print('Результат простой функции ' + my_simple_func(input('Введите действиетльное положительное число '),
                                                        input('Введите целое отрицательное число ')))
    print('Результат простой функции ' + my_complicated_func(input('Введите действиетльное положительное число '),
                                                        input('Введите целое отрицательное число ')))


if __name__ == '__main__':
    main()
