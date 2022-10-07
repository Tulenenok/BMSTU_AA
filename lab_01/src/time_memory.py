from prettytable import PrettyTable
from time import time
import tracemalloc

from tools import generate_random_string, bcolors
from algorithms import *
from tools import bcolors

COUNT_REPEATS = 1000
SEC_RATIO = 1000000


def measure_time(source_len, target_len, func, n=COUNT_REPEATS):
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


def measure_memory(source_len, target_len, func, n=COUNT_REPEATS, flag=False):
    """
        Обертка для замера затрачиваемой памяти для работы функций

        source_len - длина строка-источник
        target_len - длина целевой строки
        func - функция, для которой мы хотим замерить количество затрачиваемой памяти
        n - количество повторов расчета
    """
    res_peak = 0
    # for i in range(n):

    source = generate_random_string(source_len)
    target = generate_random_string(target_len)

    tracemalloc.start()
    func(source, target)
    curr, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return peak if source_len != 0 else peak - curr


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

MEASURE_FUNCS = (non_recursive_levenshtein, non_recursive_damerau_levenshtein,
                 recursive_damerau_levenshtein, recursive_damerau_levenshtein_with_cache)


OUTPUT_FILE_PREFIX_TIME = 'out/time/res'
OUTPUT_FILE_PREFIX_MEMORY = 'out/memory/res'


def measure_time_exp():
    print(f'PROCESSING', end=' ')

    result_table_time = PrettyTable()
    result_table_memory = PrettyTable()

    columns = [f'{bcolors.OKCYAN}Algorithm \ Length{bcolors.ENDC}'] + \
              [f'{bcolors.OKCYAN}{m_len}{bcolors.ENDC}' for m_len in MEASURE_LENS]
    name_algs = ['Levenshtein', 'Damerau-Levenshtein',
                 'Recursive Damerau-Levenshtein', 'Recursive Damerau-Levenshtein with cache']

    result_table_time.add_column(columns[0], name_algs)
    result_table_memory.add_column(columns[0], name_algs)

    flag = True

    for i, m_len in enumerate(MEASURE_LENS):
        res_time_lst = []
        res_memory_lst = []

        for j, func in enumerate(MEASURE_FUNCS):
            print('.', end='')

            if j == 2 and m_len[0] >= 10 or j == 3 and m_len[0] > 10:
                res_time_lst.append('-')
                res_memory_lst.append('-')
            else:
                res_memory_lst.append(f'{measure_memory(m_len[0], m_len[1], func, flag): 5.3f}')
                res_time_lst.append(f'{measure_time(m_len[0], m_len[1], func): 3.2f}')

        result_table_time.add_column(columns[i + 1], res_time_lst)
        result_table_memory.add_column(columns[i + 1], res_memory_lst)

        with open(f'{OUTPUT_FILE_PREFIX_TIME}_{m_len[0]}_{m_len[1]}.txt', 'w') as f:
            for r in res_time_lst:
                f.write(f'{r}' + '\n')

        with open(f'{OUTPUT_FILE_PREFIX_MEMORY}_{m_len[0]}_{m_len[1]}.txt', 'w') as f:
            for r in res_memory_lst:
                f.write(f'{r}' + '\n')

    print(' SUCCESS')

    print(f'{bcolors.OKBLUE}\nTIME RESULT{bcolors.ENDC} (microseconds)')
    print(result_table_time)
    print()

    print(f'{bcolors.OKBLUE}MEMORY RESULT{bcolors.ENDC} (bytes)')
    print(result_table_memory)
    print()