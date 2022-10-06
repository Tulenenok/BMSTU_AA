from time import time
from tools import generate_random_string, bcolors
from algorithms import *
from prettytable import PrettyTable
from tools import bcolors

COUNT_REPEATS = 3000
SEC_RATIO = 1000000


def _measure_time_wrap(source_len, target_len, func, n=COUNT_REPEATS):
    """
        Обертка для замера времени работы функций

        source_len - длина строка-источник
        target_len - длина целевой строки
        func - функция, время работы которой мы хотим замерить
        n - количество повторений замера
    """
    gen_strings = [(generate_random_string(source_len),
                    generate_random_string(target_len)) for i in range(n)]

    t1 = time()
    for s in gen_strings:
        func(s[0], s[1])
    t2 = time()

    return (t2 - t1) / n * SEC_RATIO


def measure_time_l(source_len, target_len, n=COUNT_REPEATS):
    """ Замер времени для расстояния Левенштейна """
    return _measure_time_wrap(source_len, target_len, non_recursive_levenshtein, n)


def measure_time_dl(source_len, target_len, n=COUNT_REPEATS):
    """ Замер времени для расстояния Дамерау-Левенштейна """
    return _measure_time_wrap(source_len, target_len, non_recursive_damerau_levenshtein, n)


def measure_time_rdl(source_len, target_len, n=COUNT_REPEATS):
    """ Замер времени для расстояния рекурсивного Дамерау-Левенштейна """
    return _measure_time_wrap(source_len, target_len, recursive_damerau_levenshtein, n)


def measure_time_rdl_cache(source_len, target_len, n=COUNT_REPEATS):
    """ Замер времени для расстояния рекурсивного Дамерау-Левенштейна с кешем """
    return _measure_time_wrap(source_len, target_len, recursive_damerau_levenshtein_with_cache, n)


MEASURE_LENS = (
    (0, 0),
    (1, 1),
    (3, 3),
    (5, 5),
    (10, 10),
    (25, 25),
    (50, 50),
    # (100, 100)
)

SECTIONS = (
    (measure_time_l, '\nРасстояние Левенштейна'),
    (measure_time_dl, '\nРасстояние Дамерау-Левенштейна'),
    (measure_time_rdl, '\nРекурсивное расстояние Дамерау-Левенштейна'),
    (measure_time_rdl_cache, '\nРекурсивное расстояние Дамерау-Левенштейна с кешем')
)

OUTPUT_FILE_PREFIX = 'out/res_time'


def measure_time_exp():
    print(f'{bcolors.WARNING}PROCESSING', end=' ')

    result_table = PrettyTable()
    columns = [f'{bcolors.OKCYAN}Algorithm{bcolors.ENDC}'] + [f'{bcolors.OKCYAN}{m_len}{bcolors.ENDC}' for m_len in MEASURE_LENS]

    name_algs = ['Levenshtein', 'Damerau-Levenshtein',
                 'Recursive Damerau-Levenshtein', 'Recursive Damerau-Levenshtein with cache']
    result_table.add_column(columns[0], name_algs)

    for i, m_len in enumerate(MEASURE_LENS):
        print('.', end='')
        res = []

        for j, s in enumerate(SECTIONS):
            print('.', end='')
            func, title = s
            if j == 2 and m_len[0] >= 10 or j == 3 and m_len[0] > 10:
                res.append('-')
            else:
                res.append(f'{func(m_len[0], m_len[1]): 3.3f}')

        result_table.add_column(columns[i + 1], res)

        with open(f'{OUTPUT_FILE_PREFIX}_{m_len[0]}_{m_len[1]}.txt', 'w') as f:
            for r in res:
                f.write(f'{r}' + '\n')
    print(f'{bcolors.OKGREEN} SUCCESS{bcolors.ENDC}')
    print(result_table)
    print()