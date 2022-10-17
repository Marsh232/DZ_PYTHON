def convert_mark():
    marks = {
        'A': 5, '5': 'A',
        'B': 4, '4': 'B',
        'C': 3, '3': 'C',
        'D': 2, '2': 'D'
    }
    try:
        mark = input('Введите оценку для конвертации: ')
        while mark != '':
            print(marks[mark])
            mark = input('Введите оценку для конвертации: ')
    except KeyError:
        print('Вы ввели неправильно\n'
              'Допустимые оценки:\n'
              'A = 5\n'
              'B = 4\n'
              'C = 3\n'
              'D = 2\n')




if __name__ == '__main__':
    convert_mark()