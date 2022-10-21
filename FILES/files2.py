def scaning(n_file):
    file = open(n_file, encoding='utf-8')
    lst_stat = file.read().splitlines()
    fl_lst =[]
    for i in lst_stat:
        fl_lst.append(float(i))
    max_temp = max(fl_lst)
    min_temp = min(fl_lst)
    sr_temp = sum(fl_lst) / 828
    sort_fl_lst = list(set(fl_lst))
    sort_fl_lst.sort()
    print('Максимальная температура: ', max_temp)
    print('Минимальная температура: ', min_temp)
    print('Средняя температура: ', sr_temp)
    print('Уникальные значения: ', sort_fl_lst)

    file.close()

if __name__ == '__main__':
    n_file = 'temper.stat'
    scaning(n_file)