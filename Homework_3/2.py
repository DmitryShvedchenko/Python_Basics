def personal_inf(**kwargs):
    return ' '.join(kwargs.values())


def main():
    name = input('Введите имя - ')
    surname = input('Введите фамилию - ')
    birthday = input('Введите дату рождения - ')
    city = input('Введите город проживания - ')
    email = input('Введите email - ')
    phone = input('Введите номер телефона - ')
    print(personal_inf(name=name, surname=surname, birthday=birthday, city=city, email=email, phone=phone))


if __name__ == '__main__':
    main()
