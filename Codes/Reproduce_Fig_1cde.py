#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 20:49:04 2022

@author: lviens
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
 The data for this code are too big for Github and need to be downloaded from: https://drive.google.com/file/d/13Lk2pSpx4m9JTnw6Am0lyL1xRaNfHypZ/view?usp=sharing
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""
import numpy as np
import scipy.io as sio
import scipy.signal, sys
from os.path import exists
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt


def taper(x,p):
    # Taper the data
    if p <= 0.0:
        return x
    else:
        f0 = 0.5
        f1 = 0.5
        n  = len(x)
        nw = int(p*n)
        if nw > 0:
            ow = np.pi/nw
            w = np.ones( n )
            for i in range( nw ):
                w[i] = f0 - f1 * np.cos(ow*i)
            for i in range( n-nw,n ):
                w[i] = 1.0 - w[i-n+nw]

            return x * w
        elif nw == 0:
            return x


def butter_bandpass_filter(data, lowcut, highcut, fs, order=4):
    # Bandpass filter 
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    y = filtfilt(b, a, data)
    return y


def next_power_of_2(n):
    # Bitwise version
    """
    Return next power of 2 greater than or equal to n
    """
    return 2**(n-1).bit_length()


def apcc2(x1, dt, lag0, lagu):
    """
     Compute autocorrelation functions
    """
    # Preprocessing
    x1 = x1 - np.mean(x1)
    x1 = taper(x1, 0.05)
    N  = len(x1)
    Nz = next_power_of_2( 2*N )

    # Analytic signal and normalization
    xa1 = scipy.signal.hilbert(x1)
    xa1 = xa1 / np.abs(xa1)

    # Padding zeros
    xa1 = np.append(xa1, np.zeros((Nz-N), dtype=np.complex_))

    # FFT, correlation and IFFT
    xa1 = np.fft.fft(xa1)
    amp = xa1 * np.conj(xa1)
    pcc = np.real( np.fft.ifft(amp) ) / N
    pcc = np.fft.ifftshift(pcc)
    tt  = Nz//2 * dt
    t   = np.arange(-tt, tt, dt)
    return t[(t >= lag0) & (t <= lagu)], pcc[(t >= lag0) & (t <= lagu)]

#%% Check if the data have been downloaded 

file_exists = exists('../Data/Data_Figure_1cde.mat')
if not file_exists:
    sys.exit('\n../Data/Data_Figure_1cde.mat is not found. \nDownload the data from: https://drive.google.com/file/d/13Lk2pSpx4m9JTnw6Am0lyL1xRaNfHypZ/view?usp=sharing')

#%% Load data MV 2.5 earthquake
# Info from Hi-net: 2019-11-28 23:17:32.83, lat: 39.168, lon: 142.565, Depth: 29.7, Magnitude 2.5V   

file = sio.loadmat('../Data/Data_Figure_1cde.mat')
Strain_data =  np.squeeze(file['Strain_data']) # Strain data (50 Hz sampling rate) 
StrainRate_data_4000 =  np.squeeze(file['StrainRate_data_4000']) # Strain-rate data at channel 4000 (500 Hz sampling rate) 
fs_strain = np.squeeze(file['fs_strain']) # Sampling rate of the strain data
fs_strainRate_4000 = np.squeeze( file['fs_strainRate_4000'])# Sampling rate of the strain-rate data at channel 4000
stations =  np.squeeze(file['stations']) # initial and last channel stations
Strain_filter = np.squeeze(file['filter']) # bandpass filter applied to the strain data
 
#%% Plot strain data
fnt = 12
xlim = [stations[0], stations[-1]]
t1 = np.arange(0,len(Strain_data[0])/fs_strain ,1/fs_strain) + 4
cl = 1.2*10**-9


fig2 = plt.figure(figsize =(10,9))

ax2 = fig2.add_subplot(221)
plt.imshow(Strain_data.T, aspect = 'auto',  clim = (-cl, cl), cmap = 'bone' , extent = ( xlim[0], xlim[-1], t1[-1], t1[0]  ))

plt.title('$M_V$ 2.5 earthquake, Filter: ' +  str(Strain_filter[0]) + '-' + str(round(Strain_filter[1]) ) + ' Hz' , fontsize = fnt)

plt.ylabel('Time (s)', fontsize = fnt)
plt.xlabel('Channel #', fontsize = fnt)
plt.xticks(fontsize = fnt )
plt.yticks(fontsize = fnt )
ax2.tick_params( bottom=True, top=True, left=True, right=True)

plt.ylim(40, 4)
plt.xlim(xlim[0], xlim[1]+1)
plt.grid(linewidth = .5)


plt.text(5500, 6, 'P-wave', weight = 'bold')
plt.arrow(5700, 6.75 , 200, 1.4, shape = 'full')

plt.text(5500, 17, 'S-wave',  weight = 'bold')
plt.arrow(5700, 15 , 200, -1.4, shape = 'full')

