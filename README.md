# data-tools
Simple data tools implemented in Python.


The project consists of three Python 2.7 scripts which help with the evaluation of scientific data. They were specifically created for the cleaning, plotting and fitting of complex dielectric functions of carbon nanotubes to be used in CST MW Studio 2017.

## mergedata.py

The original data contained two separate data sets with corresponding (but not matching) x columns in a comma-separated file format. The original data was modeled by "mock data" with the same structure:

testcsv1.csv:
```
x1;y1
0.5;3.4
0.8;3.8
0.9;1.2
1.3;1.1
1.9;2.3
```

testcsv2.csv:
```
x2;y2
0.3;-0.2
0.8;-0.9
0.91;0.2
1.0;0.1
1.5;1.2
1.6;6.3
```

mergecsv.py manages to merge both files into a csv-file with three columns, the first corresponding to x1 and x2, the second to y1 and the third to y2. The program sorts the x-values, merges them into one column and removes double values. It then places the y-values at their corresponding position in the second and third column. In the final step, the values in the y-columns are interpolated to account for the gaps in the data. For this purpose, a linear interpolation (averaging) is used, but a polynomial spline can also be implemented for certain tasks. To deal with edge cases, the first and last values are trimmed off, in case they have any empty cells. This is not a problem, since in the concrete data for which this script was developed, there are many data points per frequency interval, so the edge cases do not contribute significantly.


## plotcsv.py

This Python script loads a csv-file and plots the contents using matplotlib. The values are written to a list and later processed as data points.

## datafit.py

This script takes data from a csv-file, plots it and tries to fit a pre-defined function to the data points. The best fit is determined by the least-squares method. The user needs to define the expected function the data will take and starting values for the initial guesses. The fitted function is presented as an overlay on the final plot.
