#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 27 13:37:14 2022

@author: lviens
"""

import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator)
                               
#%% Plot Figure 4a
f1ini = np.arange(2,21) 

outputf =  '../Data/Data_Figure_4a.mat'
data_mat = sio.loadmat(outputf ) 

dv = np.squeeze(data_mat['dv']) 
cc = np.squeeze(data_mat['cc']) 
PGSmaxall = np.squeeze(data_mat['PGSmax'])
PGSRmaxall = np.squeeze(data_mat['PGSRmaxall']) 


fnt = 14
fig = plt.figure(figsize = (12,6))
sub = plt.subplot(111)
plt.imshow(dv, aspect = 'auto' , cmap = 'rainbow' , clim = (-30,30),  extent = (500, 9000, (f1ini[-1]*2+ f1ini[-1] )/2,  (f1ini[0]*2+ f1ini[0] )/2 ) )
plt.xlabel('Channel #', fontsize = fnt)
plt.ylabel('Central frequency (Hz)', fontsize = fnt)
plt.grid(linewidth = .5)
plt.xticks(fontsize = fnt)
plt.yticks(fontsize = fnt)
plt.text(0, 3.8, '(a)' ,fontsize = fnt)
sub.yaxis.set_minor_locator(MultipleLocator(1))
sub.xaxis.set_minor_locator(MultipleLocator(100))

sub.tick_params(bottom=True, top=True, left=True, right=True )
cbaxes = fig.add_axes([0.915, 0.35, 0.02, 0.29])
cb = plt.colorbar(cax = cbaxes, orientation = 'vertical'  ) 
cb.ax.set_ylabel('dv/v (%)', fontsize=fnt)
plt.yticks(fontsize= fnt)
pos = [.07, .09,  .82, .8 ] 
sub.set_position(pos)

fig.savefig('../Figures/Fig_4a.png', dpi=400)



#%% Plot Figure 4b-g
file_name = '../Data/Data_Figure_4bg.mat'
data = sio.loadmat(file_name)
Selected_PGV = np.squeeze(data['Selected_PGV'])
VS30 = np.squeeze(data['VS30'])
Selected_dv = np.squeeze( data['Selected_dv'])
channels = np.squeeze(data['channels'])

 
cp = 1

fig = plt.figure(figsize = (12, 8) )
for fr in  [0, 13, 18] :  
    sub1 = plt.subplot(2, 3, cp)
    if cp == 1 :
        plt.ylabel('dv/v (%)')
    plt.xlabel('Dynamic peak strain', fontsize = fnt)
    plt.scatter( Selected_PGV[fr,:] , Selected_dv[fr,:], c = channels, cmap = 'magma'  )
    plt.grid(linewidth = .5)
    sub1.set_xscale('log')
    plt.title('Filter: ' + str(f1ini[fr] ) + '-' +str(f1ini[fr] *2)+ ' Hz', fontsize = fnt)
    plt.ylim(-33,9)
    plt.xticks(fontsize = fnt)
    plt.yticks(fontsize = fnt)
    if cp==1 :
        plt.ylabel('dv/v (%)', fontsize = fnt)
        plt.text(5*10**-9, 9, '(b)', fontsize = fnt)
    elif cp ==2 : 
        plt.text(5*10**-10, 9, '(c)', fontsize = fnt)
    elif cp ==3:
        plt.text(3*10**-10, 9, '(d)', fontsize = fnt)

        
    if cp == 1:
        rect = plt.Rectangle( (8*10**-9, -32 ) ,  33*10**-9, 12, alpha = 1, facecolor = 'w', edgecolor = 'k',  zorder = 1 )
        sub1.add_patch(rect)
        cbaxes = fig.add_axes([0.09, 0.66, 0.13, 0.019])
        cb = plt.colorbar( cax = cbaxes, orientation = 'horizontal'  ) 
        cb.ax.set_xlabel('Channel #', fontsize=fnt)
        plt.xticks(fontsize= fnt)
    sub1.tick_params(bottom=True, top=True, left=True, right=True )

    sub2 = plt.subplot(2, 3, cp + 3)
    plt.ylim(-33, 9)
    plt.scatter(VS30, Selected_dv[fr,:], c = channels, cmap = 'magma')
    plt.xlabel( '$V_{S30}$ (m/s)', fontsize = fnt)
    plt.grid(linewidth = .5)
    if cp==1 :
        plt.ylabel('dv/v (%)', fontsize = fnt)
        plt.text(3, 9.5, '(e)', fontsize = fnt)
    elif cp ==2:
        plt.text(3, 9.5, '(f)', fontsize = fnt)
    elif cp ==3 : 
        plt.text(3, 9.5, '(g)', fontsize = fnt)
    plt.xticks(fontsize = fnt)
    plt.yticks(fontsize = fnt)
    sub2.tick_params(bottom=True, top=True, left=True, right=True )
    cp+=1

plt.tight_layout()
plt.show()
fig.savefig('../Figures/Fig_4b-g.png', dpi=400)

