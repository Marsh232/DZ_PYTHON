def sort_files(name_file, sort_file):
    file = open(name_file, encoding='utf-8')
    s_file = open(sort_file,'w+', encoding='utf-8')
    lst_file = file.read().splitlines()
    lst_file.sort()
    lst_file.pop(0)
    for line in lst_file:
        s_file.writelines(line+'\n')


if __name__ == '__main__':
    name_f = 'plan.txt'
    sort_f = 'sort_plan.txt'
    sort_files(name_f, sort_f)