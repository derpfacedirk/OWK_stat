import numpy as np
import matplotlib.pyplot as plt


def get_totals(data):
    to_return = np.zeros(shape=(6, 6))

    for i in range(6):
        for j in range(6):
            for k in data[i][j]:
                to_return[i][j] += k
    return to_return


def get_averages(data, data_points):
    totals = get_totals(data)
    to_return = np.zeros(shape=(6, 6))

    for i in range(6):
        for j in range(6):
            to_return[i][j] = totals[i][j] / data_points
    return to_return


def plot_averages(data, path):
    data_points = len(data[0][0])
    averages = get_averages(data, data_points)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    x = [1, 2, 3, 4, 5, 6]
    ax.set_xticks(np.arange(6) + 1, ('A', 'B', 'C', 'D', 'E', 'F'))
    y_red = averages[0]
    y_orange = averages[1]
    y_yellow = averages[2]
    y_green = averages[3]
    y_blue = averages[4]
    y_purple = averages[5]

    ax.scatter(x, y_red, c="red")
    ax.scatter(x, y_orange, c="orange")
    ax.scatter(x, y_yellow, c="yellow")
    ax.scatter(x, y_green, c="green")
    ax.scatter(x, y_blue, c="blue")
    ax.scatter(x, y_purple, c="purple")

    plt.savefig('charts/' + path)
