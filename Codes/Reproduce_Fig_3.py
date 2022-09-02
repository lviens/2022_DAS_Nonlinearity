#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 11 08:39:00 2022

@author: lviens
"""
import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt

#%% Plot Figure 3ab
cm = plt.cm.get_cmap('rainbow')
range_chan = 10
let = 'ab'
isplot = 1
fnt = 12
fig = plt.figure(figsize= (10,3.5))

cp = 1
for station in  [5000, 7000] :
    # Load data          
    file_in = '../Data/Data_Figure_3ab_channel_' + str(station)+ '-' + str(station +range_chan ) + '.mat'
    data_mat = sio.loadmat(file_in)
    freq_r = np.squeeze(data_mat['freq_range'])
    PGAstraintmp2 = np.squeeze(data_mat['Peak_Strain'])
    dv = np.squeeze(data_mat['dv'])
    
    # Plot data
    ax = plt.subplot(1,2, cp )
    for sta in np.arange(dv.shape[0]): # loop over the numebr of channels
        for fr in np.arange(len(freq_r) ): # Loop over frequency band
            plt.scatter(PGAstraintmp2[sta,:,fr], np.ones(len(PGAstraintmp2[sta,:,fr])) * ( freq_r[fr]+freq_r[fr]*2)/2 , c = dv[sta,fr,:], s = 90, cmap = cm,vmin = -30 , vmax = 30 ,alpha =.8, marker = 'o') 

    plt.grid(linewidth = .5)
    plt.xlim(2*10**-10, 10**-7)
    ax.tick_params(bottom=True, top=True, left=True, right=True )
    plt.xticks(fontsize=fnt)
    plt.text(1.5*10**-10, 32.5  ,'(' + let[cp-1] + ')' , fontsize = fnt )
    plt.xlabel('Dynamic peak strain', fontsize=fnt )
    ax.set_xscale('log')
    if cp ==1:
        plt.ylabel('Central frequency (Hz)', fontsize=fnt)
    elif cp ==2:
        rect = plt.Rectangle( (2*10**-8, 20 ) ,  7*10**-8, 10, alpha = 1, facecolor = 'w', edgecolor = 'k',  zorder = 1 )
        ax.add_patch(rect)
        cbaxes = fig.add_axes([0.87, 0.64, 0.02, 0.2])
        cb = plt.colorbar( cax = cbaxes, orientation = 'vertical'  ) 
        cb.ax.set_ylabel('dv/v (%)', fontsize=fnt)
    
    cp+=1 
plt.tight_layout()
plt.show()
fig.savefig('../Figures/Fig_3ab.png', dpi=400)

#%% PLot Figure 3cd
print(' ')
print('Plotting Figures 3c-d, it might take a few minutes')

cm = plt.cm.get_cmap('rainbow')

fnt = 11
fig = plt.figure(figsize = (8,7))
sta0 = 500
cp =1
for freq in  [5, 10] : 
    file_in = '../Data/Data_Figure_3cd_Frequency_'+ str(freq)+ '-' + str(freq*2) +'.mat'
    data_mat = sio.loadmat(file_in)
    dv = np.squeeze(data_mat['dv'])
    Peak_Strain = np.squeeze(data_mat['Peak_Strain'])
    if cp == 1:
        ax1 = plt.subplot(2,1, cp )
    elif cp == 2:
        ax2 = plt.subplot(2,1, cp )
    for sta1 in np.arange(8500):
        plt.scatter(np.ones(len(Peak_Strain[sta1,:])) * ( sta1+sta0), Peak_Strain[sta1, :], c = dv[sta1,:], s=.5, cmap = cm, vmin = -30 , vmax = 30 ,alpha = .3, marker = 'o')

    plt.ylabel('Dynamic peak strain', fontsize = fnt )
    
    if cp ==1:
        plt.text(150, 8*10**-8, '(c)', fontsize = fnt)
    else:
        plt.xlabel('Channel #', fontsize = fnt)
        plt.text(150, 8*10**-8, '(d)', fontsize = fnt)
        
    
    plt.grid(linewidth = .2)
    plt.title('Frequency band: ' +  str(freq) + '-' + str(freq*2) + ' Hz', fontsize = fnt)
    plt.xlim(500, 9000 )
    plt.ylim(1 * 10**-10,  9.9*10**-8 )
    plt.xticks(fontsize = fnt)
    plt.yticks(fontsize = fnt)
    cp+=1


ax1.set_yscale('log')
ax2.set_yscale('log')

ax1.tick_params(bottom=True, top=True, left=True, right=True)
ax2.tick_params(bottom=True, top=True, left=True, right=True)

pos = [.09 , .56  ,  .85 , .405 ] 
ax1.set_position(pos)
pos = [.09 , .07  ,  .85 , .405 ] 
ax2.set_position(pos)
 
fig.savefig('../Figures/Fig_3cd.png', dpi=150)

