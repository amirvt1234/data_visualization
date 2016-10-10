import numpy as np
#from scipy.interpolate import griddata



filename     = "maxvalues_control"
N            = 4801
N1           = 2641 
N2           = N*N1

x=[]; y=[]; hmax=[]; mommax=[]; 
i = 0
with open(filename, 'r') as source_file:
    for line in source_file:
       l1=line.strip()
       if not l1.startswith("#"):
         l2 = line.rstrip()
         if (l2): 
	   col1, col2, col3, col4 = line.split()
           x.append(col1); y.append(col2); hmax.append(col3); mommax.append(col4)

x = np.array(x); y = np.array(y); mommax = np.array(mommax); hmax = np.array(hmax);
x = x.astype(float); y = y.astype(float); mommax = mommax.astype(float); hmax = hmax.astype(float); 
x1 = x[0:N2].reshape(N,N1); y1 = y[0:N2].reshape(N,N1); hmax1 = hmax[0:N2].reshape(N,N1); mommax1 = mommax[0:N2].reshape(N,N1); 
x=[]; y=[]; hmax=[]; mommax=[]; 
