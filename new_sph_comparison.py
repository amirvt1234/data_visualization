import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.interpolate import interp1d

mpl.rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
mpl.rc('font', size=13)
mpl.rc('text', usetex=True)
mpl.rc('xtick', labelsize=13, color='black')
mpl.rc('ytick', labelsize=13, color='black')
mpl.rc('lines', linewidth=1.0)
mpl.rcParams['axes.linewidth'] = 1.0
mpl.rcParams['axes.edgecolor'] = 'black'
plt.rc('text', usetex=True)

YYB   = np.zeros((1099, 27))
GN    = np.zeros((np.size(np.loadtxt('./GN/g1r'), axis=0), 27))
vxGN  = np.zeros((np.size(np.loadtxt('./GN/g1r'), axis=0), 27))
vyGN  = np.zeros((np.size(np.loadtxt('./GN/g1r'), axis=0), 27))
EXP   = np.zeros((751, 27))
EXPOS = np.zeros((1251, 6))
vxEXP = np.zeros((751, 27))
vyEXP = np.zeros((751, 27))



for i in xrange (26):
  fname = './COULWAVE/' + 'tmsr00'
  ii = str(i+1)
  if (i<9):
    ii = '0' + str(i+1)
  fname =fname + ii + '.dat'
  YYB[:,0]   = np.loadtxt(fname)[1:1100,0]
  YYB[:,i+1] = np.loadtxt(fname)[1:1100,1]
fname=  './Experiment/OFFSHORE.dat'
for i in xrange (5):
  EXPOS[:,0]   = np.loadtxt(fname)[:,0]
  EXPOS[:,i+1] = np.loadtxt(fname)[:,i+1]
 
for i in xrange (21):
  ii = ii + 1;
  if (i==0):  
    fname = './Experiment/vel/R1_AV_Debad_adv';
    ii = 1;   
  if (i==7): 
    fname = './Experiment/vel/R2_AV_Debad_adv';
    ii = 1 ;
  if (i==14): 
    fname = './Experiment/vel/R3_AV_Debad_adv';
    ii = 1 ;
  fname1 = fname + str(ii) + '_Rep55.txt'
  vxEXP[:,0] = np.loadtxt(fname1)[:,0]
  vxEXP[:,i+6] = np.loadtxt(fname1)[:,1]
  vyEXP[:,0] = np.loadtxt(fname1)[:,0]
  vyEXP[:,i+6] = np.loadtxt(fname1)[:,2]
# wavegauge experiment
ii = 0 
for i in xrange (21):
  ii = ii + 1;
  if (i==0):  
    fname = './Experiment/R1_AV_Lowpass_Gauge_Rep55.txt';
    ii = 1;   
  if (i==7): 
    fname = './Experiment/R2_AV_Lowpass_Gauge_Rep55.txt';
    ii = 1 ;
  if (i==14): 
    fname = './Experiment/R3_AV_Lowpass_Gauge_Rep55.txt';
    ii = 1 ;
  EXP[:,0] = np.loadtxt(fname)[:,0]
  EXP[:,i+6] = np.loadtxt(fname)[:,ii]


for i in xrange (26):
  fname = './GN/g' + str(i+1) + 'r'
  GN [:,0]   = np.loadtxt(fname)[:,0]
  GN [:,i+1] = np.loadtxt(fname)[:,1]

for i in xrange (21):
  ii = i + 6
  fname = './GN/g' + str(ii) + 'r'
  vxGN [:,0]   = np.loadtxt(fname)[:,0]
  vxGN [:,i+6] = np.loadtxt(fname)[:,2]
  vyGN [:,0]   = np.loadtxt(fname)[:,0]
  vyGN [:,i+6] = np.loadtxt(fname)[:,3]


plt.close()
plt.clf()
plt.cla()



xnew = np.linspace(10,20,40)

