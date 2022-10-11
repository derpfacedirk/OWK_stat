import numpy as np
import matplotlib
import os

data = np.zeros(shape=(6,6,1))

j = 0
for file_name in os.listdir('data/'):
	file = open('data/' + file_name, 'r')
	for l, line in enumerate(file):
		inputs = line.split(',')
		for k in range (6):
			if j == 0:
				data[l][k][0] = inputs[k]
			else:
				pass
				# np.append(data[l][k], inputs)
				# data[l][k].append(inputs[k])
	j += 1

print(data)
input("Press Enter to close...")
