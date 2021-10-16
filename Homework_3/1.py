def div(num_1, num_2):
    try:
        num_1, num_2 = int(num_1), int(num_2)
        div_num = num_1 / num_2
    except ValueError:
        return 'Пожалуйста, введите числа'
    except ZeroDivisionError:
        return 'Второе число должно отличаться от нуля'
    return round(div_num, 4)


def main():
    print(div(input('Введите первое число - '), input('Введите второе число - ')))


if __name__ == '__main__':
    main()
