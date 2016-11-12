# By Wei Liu, Yao Zhao and Huamin Li
# Nov 2016
# Plot all normalized spectra
import os
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D

#normalization of the spectra
def normal(y):
     suma = 0
     for current in y:
        suma=suma+current
     for i,item in enumerate(y):
        y[i]=item/suma
     return y


#load data directory
data_dir = '../data/fruitsms'


filenames = os.listdir(data_dir)
colors = np.zeros((len(filenames)))
headers = []
header = ''
colortmp = -1
for i, filename in zip(range(len(filenames)), filenames):
    new_header = filename.split('_')[0]
    if header != new_header:
        colortmp += 1
        header = new_header
        headers.append(header)
    colors[i] = colortmp

colormaps=plt.cm.rainbow(np.linspace(0,1,colortmp+1))
mat=np.empty((0, 1024))
nameholder = ''
for color, filename in zip(colors, filenames):
    x,y = np.loadtxt(os.path.join(data_dir, filename), unpack=True)
    y = normal(y)    
    itemname = filename.split('_')[0]
    if nameholder != itemname:     
         plt.plot(x,y,c=colormaps[color], label = filename.split('_')[0])
         nameholder = itemname
    else:
         plt.plot(x,y,c=colormaps[color])

legend = plt.legend(loc='upper right', fontsize='large', shadow=True)
plt.xlabel('wavelength(nm)', fontsize=18)
#plt.ylabel('raw intensity(a.u.)', fontsize=18)
plt.ylabel('normalized intensity(a.u.)', fontsize=18)
plt.show()


