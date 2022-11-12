from algorithms import (
    simple_matrix_mult,
    winograd_matrix_mult,
    winograd_matrix_mult_opim
)
from tools import bcolors, check_matrix_dol


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
    [ [[1, 1, 1]], [[1], [1], [1]] ],
    [ [[1]], [[3]] ],
    [ [[1, 0, 0], [0, 1, 0], [0, 0, 1]], [[1], [1], [1]] ],
    [ [[1, 2], [2, 1]], [[1, 0], [1, 0]] ],
    [ [[1, 2, 3], [4, 5, 6], [1, 2, 3]], [[1, 2, 3], [4, 5, 6], [1, 2, 3]] ],
    [ [[1, 2, 3]], [[1], [2], [3]] ],
    [ [[1, 3]], [[1], [3]] ]
)

SECTIONS = (
    (simple_matrix_mult, check_matrix_dol, '\nСтандартный алгоритм'),
    (winograd_matrix_mult, check_matrix_dol, '\nАлгоритм Винограда'),
    (winograd_matrix_mult_opim, check_matrix_dol, '\nОптимизированный алгоритм Винограда'),
)


def unit_tests():
    for s in SECTIONS:
        fun, check_fun, title = s

        print(bcolors.BOLD + title + bcolors.ENDC)

        count_errors = 0
        for i, test in enumerate(TESTS):
            rc, exp, rec = _test_wrap(fun, check_fun, *test)

            if rc != 0:
                print('TEST %2d ---> %sPASSED%s' % (i + 1, bcolors.OKGREEN, bcolors.ENDC))
                # print('TEST %2d ---> %sPASSED %s' % (i + 1, bcolors.OKGREEN, bcolors.ENDC))
            else:
                print('TEST %2d ---> %sFAILED%s' % (i + 1, bcolors.FAIL, bcolors.ENDC))
                # print(exp, rec)
                count_errors += 1

        print(f'{bcolors.WARNING}SUMMARY{bcolors.ENDC}: count tests {len(TESTS)}, count failed {count_errors}')
    print()