plt.text(50, 4 , '(c)', fontsize = fnt)


# Plot colorbar
rect = plt.Rectangle( (7700, 29),  1300, 11, alpha = .75, facecolor = 'w', edgecolor = 'k',  zorder = 1 )
ax2.add_patch(rect)
cbaxes = fig2.add_axes([0.86, 0.65, 0.1, 0.02])
cb = plt.colorbar( cax = cbaxes, orientation = 'horizontal'  ) 
cb.ax.set_title('Strain', fontsize = fnt) 


#%% Subplot Fig. 1(d)
f1 = [2 ,4 ,6 ,8 ,10 , 12, 14 ] # filters applied to the data: 2 -> 2-4 Hz filter
time_minus = 5
time_tot = 15
order = 4
t = np.arange(0,len(StrainRate_data_4000)/fs_strainRate_4000 ,1/fs_strainRate_4000) 

# Find the 15 s window near the peak strain rate after bandpass filtering the data between 2 and 30 Hz 
tmp_strainRate = butter_bandpass_filter(StrainRate_data_4000, lowcut=2, highcut=30, fs = fs_strainRate_4000, order=order) 
argmaxtot = np.argmax(abs(tmp_strainRate))


ax3 = plt.subplot(223)
dz = 0
dzval = 5*10**-10

for fil in np.arange(len(f1)):
    dataeq = butter_bandpass_filter(StrainRate_data_4000, lowcut=f1[fil], highcut=f1[fil]*2, fs = fs_strainRate_4000, order=order) # bandpass filter the strain-rate data
    plt.plot(t, dataeq + dz, 'k', linewidth = .75)
    plt.text(30, dataeq[30*fs_strainRate_4000] + dz+.2*dzval, str(f1[fil]) + '-' + str(f1[fil]*2) + ' Hz' )
    plt.xlabel('Time (s)', fontsize = fnt)
    plt.ylabel('Strain-rate ($s^{-1}$)', fontsize = fnt)
    plt.xlim(5, 35)
    dz+=dzval
    
plt.grid(linewidth = .5)
ax3.tick_params(  bottom=True, top=True, left=True, right=True)
ymax = np.max(abs(dataeq))+ np.max(abs(dataeq))*.1 +dz
plt.ylim(-.15*10**-9, ymax -3*10**-10 )
rect = plt.Rectangle( (t[argmaxtot]-5, -ymax ) , 15, ymax*2, alpha = .25, facecolor = 'k' )
ax3.add_patch(rect)
plt.xticks(fontsize=fnt )
plt.yticks(fontsize=fnt )
plt.title( 'Channel 4000: waveforms' , fontsize = fnt )
plt.text(2, dz -dzval*.15 , '(d)', fontsize = fnt)



#%% Subplot Fig. 1(e)

dur_ACF = 1
dz2 = 0
dzval2 = 2.5
ax4 = plt.subplot(224)
for fil in np.arange(len(f1)):
    filt_data = butter_bandpass_filter(StrainRate_data_4000, lowcut=f1[fil], highcut=f1[fil]*2, fs = fs_strainRate_4000, order=order) 
    filt_data = taper(filt_data,0.01)
    
    data = filt_data[argmaxtot - time_minus*fs_strainRate_4000: argmaxtot + (time_tot- time_minus)*fs_strainRate_4000]
    [tacf, tmp] = apcc2(data, 1/fs_strainRate_4000, lag0 = 0, lagu = dur_ACF)
    
    plt.plot(tacf, tmp+dz2,'k' ,linewidth = 3)
    plt.xlabel('Time (s)', fontsize = fnt)
    plt.ylabel('Normalized amplitude', fontsize = fnt)
    plt.title('Channel 4000: ACFs', fontsize = fnt)
    plt.xlim(tacf[0], .4)
    if fil >3:
        plt.text(.39, tmp[int(.4*fs_strainRate_4000)] + dz2+.15*dzval2 , str(f1[fil]) + '-' + str(f1[fil]*2) + ' Hz' , ha='right')
    else:
        plt.text(.39, tmp[int(.4*fs_strainRate_4000)] + dz2+.275*dzval2 , str(f1[fil]) + '-' + str(f1[fil]*2) + ' Hz' , ha='right')
    
    dz2+=dzval2
plt.ylim(-1, 16.5)
plt.text(-.05, dz2-dzval2*.3 , '(e)', fontsize = fnt)
plt.xticks(fontsize = fnt )
plt.yticks(fontsize = fnt )
ax4.tick_params(bottom=True, top=True, left=True, right=True)
plt.grid()    


#Set subplot positions
pos2 = [0.075 , .6 ,  .9, .36 ] 
ax2.set_position(pos2) 
pos3 = [.075 , .06  , .4 , .45] 
ax3.set_position(pos3) 
pos4 = [.575 , .06  ,  .4 , .45 ] 
ax4.set_position(pos4) 

plt.show()
fig2.savefig('../Figures/Fig_1cde.png', dpi=300)