import numpy as np
import matplotlib.pyplot as plt


def A_bar(data):
    data_a = data[1]
    bar_data_colour = np.zeros(shape=(6, 6))
    # red = 0; orange = 1; yellow = 2; green = 3; blue = 4; purple = 5

    # i represents colour
    # j represents data number
    for i in range(6):
        # print(data_a[i])
        for j in data_a[i]:
            # print(j)
            # print(type(j))
            bar_data_colour[i][int(j - 1)] += 1

    temp_array = [0, 0, 0, 0, 0, 0]
    for i in range(6):
        temp_array[i] = max(bar_data_colour[i])
    max_value = max(temp_array)

    X = np.arange(6)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xticks(X, ('1', '2', '3', '4', '5', '6'))
    ax.set_yticks(np.arange(max_value + 1))
    ax.bar(X - 0.25, bar_data_colour[0], color='red', width=0.10)
    ax.bar(X - 0.15, bar_data_colour[1], color='orange', width=0.10)
    ax.bar(X - 0.05, bar_data_colour[2], color='yellow', width=0.10)
    ax.bar(X + 0.05, bar_data_colour[3], color='green', width=0.10)
    ax.bar(X + 0.15, bar_data_colour[4], color='blue', width=0.10)
    ax.bar(X + 0.25, bar_data_colour[5], color='purple', width=0.10)

    plt.savefig('charts/Bar_a.png')
