def main():
    rus_dict = {"Один": "One", "Два": "Two", "Три": "Three", "Четыре": "Four"}
    with open('4n.txt', 'w', encoding='utf-8') as nf:
        with open('4m.txt', 'r', encoding='utf-8') as mf:
            file_lines = mf.readlines()
            for line in file_lines:
                rus_numeral = line.split()[0]
                nf.write(f'{line.replace(rus_numeral, rus_dict[rus_numeral])}')


if __name__ == '__main__':
    main()
