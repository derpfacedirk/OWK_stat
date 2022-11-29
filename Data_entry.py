import numpy as np
import matplotlib
import os


def get_data(path):
    data_points = 0
    for i in os.listdir(path):
        data_points += 1

    data = np.zeros(shape=(6, 6, data_points))

    j = 0
    # format: data[colour][question][data_point]
    for file_name in os.listdir(path):
        file = open(path + file_name, 'r')
        for j, line in enumerate(file):
            inputs = line.split(',')
            for k in range(6):
                if j == 0:
                    data[j][k][0] = int(inputs[k])
                else:
                    data[j][k][j] = int(inputs[k])
        j += 1

    return data
