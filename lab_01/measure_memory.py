import tracemalloc
from tools import generate_random_string
from algorithms import *
from tools import bcolors
from prettytable import PrettyTable

COUNT_REPEAT = 1000


def _measure_memory_wrap(source_len, target_len, func, n=COUNT_REPEAT):
    """
        Обертка для замера затрачиваемой памяти для работы функций

        source_len - длина строка-источник
        target_len - длина целевой строки
        func - функция, для которой мы хотим замерить количество затрачиваемой памяти
        n - количество повторов расчета
    """
    res_peak = 0
    for i in range(n):
        source = generate_random_string(source_len)
        target = generate_random_string(target_len)

        tracemalloc.start()
        func(source, target)
        curr, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        res_peak += peak / n

    return res_peak


def measure_memory_l(source_len, target_len, n=COUNT_REPEAT):
    return _measure_memory_wrap(source_len, target_len, non_recursive_levenshtein, n)


def measure_memory_dl(source_len, target_len, n=COUNT_REPEAT):
    return _measure_memory_wrap(source_len, target_len, non_recursive_damerau_levenshtein, n)


def measure_memory_rdl(source_len, target_len, n=COUNT_REPEAT):
    return _measure_memory_wrap(source_len, target_len, recursive_damerau_levenshtein, n)


def measure_memory_rdl_with_cache(source_len, target_len, n=COUNT_REPEAT):
    return _measure_memory_wrap(source_len, target_len, recursive_damerau_levenshtein_with_cache, n)


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
    (measure_memory_l, '\nРасстояние Левенштейна'),
    (measure_memory_dl, '\nРасстояние Дамерау-Левенштейна'),
    (measure_memory_rdl, '\nРекурсивное расстояние Дамерау-Левенштейна'),
    (measure_memory_rdl_with_cache, '\nРекурсивное расстояние Дамерау-Левенштейна с кешем')
)


OUTPUT_FILE_PREFIX = 'out/memory/res_time'


def measure_memory_exp():
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