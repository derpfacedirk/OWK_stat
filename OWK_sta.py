import numpy as np
import matplotlib
import os
from Bar_functions import *
from Totals import *

data_points = 0
for path in os.listdir('data/'):
	data_points+=1

data = np.zeros(shape=(6,6,data_points))

j = 0
# format: data[colour][question][data_point]
for file_name in os.listdir('data/'):
	file = open('data/' + file_name, 'r')
	for l, line in enumerate(file):
		inputs = line.split(',')
		for k in range (6):
			if j == 0:
				data[l][k][0] = int(inputs[k])
			else:
				data[l][k][j] = int(inputs[k])
	j += 1

occurrence_bar(get_occurrence_count(data, 0), "bar_A")
occurrence_bar(get_occurrence_count(data, 1), "bar_B")
occurrence_bar(get_occurrence_count(data, 2), "bar_C")
occurrence_bar(get_occurrence_count(data, 3), "bar_D")
occurrence_bar(get_occurrence_count(data, 4), "bar_E")
occurrence_bar(get_occurrence_count(data, 5), "bar_F")
plot_averages(data, data_points)
#input("Press Enter to close...")
