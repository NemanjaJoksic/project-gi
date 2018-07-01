from tkinter import *
import matplotlib.pyplot as plt
import numpy as np


def preview_results(data, patterns, label, measurement_unit, genome_name):
    columns = (patterns[0], patterns[1], patterns[2])
    rows = ['sorted index', 'hash table', 'suffix array', 'suffix tree']

    colors = ['red', 'blue', 'green', 'brown']
    n_rows = len(data)

    ind = np.arange(3)
    width = 0.2

    fig, ax = plt.subplots()
    data_copy = [row[:] for row in data]
    replace_nan(data_copy)
    for row in range(n_rows):
        ax.bar(ind + width * row, data_copy[row], width, color=colors[row])

    add_measurement_unit(data, measurement_unit)
    the_table = plt.table(cellText=data,
                          cellLoc='center',
                          rowLabels=rows,
                          rowColours=colors,
                          colLabels=columns,
                          loc='bottom')

    # Adjust layout to make room for the table:
    plt.subplots_adjust(left=0.2, bottom=0.2)

    plt.ylabel(label)
    plt.xticks([])
    plt.title(genome_name)

def replace_nan(data):
    for row in range(len(data)):
        for i in range(0, len(data[row])):
            if(data[row][i] == 'x' or data[row][i] == 'X'):
                data[row][i] = 0

def add_measurement_unit(data, unit):
    for row in range(len(data)):
        for i in range(0, len(data[row])):
            if(data[row][i] != 'x' and data[row][i] != 'X'):
                data[row][i] = str(data[row][i]) + unit


def show_preprocessing_test_results():
    preview_results(data_preprocessing_duration, genomes, 'time (s)', 's', 'preprocessing')
    preview_results(data_preprocessing_mem_usage, genomes, 'memory (GB)', 'GB', 'preprocessing')
    plt.show()


def show_testing_genome_1_results():
    preview_results(data_test1_duration, patterns, 'time (ms)', 'ms', genomes[0])
    #preview_results(data_test1_mem_usage, patterns, 'memory (GB)', genomes[0])
    plt.show()


def show_testing_genome_2_results():
    preview_results(data_test2_duration, patterns, 'time (ms)', 'ms', genomes[1])
    #preview_results(data_test2_mem_usage, patterns, 'memory (GB)', genomes[1])
    plt.show()


def show_testing_genome_3_results():
    preview_results(data_test3_duration, patterns, 'time (ms)', 'ms', genomes[2])
    #preview_results(data_test3_mem_usage, patterns, 'memory (GB)', genomes[2])
    plt.show()

data_preprocessing_duration = [[36, 173, 839], [12, 62, 320], [113, 7515, 'X'], [816, 5655, 'X']]
data_preprocessing_mem_usage = [[3.81, 18.71, 84.61], [1.01, 4.90, 21.79], [2.09, 4.26, 'X'], [25.05, 121.68, 'X']]

data_test1_duration = [[67.62, 54.37, 34.52], [42.79, 38.46, 21.39], [2.32, 1.45, 0.11], [31.83, 12.75, 4.79]]
data_test2_duration = [[406.38, 428.28, 304.14], [160.24, 186.62, 118.05], [10.34, 2.69, 0.41], [223.84, 61.83, 1.11]]
data_test3_duration = [[2807.77, 1478.21, 1094.37], [1657.09, 935.52, 711.59], ['X', 'X', 'X'], ['X', 'X', 'X']]

patterns = ['ATGAT', 'CTCTCTA', 'TCACTACTCTCA']
genomes = ['Ananas comosus cultivar', 'Canis lupus familiaris', 'Phoenix dactylifera cultivar']

window = Tk()
window.title("Testing results")
window.geometry('400x450')

btn1 = Button(window, text="Preprocessing", command=show_preprocessing_test_results, height=4, width=50)
btn1.place(relx=0.5, rely=0.2, anchor=CENTER)

btn2 = Button(window, text="Testing genome 1", command=show_testing_genome_1_results, height=4, width=50)
btn2.place(relx=0.5, rely=0.4, anchor=CENTER)

btn3 = Button(window, text="Testing genome 2", command=show_testing_genome_2_results, height=4, width=50)
btn3.place(relx=0.5, rely=0.6, anchor=CENTER)

btn4 = Button(window, text="Testing genome 3", command=show_testing_genome_3_results, height=4, width=50)
btn4.place(relx=0.5, rely=0.8, anchor=CENTER)

window.mainloop()