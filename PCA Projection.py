import os
import matplotlib.pyplot as plt
import matplotlib.lines 
import matplotlib.cm as cm
import numpy as np
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D
import math

#function for normalization
def normal(y):
     suma = 0
     for current in y:
        suma=suma+current
     for i,item in enumerate(y):
        y[i]=item/suma
     return y
# load data from directory
data_dir = '../data/fruitsms'


filenames = os.listdir(data_dir)
colors = np.zeros((len(filenames)))
headers = []
header = ''
colortmp = -1
colorholder = []
for i, filename in zip(range(len(filenames)), filenames):
    new_header = filename.split('_')[0]
    if header != new_header:
        colortmp += 1
        header = new_header
        headers.append(header)
        colorholder.append(colortmp)
    colors[i] = colortmp

mat=np.empty((0, 1024))
for filename in filenames:
    x,y = np.loadtxt(os.path.join(data_dir, filename), unpack=True)
    y = normal(y)
    mat = np.vstack((mat, y))
    
reduced = PCA(n_components=3).fit_transform(mat)
print(len(reduced))

fig = plt.figure(1, figsize=(8, 6))
ax = Axes3D(fig, elev=-150, azim=110)

colormaps=plt.cm.rainbow(np.linspace(0,1,colortmp+1))
for color in range(len(headers)):
    r = reduced[colors==color,:]
    ax.scatter(r[:,0], r[:,1],r[:,2], c=colormaps[math.floor(color)])
    
leg=plt.legend(headers, loc='upper right', fontsize='small', shadow=True)    



plt.show()


