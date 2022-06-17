#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  9 14:22:17 2022

@author: lviens
"""

import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt


#%% Folder were the ACFs are located 
fold = '../Data/'

#%% Channels and filters to plot

statot = [5000, 7000] # Channel #
filters = [10, 15] # lower limit of the bandpass filer in Hz
#%% Some variables for the plot
fig = plt.figure(figsize = (9,11) )
cl = .7  
fnt = 12
cp = 1

#%% Loop over the filters and channels
for f1 in filters :
    f2 = f1*2
    freq = [f1, f2]
    for staplt in np.arange(len(statot)):
        data_mat = sio.loadmat(fold + 'Data_Figure_2_Channel_' + str(statot[staplt])  +'_' + str(freq[0]) +'-' + str(freq[1]) + '_Hz.mat')  
        ACFall =np.squeeze(data_mat['ACFs']) # Load ACFs
        PGSall = np.squeeze(data_mat['Filtered_PGS'] ) # Load bandpass filtered peak ground strain
        delta = np.squeeze(data_mat['fs_strain'] ) # Sampling rate in Hz

        sortpgs = np.argsort(PGSall) # sort bandpass filtered peak ground strain
                
        t3 =np.arange(0,len(ACFall[0])/delta ,1/delta) # Time vector
        
        # plot the data
        if cp ==1:
            ax1  = plt.subplot(3,2, cp)
        elif cp ==2:
            ax2  = plt.subplot(3,2, cp)
        elif cp ==3:
            ax3  = plt.subplot(3,2, cp)
        elif cp ==4:
            ax4  = plt.subplot(3,2, cp)
            
        plt.imshow(np.array(ACFall)[sortpgs].T, aspect = 'auto' , extent = ( 0,len(sortpgs), t3[-1], t3[0]) , clim = (-cl, cl), cmap = 'coolwarm')    
        plt.grid(linewidth = .25)
        plt.ylim(.2, 0)    
        
        if cp ==1 or cp ==3:
            plt.tick_params(bottom=True, top=True, left=True, right=True, labelright = False, labelleft = True)
            plt.ylabel('Time (s)', fontsize =fnt )
        else:
            plt.tick_params(bottom=True, top=True, left=True, right=True, labelright = True, labelleft = False)

        plt.plot( np.mean(np.array(ACFall)[sortpgs[:10]], axis = 0)*10+10, t3, linewidth = 3, c = 'k')
        if cp == 3 or cp ==4:          
            plt.title('Filter: '+ str(freq[0]) + '-' + str(freq[1]) + ' Hz', fontsize =fnt )
        else:
            plt.title('ACFs: channel ' + str(statot[staplt]) + '\nFilter: '+ str(freq[0]) + '-' + str(freq[1]) + ' Hz' , fontsize =fnt )
            
      
        if cp ==1:
            plt.text(-10, -0.01 , '(a)' , fontsize = fnt)
            rect = plt.Rectangle( (65, .135 ) ,  35, .2075, alpha = .5, facecolor = 'w', edgecolor = 'k',  zorder = 1 )
            ax1.add_patch(rect)
            cbaxes = fig.add_axes([0.4, 0.635, 0.02, 0.07])
            cb = plt.colorbar( cax = cbaxes, orientation = 'vertical'  ) 
            cb.ax.set_title('    Clipped amp.', fontsize=fnt)
        elif cp ==2 : 
             plt.text(-3, -0.01 , '(b)' , fontsize = fnt)
        elif cp ==3 : 
             plt.text(-10, -0.01 , '(c)' , fontsize = fnt)
        elif cp ==4 : 
             plt.text(-3, -0.01 , '(d)' , fontsize = fnt)
            

        if cp == 1:
            ax5  = plt.subplot(3,2, 5)
            plt.scatter(np.arange(len(PGSall)) , PGSall[sortpgs] , s = 100 , c = 'r', edgecolor = 'k' , label = str(f1) + '-' + str(f2) + 'Hz' )
            ax5.set_ylabel('Dynamic peak strain', fontsize=fnt)
        elif cp == 3:
            ax5.scatter(np.arange(len(PGSall)) , PGSall[sortpgs] , s = 100 , c = 'b' , edgecolor = 'k', label = str(f1) + '-' + str(f2) + 'Hz' )
            ax5.grid()
            ax5.set_xlim(0,102)
            ax5.set_ylim(1*10**-10, 5*10**-8)
            ax5.set_yscale('log')
            plt.setp(ax5.get_xticklabels(), fontsize=fnt )
            plt.setp(ax5.get_yticklabels(),fontsize=fnt)
            ax5.legend( fontsize=fnt, loc='upper left')
            ax5.tick_params(bottom=True, top=True, left=True, right=True)
        elif cp ==2:
            ax6  = plt.subplot(3,2, 6)
            plt.scatter(np.arange(len(PGSall)) , PGSall[sortpgs] , s = 100 , c = 'r', edgecolor = 'k', label = str(f1) + '-' + str(f2) + 'Hz' )
        elif cp == 4:
            ax6.scatter(np.arange(len(PGSall)) , PGSall[sortpgs] , s = 100 , c = 'b' , edgecolor = 'k', label = str(f1) + '-' + str(f2) + 'Hz')
            ax6.grid()
            ax6.set_xlim(0,102)
            ax6.set_ylim(1*10**-10, 5*10**-8)
            ax6.set_yscale('log')
            ax6.tick_params(bottom=True, top=True, left=True, right=True, labelright = True, labelleft = False)
            ax6.legend( fontsize=fnt, loc='upper left')
            plt.setp(ax6.get_xticklabels(), fontsize=fnt )
            plt.setp(ax6.get_yticklabels(),fontsize=fnt)
            
        cp+=1
        
ax6.set_xlabel('Earthquake number', fontsize =fnt )
ax6.text(-5, 6* 10**-8 , '(f)' , fontsize = fnt)
ax5.set_xlabel('Earthquake number', fontsize =fnt )
ax5.text(-10, 6* 10**-8 , '(e)' , fontsize = fnt)

plt.setp(ax1.get_xticklabels(), fontsize = fnt )
plt.setp(ax1.get_yticklabels(), fontsize = fnt) 
plt.setp(ax2.get_xticklabels(), fontsize = fnt )
plt.setp(ax2.get_yticklabels(), fontsize = fnt) 
plt.setp(ax3.get_xticklabels(), fontsize = fnt )
plt.setp(ax3.get_yticklabels(), fontsize = fnt) 
plt.setp(ax4.get_xticklabels(), fontsize = fnt )
plt.setp(ax4.get_yticklabels(), fontsize = fnt) 

pos = [.085 , .63  ,  .415 , .32] 
ax1.set_position(pos) 
pos = [.52 , .63  ,  .415 , .32 ] 
ax2.set_position(pos)
pos = [.085 , .255  ,  .415 , .32 ] 
ax3.set_position(pos)
pos = [.52 , .255  ,  .415 , .32 ] 
ax4.set_position(pos) 
pos = [.085 , .06  ,  .415 , .15 ] 
ax5.set_position(pos) 
pos = [.52 , .06  ,  .415 , .15 ] 
ax6.set_position(pos)
fig.savefig('../Figures/Fig_2.png', dpi=400)