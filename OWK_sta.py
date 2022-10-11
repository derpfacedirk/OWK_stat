import numpy as np
import matplotlib
import os

data_points = 0
for path in os.listdir('data/'):
	data_points+=1

data = np.zeros(shape=(6,6,data_points))

j = 0
for file_name in os.listdir('data/'):
	file = open('data/' + file_name, 'r')
	for l, line in enumerate(file):
		inputs = line.split(',')
		for k in range (6):
			if j == 0:
				data[l][k][0] = inputs[k]
			else:
				data[l][k][j] = inputs[k]
	j += 1

print(data)
input("Press Enter to close...")
