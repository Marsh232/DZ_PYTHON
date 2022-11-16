import os

def print_docs(directory):
    all_dir = os.walk(directory)
    for catal in all_dir:
        print(f'Папка {catal[0]} содержит:')
        print(f'Директории: {", ".join([folder for folder in catal[1]])}')
        print(f'Файлы: {", ".join([file for file in catal[2]])}')
        print('\n')



if __name__=='__main__':
    direct = input("Введите путь папки: ")
    print_docs(direct)