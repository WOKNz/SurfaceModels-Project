import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid
#from plotVTK import plot as vtkPlot
#from grid_db import Grid


#IMporting data
dem = np.genfromtxt('data/JensonDomingue.txt')

# Creating grid of images
fig = plt.figure(figsize=(4., 4.))
grid = ImageGrid(fig, 111,  # similar to subplot(111)
                 nrows_ncols=(1, 1),  # creates 2x2 grid of axes
                 axes_pad=0.1,  # pad between axes in inch.
                 )

grid[0].imshow(dem,cmap='gray')

dem_dpl = np.copy(dem) # Dipressedless DEM


# Step 1 Fill singe cell depressions
for i in range(1,dem.shape[0]-1):
	for j in range(1, dem.shape[1] - 1):
		r1 = dem_dpl[i-1,j-1:j+2].tolist()
		r2 = dem_dpl[i,j-1:j+2].tolist()
		r3 = dem_dpl[i+1,j-1:j+2].tolist()
		kernel = []
		del r2[1]
		kernel.extend(r1)
		kernel.extend(r2)
		kernel.extend(r3)
		minimal = min(kernel)
		if minimal > dem_dpl[i,j]:
			dem_dpl[i,j] = minimal

# Step 2 calculate flow direction
flow = np.zeros(dem.shape)
for i in range(1,dem.shape[0]-1):
	for j in range(1, dem.shape[1] - 1):
		r1 = dem_dpl[i-1,j-1:j+2].tolist()
		r2 = dem_dpl[i,j-1:j+2].tolist()
		r3 = dem_dpl[i+1,j-1:j+2].tolist()
		kernel = []
		del r2[1]
		kernel.extend(r1)
		kernel.extend(r2)
		kernel.extend(r3)
		kernel_np = np.array(kernel)
		cell = np.ones(kernel_np.shape)*dem_dpl[i,j]
		diff = kernel_np - cell
		print('test')



plt.show()


print('pause')