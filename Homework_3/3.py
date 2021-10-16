def my_func(arg1, arg2, arg3):
    my_list = [arg1, arg2, arg3]
    return 'Сумма двух наибольших чисел равна ' + str(sum(sorted(my_list)[1:]))


def main():
    print(my_func(int(input('Введите первое число ')), int(input('Введите второе число ')),
                  int(input('Введите третье число '))))


if __name__ == '__main__':
    main()
