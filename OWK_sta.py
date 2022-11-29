import numpy as np
import matplotlib
import os
from Bar_functions import *
from Totals import *
from Data_entry import *

ronde_1 = get_data("data/ronde_1/")
ronde_2 = get_data("data/ronde_2/")


occurrence_bar(get_occurrence_count(ronde_1, 0), "ronde_1/bar_A")
occurrence_bar(get_occurrence_count(ronde_1, 1), "ronde_1/bar_B")
occurrence_bar(get_occurrence_count(ronde_1, 2), "ronde_1/bar_C")
occurrence_bar(get_occurrence_count(ronde_1, 3), "ronde_1/bar_D")
occurrence_bar(get_occurrence_count(ronde_1, 4), "ronde_1/bar_E")
occurrence_bar(get_occurrence_count(ronde_1, 5), "ronde_1/bar_F")
plot_averages(ronde_1, "ronde_1/")

occurrence_bar(get_occurrence_count(ronde_2, 0), "ronde_2/bar_A")
occurrence_bar(get_occurrence_count(ronde_2, 1), "ronde_2/bar_B")
occurrence_bar(get_occurrence_count(ronde_2, 2), "ronde_2/bar_C")
occurrence_bar(get_occurrence_count(ronde_2, 3), "ronde_2/bar_D")
occurrence_bar(get_occurrence_count(ronde_2, 4), "ronde_2/bar_E")
occurrence_bar(get_occurrence_count(ronde_2, 5), "ronde_2/bar_F")
plot_averages(ronde_2, "ronde_2/")



