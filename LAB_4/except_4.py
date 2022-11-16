def cat(name_file1, name_file2, name_file3):
    try:
        file1 = open(name_file1, encoding='utf-8')
        file2 = open(name_file2, encoding='utf-8')
        file3 = open(name_file3,'w+', encoding='utf-8')
        for line in file1.readlines():
            file3.writelines(line)
        for line in file2.readlines():
            file3.writelines(line)
        file1.close()
        file2.close()
        file3.close()
    except BaseException:
        print("ОЙ ОШИБКА\n"
              "ВЫ ВВЕЛИ ЧТО-ТО НЕПРАВИЛЬНО")



if __name__ == "__main__":
    n_fl1 = input('Введите имя первого файла: ')
    n_fl2 = input('Введите имя второго файла: ')
    n_fl3 = input('Введите имя третьего файла в который будут соединены файлы 1 и 2: ')
    cat(n_fl1, n_fl2, n_fl3)