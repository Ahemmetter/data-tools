#-*- coding: utf-8 -*-

from scipy import optimize
import numpy as np
from matplotlib import pyplot as plt
import csv

# Read dataset and load it into numpy arrays, separated into x and y
def read_datafile(file_name):
    data = np.loadtxt(file_name, delimiter=";")
    return data

data = read_datafile("testcsv1.csv")
datax = data[:,0]
datay = data[:,1]


# Fit the data set

fitfunc = lambda p, x: (p[0]**2 / (x**2 + p[1])) +  (p[4]*np.exp(-((x-p[2])/p[3])**2))      # Fit function
errfunc = lambda p, x, y: fitfunc(p, x) - y                                                 # Error function
p0 = [1000., 100., 2600., 10., 10.]                                   # Initial guesses
p1, success = optimize.leastsq(errfunc, p0[:], args=(datax, datay))
xsteps = np.linspace(datax.min(), datax.max(), 100)                                         # Steps in x

# Plot data and fit function
plt.plot(datax, datay, "rx", xsteps, fitfunc(p1, xsteps), "b-")
plt.show()
