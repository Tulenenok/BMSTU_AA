import random, string
from prettytable import PrettyTable
import numpy as np


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_matrix(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(m[i][j], end=' ')
        print()


def matrix_to_str(matrix):
    s = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            s += str(matrix[i][j]) + " "
        if i != len(matrix) - 1:
            s += "\n"
    return s


def input_matrix(comment):
    r, c, matrix = -1, -1, -1

    try:
        print(comment)
        r = int(input("Введите количество строк: "))
        c = int(input("Введите количество столбцов: "))
        print(f"Введите матрицу:")
        matrix = [list(map(int, input().split())) for _ in range(r)]
    except:
        print('Неверный ввод :((')

    if r != len(matrix) or c != len(matrix[0]):
        print('Неверный ввод')
        return -1, -1, -1

    return r, c, matrix


def print_list_matrix(list_matrix, field_names=None):
    p = PrettyTable()

    if field_names is None:
        field_names = [f'Matrix {i + 1}' for i in range(len(list_matrix))]

    p.field_names = field_names
    list_m_str = [matrix_to_str(m) for m in list_matrix]
    p.add_row(list_m_str)
    print(p)


def cmp_matrix(list_matrix):
    for i in range(len(list_matrix) - 1):
        if list_matrix[i] != list_matrix[i + 1]:
            return False
    return True


def check_matrix_dol(m1, m2):
    m1 = np.matrix(m1)
    m2 = np.matrix(m2)
    return m1.dot(m2).tolist()


def generate_matrix(r, c):
    return np.random.randint(-100, 100, (r, c)).tolist()