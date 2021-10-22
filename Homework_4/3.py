def main():
    multiplicity_list = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]
    print(multiplicity_list)


if __name__ == '__main__':
    main()
