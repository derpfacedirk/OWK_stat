import numpy
import matplotlib
import os

data = np.array()
    
j = 0
for file_name in os.listdir('data/'):
    file = open(file_name, 'r')
    for l, line in enumerate(file):
        inputs = line.split(',')
        for k in range (6):
            data[l][k][j] = inputs[k]
    j += 1

print(data)
input()