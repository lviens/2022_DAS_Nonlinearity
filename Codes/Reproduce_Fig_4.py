#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 09:49:40 2022

@author: lviens
"""
import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator)
                               
#%% Plot Figure 4
file_name = '../Data/Data_Figure_4.mat'
data = sio.loadmat(file_name)
Selected_PGV = np.squeeze(data['Selected_PGV'])
dvstd  = np.squeeze(data['dvvstdsel'])  
VS30 = np.squeeze(data['VS30'])
Selected_dv = np.squeeze( data['Selected_dv'])
channels = np.squeeze(data['channels'])

dv = np.squeeze(data['dvall']) 
PGSmaxall = np.squeeze(data['PGSmaxall'])
 
f1ini = np.arange(3,21) 


fnt = 14
cl = 30

fig, axs = plt.subplots(nrows=3, ncols=3, figsize=(12, 12))

pl = axs[0,0].imshow(dv, aspect = 'auto' , cmap = 'rainbow' , clim = (-cl, cl),  extent = (500, 9000, (f1ini[-1]*2+ f1ini[-1] )/2,  (f1ini[0]*2+ f1ini[0] )/2 ) )

axs[0,0].set_xlabel('Channel #', fontsize = fnt)
axs[0,0].set_ylabel('Central frequency (Hz)', fontsize = fnt)
axs[0,0].grid(linewidth = .5)
plt.xticks(fontsize= fnt)
plt.yticks(fontsize= fnt)
axs[0,0].text(300, 3.8, '(a)' ,fontsize = fnt)
axs[0,0].set_title('Average dv/v' ,fontsize = fnt)
axs[0,0].yaxis.set_minor_locator(MultipleLocator(1))
axs[0,0].xaxis.set_minor_locator(MultipleLocator(100))
axs[0,0].xaxis.set_tick_params(labelsize=fnt)
axs[0,0].yaxis.set_tick_params(labelsize=fnt)
axs[0,0].tick_params(bottom=True, top=True, left=True, right=True )

rect = plt.Rectangle( (6900, 24 ) ,  2000, 8, alpha = .8, facecolor = 'w', edgecolor = 'k',  zorder = 1 )
axs[0,0].add_patch(rect)

cbaxes = fig.add_axes([0.395, 0.71, 0.08, 0.01])
cb = fig.colorbar(pl, cax = cbaxes, orientation = 'horizontal'  ) 
cb.ax.set_title('dv/v (%)', fontsize=fnt)
cb.ax.set_xlabel(' ', fontsize=fnt)
 
pl2 = axs[0,1].imshow(PGSmaxall, aspect = 'auto' , cmap = 'rainbow' , clim = (1*10**-11 , 3*10**-8 ),  extent = (500, 9000, (f1ini[-1]*2+ f1ini[-1] )/2,  (f1ini[0]*2+ f1ini[0] )/2 ) )

axs[0,1].set_xlabel('Channel #', fontsize = fnt)
axs[0,1].grid(linewidth = .5)
plt.xticks(fontsize= fnt)
plt.yticks(fontsize= fnt)
axs[0,1].text(300, 3.8, '(b)' ,fontsize = fnt)
axs[0,1].yaxis.set_minor_locator(MultipleLocator(1))
axs[0,1].xaxis.set_minor_locator(MultipleLocator(100))
axs[0,1].xaxis.set_tick_params(labelsize=fnt)
axs[0,1].yaxis.set_tick_params(labelsize=fnt)
axs[0,1].set_xlabel('Channel #', fontsize = fnt)
axs[0,1].yaxis.tick_right()
axs[0,1].tick_params(bottom=True, top=True, left=True, right=True )
axs[0,1].set_title('Average maximum dynamic peak strain' ,fontsize = fnt)

rect = plt.Rectangle( (6900, 23 ) ,  2000, 8, alpha = .8, facecolor = 'w', edgecolor = 'k',  zorder = 1 )
axs[0,1].add_patch(rect)
cbaxes = fig.add_axes([0.86, 0.72, 0.08, 0.01])
cb = fig.colorbar(pl2, cax = cbaxes, orientation = 'horizontal'  ) 
cb.ax.set_title('Peak strain', fontsize=fnt)
cb.ax.set_xlabel(' ', fontsize=fnt)
axs[0,2].axis('off')


t = channels
tall = np.arange(500,9000)
valplot = VS30 
cp = 0

for fr in  [0,12,17] :  

    axs[1,cp].plot( [ Selected_PGV[fr,:], Selected_PGV[fr,:] ] , [  Selected_dv[fr,:]+dvstd[fr,:] ,Selected_dv[fr,:] - dvstd[fr,:] ] , 'k', zorder = .1)
    sc = axs[1,cp].scatter( Selected_PGV[fr,:] , Selected_dv[fr,:], s = 50 , c = t , cmap = 'magma', zorder = 1,edgecolors = 'k' , linewidth = .4 )
    axs[1,cp].grid(linewidth = .5)
    axs[1,cp].set_xlabel('Dynamic peak strain', fontsize = fnt)
    axs[1,cp].set_xscale('log')
    axs[1,cp].set_title('Filter: ' + str(f1ini[fr] ) + '-' +str(f1ini[fr] *2)+ ' Hz', fontsize = fnt)
    axs[1,cp].set_ylim(-33,9)
    plt.xticks(fontsize= fnt)
    if cp==0 :
        axs[1,cp].set_ylabel('dv/v (%)', fontsize = fnt)
        axs[1,cp].text( 3.7*10**-9, 10 , '(c)', fontsize = fnt)
        rect = plt.Rectangle( (4.5*10**-9, -32.5 ) ,  23*10**-9, 14, alpha = 1, facecolor = 'w', edgecolor = 'k',  zorder = 1 )
        axs[1,cp].add_patch(rect)
        cbaxes = fig.add_axes([0.09, 0.41, 0.13, 0.019])
        cb = plt.colorbar(sc,  cax = cbaxes, orientation = 'horizontal'  ) 
        cb.ax.set_xlabel('Channel #', fontsize=fnt)
        axs[1,cp].set_xlim(4*10**-9 , 10**-7)
    elif cp ==1 : 
        axs[1,cp].text(4.5*10**-10, 10 , '(d)', fontsize = fnt)
        axs[1,cp].yaxis.set_ticklabels([])
        axs[1,cp].set_xlim(5*10**-10 , 10**-8)
    elif cp ==2:
        axs[1,cp].text(3.2*10**-10, 10 , '(e)', fontsize = fnt)
        axs[1,cp].yaxis.tick_right()
        axs[1,cp].set_xlim(3.5*10**-10 , 10**-8)
    axs[1,cp].yaxis.set_major_locator(MultipleLocator(5))

    axs[1,cp].tick_params(bottom=True, top=True, left=True, right=True )
    axs[1,cp].xaxis.set_tick_params(labelsize=fnt)
    axs[1,cp].yaxis.set_tick_params(labelsize=fnt)
    

    axs[2,cp].plot( [ valplot,valplot ] , [  Selected_dv[fr,:]+dvstd[fr,:] ,Selected_dv[fr,:] - dvstd[fr,:] ] , 'k', zorder = .1)
    axs[2,cp].scatter(valplot , (Selected_dv[fr,:]), s = 50 ,c = t , cmap = 'magma', zorder = 1, edgecolors = 'k', linewidth = .4)
    axs[2,cp].set_xlabel( '$V_{S' + str(30) + '}$ (m/s)', fontsize = fnt)
    axs[2,cp].grid(linewidth = .5)
    axs[2,cp].set_ylim(-33,9)
    if cp==0 :
        axs[2,cp].set_ylabel('dv/v (%)', fontsize = fnt)
        axs[2,cp].text(26, 10 , '(f)', fontsize = fnt)
    elif cp ==1:
        axs[2,cp].text(26, 10, '(g)', fontsize = fnt)
        axs[2,cp].yaxis.set_ticklabels([])

    elif cp ==2 : 
        axs[2,cp].text(26, 10 , '(h)', fontsize = fnt)
        axs[2,cp].yaxis.tick_right()
    axs[2,cp].xaxis.set_tick_params(labelsize=fnt)
    axs[2,cp].yaxis.set_tick_params(labelsize=fnt)
    axs[2,cp].yaxis.set_major_locator(MultipleLocator(5))
    axs[2,cp].tick_params(bottom=True, top=True, left=True, right=True )
 
    cp+=1

pos = [0.05 , .679 ,  .44, .29 ] 
axs[0,0].set_position(pos) 

pos2 = [0.52 , .679 ,  .44, .29 ] 
axs[0,1].set_position(pos2) 

yhe = .24
pos = [0.07 , .36 ,  .275, yhe ] 
axs[1,0].set_position(pos) 

pos2 = [0.37 , .36 , .275, yhe] 
axs[1,1].set_position(pos2) 

pos2 = [0.67 , .36 , .275, yhe ] 
axs[1,2].set_position(pos2) 

pos = [0.07 , .05 ,  .275, yhe ] 
axs[2,0].set_position(pos) 

pos2 = [0.37 , .05 , .275, yhe] 
axs[2,1].set_position(pos2) 

pos2 = [0.67 , .05 , .275, yhe ] 
axs[2,2].set_position(pos2) 

plt.show()
fig.savefig('../Figures/Fig_4.png', dpi=400)
