from tools import (
    bcolors,
    input_matrix,
    print_list_matrix,
    cmp_matrix
)
from algorithms import (
    simple_matrix_mult,
    winograd_matrix_mult,
    winograd_matrix_mult_opim
)
from unit_tests import unit_tests
from time_memory import measure_time_exp


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
            r1, c1, m1 = input_matrix("\nMАТРИЦА 1")
            r2, c2, m2 = input_matrix("\nMАТРИЦА 2")

            if r1 < 0 or r2 < 0 or c1 < 0 or c2 < 0:
                continue

            if len(m1[0]) != len(m2):
                print("Неверные размеры матриц\n")
                continue

            print(f"\nВВОД --> {bcolors.OKGREEN}SUCCESS{bcolors.ENDC}")
            print_list_matrix([m1, m2])

            simple_r = simple_matrix_mult(m1, m2)
            winograd_r = winograd_matrix_mult(m1, m2)
            opt_w_r = winograd_matrix_mult_opim(m1, m2)

            print("\nРезультаты перемножения матриц \nразными способами можно увидеть в таблице")
            print_list_matrix([simple_r, winograd_r, opt_w_r], ['Simple', 'Winograd', 'Оptimization'])

            if cmp_matrix([simple_r, winograd_r, opt_w_r]):
                print(f'ВЫВОД --> {bcolors.OKGREEN}SUCCESS{bcolors.ENDC}(результаты сошлись)')
            else:
                print(f'ВЫВОД --> {bcolors.FAIL}FAILED{bcolors.ENDC}(результаты НЕ сошлись)')

            print()

        elif command == '2':
            unit_tests()

        elif command == '3':
            measure_mem_exp()

        elif command == '4':
            measure_time_exp((10, 20, 50, 100, 200, 300, 500))
            measure_time_exp((11, 21, 51, 101, 201, 301, 501))

        else:
            print('Неверный номер команды :(')


if __name__ == "__main__":
    main()
