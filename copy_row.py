from return_data_file import data_file


def copy_row():
    data, nf = data_file()
    result_data, result_nf = data_file()
    count_rows = len(data)
    if count_rows == 0:
        print("Файл пусто!")
    else:
        number_row = int(input(f"Введите номер строки "
                               f"от 1 до {count_rows}: "))
        while number_row < 1 or number_row > count_rows:
            number_row = int(input(f"Ошибка!"
                                   f"Введите номер строки "
                                   f"от 1 до {count_rows}: "))

    raw_data_to_copy = data[number_row - 1]
    row_to_copy = ';'.join(raw_data_to_copy.split(';')[1:])
    now_number_row = len(result_data) + 1
    with open(f'db/data_{result_nf}.txt', 'a', encoding='utf-8') as file:
        file.write(f'{now_number_row};{row_to_copy}')

    print("Данные успешно записаны!")