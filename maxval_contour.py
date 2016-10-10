import matplotlib.pyplot as plt
from scipy import ndimage
from patches import *
import matplotlib as mpl
from matplotlib.collections import Collection
from matplotlib.artist import allow_rasterization


mpl.rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
mpl.rc('font', size=14)
mpl.rc('text', usetex=True)
mpl.rc('xtick', labelsize=14, color='black')
mpl.rc('ytick', labelsize=14, color='black')
mpl.rc('lines', linewidth=1.0)
mpl.rcParams['axes.linewidth'] = 1.0
mpl.rcParams['axes.edgecolor'] = 'black'
plt.rc('text', usetex=True)


class ListCollection(Collection):
     def __init__(self, collections, **kwargs):
         Collection.__init__(self, **kwargs)
         self.set_collections(collections)
     def set_collections(self, collections):
         self._collections = collections
     def get_collections(self):
         return self._collections
     @allow_rasterization
     def draw(self, renderer):
         for _c in self._collections:
             _c.draw(renderer)

def insert(c):
  collections = c.collections
  for _c in collections:
    _c.remove
  cc = ListCollection(collections,rasterized=True)
  ax = plt.gca()
  ax.add_artist(cc)
  return cc

plt.clf()
plt.close()



hmax1masked = np.ma.masked_where(hmax1 > 4, hmax1)
hmax2masked = np.ma.masked_where(hmax2 > 4, hmax2)
hmax3masked = np.ma.masked_where(hmax3 > 4, hmax3)
hmax4masked = np.ma.masked_where(hmax4 > 4, hmax4)
mommax1masked = np.ma.masked_where(mommax1 > 200, mommax1)
mommax2masked = np.ma.masked_where(mommax2 > 200, mommax2)
mommax3masked = np.ma.masked_where(mommax3 > 200, mommax3)
mommax4masked = np.ma.masked_where(mommax4 > 200, mommax4)





line = np.linspace(-2.5,2.5,50)
line2= np.linspace(-1.,1.,50)
lvls1= np.linspace(-2.5,2.5,10)
lvls2= np.linspace(-1.,1.,10)
colmap = plt.cm.seismic


fig1 = plt.figure(2, facecolor=None, figsize=(8, 7))

ax1 = plt.subplot(3,1,1)

im1 = plt.contourf(x2, y2, (hmax2masked-hmax1masked)/(hmax1masked+1e-10), levels = line,  cmap=colmap ) #+0.109508050156
for c in im1.collections:
    c.set_edgecolor("face")
insert(im1)
#for c in im1.collections:
#    c.set_rasterized(True)
#im1 = plt.contourf(x2, y2, normhmax2, levels = line,  cmap=colmap ) #+0.109508050156
patches('k',0.1885)
ax1.axis([32,41,0,2.2])
plt.gca().set_aspect('equal', adjustable='box')
ax1.set_xticklabels([''])
plt.ylabel(r'$y$', rotation=0)
plt.text(32.3,1.8,r'(a)')
ax2 = plt.subplot(3,1,2)

im1 = plt.contourf(x3, y3, (hmax3masked-hmax1masked)/(hmax1masked+1e-10), levels = line,  cmap=colmap ) #+0.109508050156
for c in im1.collections:
    c.set_edgecolor("face")
insert(im1)
#im1 = plt.contourf(x2, y2, normhmax3, levels = line,  cmap=colmap ) #+0.109508050156
#ax2.set_yticklabels([''])
patches('k',0.09429)
ax2.axis([32,41,0,2.2])
plt.gca().set_aspect('equal', adjustable='box')
ax2.set_xticklabels([''])
plt.ylabel(r'$y$', rotation=0)
plt.text(32.3,1.8,r'(b)')
#plt.colorbar()
ax3 = plt.subplot(3,1,3)
#plt.axis('equal')
#plt.axis([-2.2,2.2,32,41])
im1 = plt.contourf(x4, y4, (hmax4masked-hmax1masked)/(hmax1masked+1e-10), levels = line,  cmap=colmap ) #+0.109508050156
for c in im1.collections:
    c.set_edgecolor("face")
insert(im1)
#im1 = plt.contourf(x2, y2, normhmax4, levels = line,  cmap=colmap ) #+0.109508050156
#ax3.set_yticklabels([''])
patches('k',0.06667)
ax3.axis([32,41,0,2.2])
plt.gca().set_aspect('equal', adjustable='box')
plt.ylabel(r'$y$', rotation=0)
plt.xlabel(r'$x$')
plt.text(32.3,1.8,r'(c)')
#im1 = plt.imshow( hmax1masked)
plt.tight_layout(rect=[0, 0.08, 1, 1], w_pad=0.00, h_pad=0.00)
cbaxes = fig1.add_axes([0.11, 0.05, 0.8, 0.02]) 
cb = plt.colorbar(im1, ticks=lvls1, format='%.1f', cax = cbaxes, orientation='horizontal')
fig1.text(0.12,0.075, r'$h^*_{max}$', color='k', fontsize=14)

#fig1.tight_layout()
fig1.savefig('hmax_rasterized.pdf', format='pdf', dpi=300)






