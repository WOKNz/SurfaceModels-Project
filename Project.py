import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid
#from plotVTK import plot as vtkPlot
#from grid_db import Grid


#IMporting data
dem1 = np.genfromtxt('data/dem_50.asc',skip_header=6)
dem2 = np.genfromtxt('data/dem_3_50.asc',skip_header=6)
dem3 = np.genfromtxt('data/dem_4_50.asc',skip_header=6)

params1 = pd.read_csv('data/dem_50.asc',nrows=6,delim_whitespace=True,header=None)
params1.columns = ['Key','Value']
params1 = pd.Series(params1.Value.values,index=params1.Key).to_dict()

params2 = pd.read_csv('data/dem_3_50.asc',nrows=6,delim_whitespace=True,header=None)
params2.columns = ['Key','Value']
params2 = pd.Series(params2.Value.values,index=params2.Key).to_dict()

params3 = pd.read_csv('data/dem_4_50.asc',nrows=6,delim_whitespace=True,header=None)
params3.columns = ['Key','Value']
params3 = pd.Series(params3.Value.values,index=params3.Key).to_dict()



dem3_2nd_min = np.amin(dem3[dem3 != params3['NODATA_value']])
# Creating grid of images
fig = plt.figure(figsize=(4., 4.))
grid = ImageGrid(fig, 111,  # similar to subplot(111)
                 nrows_ncols=(1, 3),  # creates 2x2 grid of axes
                 axes_pad=0.1,  # pad between axes in inch.
                 )
for ax, im in zip(grid, [[dem1,params1], [dem2,params2], [dem3,params3]]):
    # Iterating over the grid returns the Axes.
    if im[0] is dem3:
        ax.imshow(im[0] ,cmap='gray',vmin=dem3_2nd_min)
    else:
	    ax.imshow(im[0] ,cmap='gray')
plt.show()


print('pause')