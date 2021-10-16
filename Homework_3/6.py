def int_func(word):
    latin_char = 'abcdefghijklmnopqrstuvwxyz'
    if not set(word).difference(latin_char):
        return word.title()
    else:
        return False


def main():
    words = input('Введите строку из слов разделенных пробелами ').split()
    final_string = ''
    for word in words:
        res = int_func(word)
        if res:
            final_string += res + ' '
    print(final_string[:-1])


if __name__ == '__main__':
    main()
