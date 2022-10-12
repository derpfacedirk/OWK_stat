import numpy as np
import matplotlib.pyplot as plt


def occurrence_bar(data, name):
    temp_array = [0, 0, 0, 0, 0, 0]
    for i in range(6):
        temp_array[i] = max(data[i])
    max_value = max(temp_array)

    X = np.arange(6)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xticks(X, ('1', '2', '3', '4', '5', '6'))
    ax.set_yticks(np.arange(max_value + 1))
    ax.bar(X - 0.25, data[0], color='red', width=0.10)
    ax.bar(X - 0.15, data[1], color='orange', width=0.10)
    ax.bar(X - 0.05, data[2], color='yellow', width=0.10)
    ax.bar(X + 0.05, data[3], color='green', width=0.10)
    ax.bar(X + 0.15, data[4], color='blue', width=0.10)
    ax.bar(X + 0.25, data[5], color='purple', width=0.10)

    plt.savefig('charts/' + name)


def get_occurrence_count(data, column):
    use_data = data[column]
    to_return = np.zeros(shape=(6, 6))
    # red = 0; orange = 1; yellow = 2; green = 3; blue = 4; purple = 5

    # i represents colour
    # j represents data number
    for i in range(6):
        # print(data_a[i])
        for j in use_data[i]:
            to_return[i][int(j - 1)] += 1

    return to_return
