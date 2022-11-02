from algorithms import (
    binary_tree_sort,
    gnome_sort,
    smooth_sort
)
from tools import bcolors


def _test_wrap(func, check_func, *params):
    """
        Обертка для тестирования функций

        func - функция, которую мы хотим проверить на корректность работы
        сheck_func - функция, с которой будем сравнивать результат
        params - список аргументов, который нужно передать функциям
    """

    expected = check_func(*params)
    received = func(*params)

    return int(expected == received), expected, received


TESTS = (
    [],
    [1],
    [0, 1],
    [1, 0],
    [2, -2],
    [2, -2, 2],
    [0, 0, 1, 2],
    [1, 2, 8, 1, -1, -10],
    [-1.1, -0, 16, 1, 1, 1, 4, 2],
    [5, 2, 1, 8, 9, 10],
    [-9.1, -8.9, 0, 3.3, 10, 13, 124],
    [1, 2, 3, 4, 5, 6, 7],
    [9, 2, 1],
    [9, -10000, -20000],
    [-1, 2, 7, 1, 12, 100, -100, 4, 5]
)

SECTIONS = (
    (gnome_sort, sorted, '\nГномья сортировка'),
    (smooth_sort, sorted, '\nПлавная сортировка'),
    (binary_tree_sort, sorted, '\nСортировка бинарным деревом'),
)


def unit_tests():
    for s in SECTIONS:
        fun, check_fun, title = s

        print(bcolors.BOLD + title + bcolors.ENDC)

        count_errors = 0
        for i, test in enumerate(TESTS):
            rc, exp, rec = _test_wrap(fun, check_fun, test)

            if rc != 0:
                print('TEST %2d ---> %sPASSED%s' % (i + 1, bcolors.OKGREEN, bcolors.ENDC))
                # print('TEST %2d ---> %sPASSED %s' % (i + 1, bcolors.OKGREEN, bcolors.ENDC))
            else:
                print('TEST %2d ---> %sFAILED%s' % (i + 1, bcolors.FAIL, bcolors.ENDC))
                #print(exp, rec)
                count_errors += 1

        print(f'{bcolors.WARNING}SUMMARY{bcolors.ENDC}: count tests {len(TESTS)}, count failed {count_errors}')
    print()