#f1=[]; f2=[];
#for i in xrange(26):
#  f1.append(interp1d (EXP[:,0]+7.43, EXP[:,i+1], kind='cubic'))
#  f2.append(interp1d (GN [:,0]+2, GN[:,i+1], kind='cubic'))

x = np.linspace(11,19,5);
y = np.linspace(0,0.15,3);
y2 = np.linspace(0,1.,3);
abc = "abcdefghijklmn"

fig2 = plt.figure(3, facecolor=None, figsize=(8, 5)) #, figsize=(12, 12)
k = 0
for i in xrange(3):
  ii = i +1 
  jj = 0
  for j in xrange(4):
    jj = j+1
    if ((i*4+j+1)==8): k = 7;
    ax1 = plt.subplot(3,4,i*4+j+1)
    f1 = interp1d (EXP[::4,0]+7.43, EXP[::4,5+i*4+j+1+k], kind='cubic')
    f2 = interp1d (GN [::10,0]+2, GN[::10,5+i*4+j+1+k], kind='cubic')
    plt.plot(xnew, f2(xnew), 'k', label='2D-SGN' )
    plt.plot(SPH[:,0]+0.4, SPH[:,5+i*4+j+1+k], 'r--',label='GPUSPH')
    plt.plot(YYB[:,0]-0.15, YYB[:,5+i*4+j+1+k]-YYB[1,5+i*4+j+1+k], 'g-.', label='COULWAVE')
    plt.plot(xnew, f1(xnew), 'o b', markersize=3, markeredgecolor='b', label='Experiment')
    ax1.axis([10, 20, 0, 0.15])
    plt.yticks(y)
    plt.xticks(x)
    if (i==0 and j==0): plt.legend( fontsize=8, frameon=False, bbox_to_anchor=(0., 1.02, 3., .102), loc=3,
           ncol=4, mode="expand")
    if (i<2): ax1.set_xticklabels([''])
    if (j>0): ax1.set_yticklabels([''])
    plt.text(13.8,0.125,'('+abc[4*i +j]+') Gauge '+str(4*ii +jj))
    if (i==2): plt.xlabel(r't', fontsize=13)
    if (j==0): plt.ylabel(r'h', rotation=0, fontsize=13)



fig2.tight_layout(w_pad=1.,h_pad=0.01)
#fig2.tight_layout()
plt.savefig('allsonic.png')


x = np.linspace(11,19,5);
y = np.linspace(-3,3,4);

fig3 = plt.figure(4, facecolor=None, figsize=(8, 6)) #, figsize=(12, 12)
k = 0
for i in xrange(3):
  for j in xrange(4):
    if ((i*4+j+1)==8): k = 7;
    ax1 = plt.subplot(5,4,i*4+j+1)
    #f1 = interp1d (vxEXP[::4,0]+7.43, vxEXP[::4,5+i*4+j+1+k], kind='cubic')
    f2 = interp1d (vxGN [::10,0]+2, vxGN[::10,5+i*4+j+1+k], kind='cubic')
    plt.scatter(vxEXP[::4,0]+7.43, vxEXP[::4,5+i*4+j+1+k], facecolors='b', edgecolors='b', s=8, linewidth='0.5')
    #plt.plot(xnew, f1(xnew), 'o b', markersize=3)
    plt.plot(xnew, f2(xnew), 'k')
    ax1.axis([10, 20, -3, 4])
    plt.yticks(y)
    plt.xticks(x)
    if (i<2): ax1.set_xticklabels([''])
    if (j>0): ax1.set_yticklabels([''])
    plt.text(17,0.078,'WG '+str((i*4+j+k)%7+1)+'-'+str((i*4+j+k)/7+1))
    if (i==2): plt.xlabel(r't')
    if (j==0): plt.ylabel(r'h', rotation=0)
 

fig3.tight_layout(w_pad=1.,h_pad=0.01)
fig3.savefig('vel_allsonic.pdf')






