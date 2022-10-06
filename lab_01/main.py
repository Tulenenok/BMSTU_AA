import algorithms
from tools import bcolors
from unit_tests import unit_tests
from time_memory import measure_time_exp


def main():
    show_menu = True
    while show_menu:
        command = input(f"{bcolors.HEADER}МЕНЮ{bcolors.ENDC} \n"
                        "  0. Выход\n"
                        "  1. Расстояние Левенштейна \n"
                        "  2. Расстояние Дамерау-Левенштейна \n"
                        "  3. Расстояние Дамерау-Левенштейна рекурсивно \n"
                        "  4. Расстояние Дамерау-Левенштейна рекурсивно c кешем\n"
                        "  5. Все алгоритмы вместе\n"
                        "  6. Автоматическое тестирование \n"
                        "  7. Замер памяти и времени\n"
                        f"{bcolors.HEADER}Введите номер команды:{bcolors.ENDC} ")

        if command == '0':
            show_menu = False

        elif command in ['1', '2', '3', '4', '5']:
            source = input("\nВведите строку-источник: ")
            target = input("Введите целевую строку: ")

            if command == '1' or command == '5':
                print(f'{bcolors.WARNING}Ответ{bcolors.ENDC} (расстояние Левенштейна): ',
                      algorithms.non_recursive_levenshtein(source, target))

            if command == '2' or command == '5':
                print(f'{bcolors.WARNING}Ответ{bcolors.ENDC} (расстояние Дамерау-Левенштейна): ',
                      algorithms.non_recursive_damerau_levenshtein(source, target))

            if command == '3' or command == '5':
                print(f'{bcolors.WARNING}Ответ{bcolors.ENDC} (расстояние Дамерау-Левенштейна рекурсивно): ',
                      algorithms.recursive_damerau_levenshtein(source, target))

            if command == '4' or command == '5':
                print(f'{bcolors.WARNING}Ответ{bcolors.ENDC} (расстояние Дамерау-Левенштейна рекурсивно с кешем): ',
                      algorithms.recursive_damerau_levenshtein_with_cache(source, target))

            print()

        elif command == '6':
            unit_tests()

        elif command == '7':
            measure_time_exp()

        else:
            print('Неверный номер команды :(')


if __name__ == "__main__":
    main()