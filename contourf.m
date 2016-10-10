clear all
close all
clc

load SPH_GRIDm.txt;

load NV_JNNFM2005_f6.txt

x_jnnfm=NV_JNNFM2005_f6(:,1);
y_jnnfm=NV_JNNFM2005_f6(:,2);

x_j_av=(min(x_jnnfm)+max(x_jnnfm))/2

cgrid=[SPH_GRIDm];


YC=cgrid(:,1)';
XC=cgrid(:,2)';
VY=cgrid(:,3)';
VX=cgrid(:,4)';
V=sqrt(VX.^2+VY.^2);
PRES=cgrid(:,5)';
CO=cgrid(:,6)';
Tag=cgrid(:,7)';

rangex=0:0.01:max(XC);
rangey=0:0.01:max(YC);

[x y]=meshgrid(rangex,rangey);
vx=griddata(XC,YC,VX,x,y);
vy=griddata(XC,YC,VY,x,y);
v=griddata(XC,YC,V,x,y);
pres=griddata(XC,YC,PRES,x,y);
co=griddata(XC,YC,CO,x,y);

nlev=600;
clev=linspace(min(min(vx)),max(max(vx)),nlev);

figure
contourf(x,y,vx,clev,'linecolor','none')
axis('equal')
colormap(jet(nlev))

figure
contourf(x,y,vx,clev,'linecolor','none')
axis('equal')


figure
surf(x,y,vx)
shading interp
view([0 90])
axis('equal')