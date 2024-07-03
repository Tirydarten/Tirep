def clear_names(file_name: str) -> list:
    """Функция для очистки имён от лишних символов"""
    new_name_list = list()
    with open(r"C:\Users\User\PycharmProjects\9.2_basics_git_practice\data\names.txt", "r", encoding='utf-8') as names_file:
        names_list = names_file.read().split()
        for name_item in names_list:
            new_name = ''
            for symbol in name_item:
                if symbol.isalpha():
                    new_name += symbol
            if new_name.isalpha():
                new_name_list.append(new_name)
    return new_name_list


if __name__ == '__main__':
    cleared_name = clear_names('names.txt')

    for i in cleared_name:
        print(i)
