import rasterio
from rasterio import plot
import matplotlib.pyplot as plt
import numpy as np

import os
os.listdir('/home/niranjan/Pictures/ndvi/LC08_L1GT_144050_20190804_20190820_01_T2/')

#import bands as separate 1 band raster
band4 = rasterio.open('/home/niranjan/Pictures/ndvi/LC08_L1GT_144050_20190804_20190820_01_T2/LC08_L1GT_144050_20190804_20190820_01_T2_B5.TIF') #red
band5 = rasterio.open('/home/niranjan/Pictures/ndvi/LC08_L1GT_144050_20190804_20190820_01_T2/LC08_L1GT_144050_20190804_20190820_01_T2_B4.TIF') #nir

#number of raster rows
band4.height

#number of raster columns
band4.width

#plot.show(band4)

#type of raster byte
band4.dtypes[0]

#raster sytem of reference
band4.crs

#raster transform parameters
band4.transform

#raster values as matrix array
band4.read(1)

#multiple band representation
#fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
#plot.show(band4, ax=ax1, cmap='Blues') #red
#plot.show(band5, ax=ax2, cmap='Blues') #nir
#fig.tight_layout()

#generate nir and red objects as arrays in float64 format
red = band4.read(1).astype('float64')
nir = band5.read(1).astype('float64')

#nir
ndvi = (nir-red)/(nir+red)
#ndvi=np.where(
#    (nir+red)==0.,
#    0,
#    (nir-red)/(nir+red))
ndvi[:5,:5]

#export ndvi image
ndviImage = rasterio.open('/home/niranjan/Pictures/ndvi/ndviImage.tiff','w',driver='Gtiff',
                          width=band4.width,
                          height = band4.height,
                          count=1, crs=band4.crs,
                          transform=band4.transform,
                          dtype='float64')
ndviImage.write(ndvi,1)
ndviImage.close()

#plot ndvi
ndvi = rasterio.open('/home/niranjan/Pictures/ndvi/ndviImage.tiff')
fig = plt.figure(figsize=(18,12))
plot.show(ndvi)