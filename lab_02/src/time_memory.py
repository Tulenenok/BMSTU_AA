import random
from prettytable import PrettyTable
import tracemalloc
from time import process_time
import matplotlib.pyplot as plt

from algorithms import (
    simple_matrix_mult,
    winograd_matrix_mult,
    winograd_matrix_mult_opim
)
from tools import bcolors, generate_matrix


N = 1
MICRO = 1000000

FIELD_NAMES = [f'{bcolors.OKCYAN}N{bcolors.ENDC}',
               f'{bcolors.OKCYAN}Стандартный алгоритм{bcolors.ENDC}',
               f'{bcolors.OKCYAN}Алгоритм Винограда{bcolors.ENDC}',
               f'{bcolors.OKCYAN}Оптимизированный алгоритм Винограда{bcolors.ENDC}']


TEST_FUNCS = (
    ("Стандартный алгоритм", simple_matrix_mult),
    ("Алгоритм Винограда", winograd_matrix_mult),
    ("Оптимизированный алгоритм Винограда", winograd_matrix_mult_opim)
)

GRAPH_NUM = 1
NAMES = ['четные', 'нечетные']

def _measure_time(test_func, *params):
    t1 = process_time()
    for _ in range(N):
        test_func(*params)
    t2 = process_time()
    return round((t2 - t1) / N * MICRO)


def measure_time_exp(values=(50, 100, 150, 200, 300, 400, 500)):
    global GRAPH_NUM

    print('\n', bcolors.BOLD + 'Замер времени' + bcolors.ENDC)

    tbl = PrettyTable()
    tbl.field_names = FIELD_NAMES
    tbl.align = 'l'

    y_values = [[] for _ in TEST_FUNCS]
    plt.figure(dpi=1200)

    for i in values:
        row = [i]

        m1 = generate_matrix(i, i)
        m2 = generate_matrix(i, i)

        for i, fun in enumerate(TEST_FUNCS):
            res = _measure_time(fun[1], m1, m2)

            row.append(res)
            y_values[i].append(res * 0.001)

        tbl.add_row(row)

    for y, c, name in zip(y_values, ('r', 'm', 'b'), TEST_FUNCS):
        plt.plot(values, y, c, label=name[0])

    plt.title(f'Временные характеристики ({NAMES[GRAPH_NUM - 1]} размеры матриц)')
    plt.ylabel('Затраченное время (микросекунды)')
    plt.xlabel('Размер квадратной матрицы')

    plt.legend()
    plt.grid(True)

    plt.savefig(f'/Users/gurovana/Documents/aa/Tulenenok/lab_02/out/graph{GRAPH_NUM}.jpeg')
    GRAPH_NUM += 1
    plt.clf()

    print(tbl)



