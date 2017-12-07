#-*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt
import csv

# Read dataset and turn it into a numpy array
def read_datafile(file_name):
    data = np.loadtxt(file_name, delimiter=";")
    return data

data = read_datafile("testcsv1.csv")
x = data[:,0]
y = data[:,1]

# Plot statements
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_title("Title")
ax1.set_xlabel("x label")
ax1.set_ylabel("y label")
ax1.plot(x,y, c="r", label="red curve")
leg = ax1.legend()
ax1.grid()
plt.show()
