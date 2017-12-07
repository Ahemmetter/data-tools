#-*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import interp1d
import csv

# Read data files and turn them into numpy array for further processing
def read_datafile(file_name):
    data = np.loadtxt(file_name, delimiter=";")
    return data

data1 = read_datafile("testcsv1.csv")
data2 = read_datafile("testcsv2.csv")

# Add empty column at the appropriate position
emptycol1 = np.empty((len(data1), 3))
emptycol1[:] = np.nan
emptycol2 = np.empty((len(data2), 3))
emptycol2[:] = np.nan
emptycol1[:,:-1] = data1
emptycol2[:,[0, 2]] = data2

# Merge and sort the data sets. Create empty array to add final results
merged_temp = np.concatenate((emptycol1, emptycol2))
merged_temp = np.array(sorted(merged_temp, key = lambda x: float(x[0])))
merged = np.empty((1, 3))

# Check for entries where the x values already match. Merge those into one row
i = 0
while i < len(merged_temp)-1:
    if merged_temp[i, 0] == merged_temp[i+1, 0]:
        newrow = np.array([merged_temp[i, 0], merged_temp[i, 1], merged_temp[i+1, 2]])
        merged = np.vstack((merged, newrow))
        i += 2
    else:
        newrow = np.array([merged_temp[i, 0], merged_temp[i, 1], merged_temp[i, 2]])
        merged = np.vstack((merged, newrow))
        i += 1

# Check for so far undefined values (gaps in the data). Interpolate between them (linearly)
for i in range(len(merged)-1):
    # First y column
    if np.isnan(merged[i, 1]) == True:
        # If only one value is missing (maybe not necessary to separate this case)
        if (np.isnan(merged[i-1, 1]) == False) and (np.isnan(merged[i+1, 1]) == False):
            merged[i, 1] = (merged[i-1, 1] + merged[i+1, 1])/2
        # If two or more values are missing
        elif np.isnan(merged[i, 1]) == True:
            l = 0
            while (np.isnan(merged[i+l, 1]) == True) and (i+l != len(merged)-1):
                l += 1
            x1 = np.array([i-1, i+l])                       # endpoints
            x = np.linspace(i, i+l-1, l, endpoint=True)     # missing points
            y = np.array([merged[i-1, 1], merged[i+l, 1]])  # values at endpoints
            f = interp1d(x1, y)                             # linear interpolation
            for k in x:
                merged[k, 1] = f(k)
    # Second y column
    if np.isnan(merged[i, 2]) == True:
        # If only one value is missing
        if (np.isnan(merged[i-1, 2]) == False) and (np.isnan(merged[i+1, 2]) == False):
            merged[i, 2] = (merged[i-1, 2] + merged[i+1, 2])/2
        # If two or more values are missing
        elif np.isnan(merged[i, 2]) == True:
            l = 0
            while (np.isnan(merged[i+l, 2]) == True) and (i+l != len(merged)-1):
                l += 1
            x1 = np.array([i-1, i+l])                       # endpoints
            x = np.linspace(i, i+l-1, l, endpoint=True)     # missing points
            y = np.array([merged[i-1, 2], merged[i+l, 2]])  # values at endpoints
            f = interp1d(x1, y)                             # linear interpolation
            for k in x:
                merged[k, 2] = f(k)

# Remove lines which still have "nan" values (beginning and end). This could be prevented by an extrapolation
merged = merged[~np.isnan(merged).any(axis=1)]
merged = np.delete(merged, (0), axis=0)

# Write table to new csv file in the same directory
with open("testcsv_merged.csv", "w") as mergedfile:
    writer = csv.writer(mergedfile)
    [writer.writerow(r) for r in merged]
