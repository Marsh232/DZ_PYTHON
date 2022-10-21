def numberic(nf_file, nl_file):
    f_file = open(nf_file, encoding='utf-8')
    l_file = open(nl_file, 'w+', encoding='utf-8')
    n = 1
    for line in f_file.readlines():
        l_file.writelines(str(n)+ ' ' + line)
        n += 1
    f_file.close()
    l_file.close()

if __name__ == '__main__':
    file1 = input("Введите имя первого: ")
    file2 = input("Введите имя конечного файла: ")
    numberic(file1, file2)