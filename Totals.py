import numpy as np
import matplotlib.pyplot as plt


"""
Calculates the average score per colour per question.

data: The data NumPy array, formatted like data[colour][question][data_point]
data_points: The total number of data points

returns a 2D NumPy array with the average of each colour per question.
"""
def get_averages(data, data_points):
	totals = np.zeros(shape=(6,6))
	to_return = np.zeros(shape=(6,6))

	for i in range(6):
		for j in range(6):
			amount_used = data_points
			for k in data[i][j]:
				if(k == 0):
					amount_used -= 1
				totals[i][j] += k
			to_return[i][j] = totals[i][j] / amount_used
	return to_return


def plot_averages(data, data_points):
	averages = get_averages(data, data_points)

	fig = plt.figure()
	ax = fig.add_subplot(111)
	x = [1, 2, 3, 4, 5, 6]
	ax.set_xticks(np.arange(6)+1,('A', 'B', 'C', 'D', 'E', 'F'))
	y_red = averages[0]
	y_orange = averages[1]
	y_yellow = averages[2]
	y_green = averages[3]
	y_blue = averages[4]
	y_purple = averages[5]

	ax.set_xlabel("Ronde")
	ax.set_ylabel("Gemiddelde score")

	ax.scatter(x, y_red, c="red")
	ax.scatter(x, y_orange, c="orange")
	ax.scatter(x, y_yellow, c="yellow")
	ax.scatter(x, y_green, c="green")
	ax.scatter(x, y_blue, c="blue")
	ax.scatter(x, y_purple, c="purple")
	ax.grid(axis='y')

	plt.savefig('charts/averages.png')
