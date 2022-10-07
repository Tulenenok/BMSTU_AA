from algorithms import *
from tools import bcolors

from Levenshtein import distance
from pyxdameraulevenshtein import damerau_levenshtein_distance


def _test_wrap(source, target, func, check_func):
    """
        Обертка для тестирования функций поиска расстояния

        source - строка-источник
        target - целевая строка
        func - функция, которую мы хотим проверить на корректность работы
        сheck_func - функция, с которой будем сравнивать результат
    """

    expected = check_func(source, target)
    received = func(source, target)

    return expected - received, expected, received


def test_l(source, target):
    """ Тест для расстояния Левенштейна """
    return _test_wrap(source, target, non_recursive_levenshtein, distance)


def test_dl(source, target):
    """ Тест для расстояния Дамерау-Левенштейна """
    return _test_wrap(source, target, non_recursive_damerau_levenshtein, damerau_levenshtein_distance)


def test_rdl(source, target):
    """ Тест для расстояния рекурсивного Дамерау-Левенштейна """
    return _test_wrap(source, target, recursive_damerau_levenshtein, damerau_levenshtein_distance)


def test_rdl_cache(source, target):
    """ Тест для расстояния рекурсивного Дамерау-Левенштейна с кешем """
    return _test_wrap(source, target, recursive_damerau_levenshtein_with_cache, damerau_levenshtein_distance)


TESTS = (
    ('', ''),
    ('', 'a'),
    ('b', ''),
    ('asdfv', ''),
    ('', 'sdfvs'),
    ('lll', 'lll'),
    ('qwem', 'qwem'),
    ('aa', 'cg'),
    ('kot', 'sobaka'),
    ('stroka', 'sobaka'),
    ('kot', 'kod'),
    ('cat', 'caaat'),
    ('cat', 'catty'),
    ('cat', 'tac'),
    ('recur', 'norecur')
)

SECTIONS = (
    (test_l, '\nРасстояние Левенштейна'),
    (test_dl, '\nРасстояние Дамерау-Левенштейна'),
    (test_rdl, '\nРекурсивное расстояние Дамерау-Левенштейна'),
    (test_rdl_cache, '\nРекурсивное расстояние Дамерау-Левенштейна с кешем')
)


def unit_tests():
    for s in SECTIONS:
        fun_test, title = s
        print(bcolors.BOLD + title + bcolors.ENDC)

        count_errors = 0
        for i, test in enumerate(TESTS):
            rc, exp, rec = fun_test(test[0], test[1])

            if rc == 0:
                print('TEST %2d ---> %sPASSED%s (expected = %d, received = %d)' % (i + 1, bcolors.OKGREEN, bcolors.ENDC, exp, rec))
                # print('TEST %2d ---> %sPASSED %s' % (i + 1, bcolors.OKGREEN, bcolors.ENDC))
            else:
                print('TEST %2d ---> %sFAILED%s (expected = %d, received = %d)' % (i + 1, bcolors.FAIL, bcolors.ENDC, exp, rec))
                count_errors += 1

        print(f'{bcolors.WARNING}SUMMARY{bcolors.ENDC}: count tests {len(TESTS)}, count failed {count_errors}')
    print()