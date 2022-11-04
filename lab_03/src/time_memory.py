import random
from prettytable import PrettyTable
import tracemalloc
from time import time

from algorithms import (
    gnome_sort,
    smooth_sort,
    binary_tree_sort
)
from tools import bcolors


N = 500
MICRO = 1000000

FIELD_NAMES = [f'{bcolors.OKCYAN}N{bcolors.ENDC}',
               f'{bcolors.OKCYAN}Не отсортированный{bcolors.ENDC}',
               f'{bcolors.OKCYAN}Отсортированный{bcolors.ENDC}',
               f'{bcolors.OKCYAN}Упорядоченный по убыванию{bcolors.ENDC}']


def _measure_memory(test_func, *params):
    tracemalloc.start()
    curr, peak = tracemalloc.get_traced_memory()
    test_func(*params)
    curr, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return peak


TEST_FUNCS = (
    ("Гномья сортировка", gnome_sort),
    ("Плавная сортировка", smooth_sort),
    ("Сортировка бинарным деревом", binary_tree_sort)
)


def measure_mem_exp():
    for title, fun in TEST_FUNCS:
        print('\n', bcolors.BOLD + title + bcolors.ENDC)

        _measure_memory(fun, [])

        tbl = PrettyTable()
        tbl.field_names = FIELD_NAMES
        tbl.align = 'l'

        for i in (0, 1, 5, 10, 50, 100, 250, 500):
            row = [i]

            lst = list(range(i))
            row.append(_measure_memory(fun, lst))

            lst.sort()
            row.append(_measure_memory(fun, lst))

            lst.reverse()
            row.append(_measure_memory(fun, lst))

            tbl.add_row(row)

        print(tbl)


def _measure_time(test_func, *params):
    t1 = time()
    for _ in range(N):
        test_func(*params)
    t2 = time()
    return round((t2 - t1) / N * MICRO)


def measure_time_exp():
    for title, fun in TEST_FUNCS:
        print('\n', bcolors.BOLD + title + bcolors.ENDC)

        tbl = PrettyTable()
        tbl.field_names = FIELD_NAMES
        tbl.align = 'l'

        for i in (0, 1, 5, 10, 50, 100, 250):
            row = [i]

            lst = list(range(i))
            row.append(_measure_time(fun, lst))

            lst.sort()
            row.append(_measure_time(fun, lst))

            lst.reverse()
            row.append(_measure_time(fun, lst))

            tbl.add_row(row)

        print(tbl)


FIELD_NAMES_2 = [f'{bcolors.OKCYAN}N{bcolors.ENDC}',
                 f'{bcolors.OKCYAN}Гномья сортировка{bcolors.ENDC}',
                 f'{bcolors.OKCYAN}Плавная сортировка{bcolors.ENDC}',
                 f'{bcolors.OKCYAN}Сортировка бинарным деревом{bcolors.ENDC}']


def measure_time_exp_2():
    TITLES = ["не отсортирован", "отсортирован", "отсортирован в обратном порядке"]

    for j, title in enumerate(TITLES):
        print('\n', bcolors.BOLD + "Массив " + title + bcolors.ENDC)

        tbl = PrettyTable()
        tbl.field_names = FIELD_NAMES_2
        tbl.align = 'l'

        for i in (0, 1, 5, 10, 50, 100, 250):
            row = [i]

            lst = list(range(i))
            if j == 1:
                lst.sort()
            if j == 2:
                lst.reverse()

            row.append(_measure_time(gnome_sort, lst))
            row.append(_measure_time(smooth_sort, lst))
            row.append(_measure_time(binary_tree_sort, lst))

            tbl.add_row(row)

        print(tbl)
