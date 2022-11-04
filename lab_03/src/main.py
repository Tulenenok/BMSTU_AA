from algorithms import (
    binary_tree_sort,
    gnome_sort,
    smooth_sort
)
from tools import bcolors
from unit_tests import unit_tests
from time_memory import measure_mem_exp, measure_time_exp_2


def main():
    show_menu = True
    while show_menu:
        command = input(f"{bcolors.HEADER}МЕНЮ{bcolors.ENDC} \n"
                        "  0. Выход\n"
                        "  1. Ручное тестирование\n"
                        "  2. Автоматическое тестирование \n"
                        "  3. Замер памяти\n"
                        "  4. Замер времени\n"
                        f"{bcolors.HEADER}Введите номер команды:{bcolors.ENDC} ")

        if command == '0':
            show_menu = False

        elif command == '1':
            source = input("\nВведите массив (одной строкой): ")
            try:
                lst = list(map(float, source.split()))
            except:
                print('Неверно введен массив :((')
                continue

            gnome_res = gnome_sort(lst)
            smooth_res = smooth_sort(lst)
            bin_res = binary_tree_sort(lst)

            print(f'{bcolors.WARNING}Ответ{bcolors.ENDC} (гномья сортировка): ', gnome_res)
            print(f'{bcolors.WARNING}Ответ{bcolors.ENDC} (плавная сортировка): ', smooth_res)
            print(f'{bcolors.WARNING}Ответ{bcolors.ENDC} (сортировка бинарным деревом): ', bin_res)

            if gnome_res == smooth_res == bin_res:
                print(f'{bcolors.OKGREEN}SUCCESS (результаты сошлись){bcolors.ENDC}')
            else:
                print(f'{bcolors.FAIL}FAILED (результаты НЕ сошлись){bcolors.ENDC}')

            print()

        elif command == '2':
            unit_tests()

        elif command == '3':
            measure_mem_exp()

        elif command == '4':
            measure_time_exp_2()

        else:
            print('Неверный номер команды :(')


if __name__ == "__main__":
    main()