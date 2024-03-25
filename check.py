import os
import json

import numpy as np
import matplotlib.pyplot as plt


def calc_matrix(m1, m2):
    return np.dot(m1, m2)


def check_results(m1, m2, res):
    return np.array_equal(calc_matrix(m1, m2), res)


def read_json(file_name):
    with open(os.path.join(os.path.join('results', 'result_computing'), file_name), 'r') as file:
        data = json.load(file)

    return data["size"], data["time"]


def read_matrix(dirname, file_name):
    return np.loadtxt(os.path.join(dirname, file_name))

def write_to_file(size, value):
    with open('checking calculations.txt', 'a', encoding="utf-16") as file:
        file.write(f"Результат для матриц размером {size}x{size}: {value}\n")

def draw_graph(size, time):
    plt.plot(size, time)
    plt.xlabel('Array size')
    plt.ylabel('Calculation time')
    plt.title('The dependence of the calculation time on the size of the matrix')
    plt.grid(True)
    plt.savefig('graph.png')