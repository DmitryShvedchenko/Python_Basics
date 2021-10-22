def main():
    my_list = [5, 8, 45, 1, 2, 65, 9, 4, 32, 7, 3, 9, 10]
    result_list = [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]
    print(result_list)


if __name__ == '__main__':
    main()
