# Python codes to detect soil non-linear behavior during earthquakes recorded by Distributed Acoustic Sensing (DAS) 

The codes are for the following manuscript:
- Viens L., L. F. Bonilla, Z. J. Spica, K. Nishida, T. Yamada, S. Shinohara, Nonlinear earthquake response of marine sediments with distributed acoustic sensing (Submitted, pre-print link coming soon)

## Description:
* The **Codes** folder contains:

  - **Reproduce_Fig_1cde.py** to reproduce Figure 1cde of the paper (plot strain waveforms for Mv 2.5 earthquake, strain-rate data at station 4000, and compute ACFs)
  - **Reproduce_Fig_2.py** to reproduce Figure 2 (ACFs at two channels for two frequency bands)
  - **Reproduce_Fig_3.py** to reproduce Figure 3 of the paper ( ).
  - **Reproduce_Fig_4.py** to reproduce the Figure 4 of the paper ( ).

* The **Data** folder contains:
  - The data to reproduce Figures 2-4.
  - The data to reproduce Figure 1cde (too big for github) need to be downloaded at: https://drive.google.com/file/d/13Lk2pSpx4m9JTnw6Am0lyL1xRaNfHypZ/view?usp=sharing

* The **Figures** folder contains 6 figures that can be plotted with the 4 codes. 


## Codes and their outputs:

* The **Reproduce_Fig_1cde.py** code reads the strain data for the MV 2.5 earthquake (Warning: the data were downsampled to 50 Hz for this example to reduce the size of the file. Fig. 1c is slightly different to that shown in the manucript as the bandpass filter applied to the data is 2-25 Hz, whereas it is 2-30 Hz in the manuscript). The strain-rate data at channel 4000 have a 500 Hz sampling rate and are used to compute the frequency dependent ACFs at this channel. 


* The **Reproduce_Fig_2.py** code is used to plot the noise and earthquake ACFs along the 3 lines. The Figure below shows the ACFs along Line 1. 


* The **Reproduce_Fig_3.py** code compares the bedrock depths from the JIVSM, noise ACF, and earthquake ACF measurements. 


* The **Reproduce_Fig_4.py** code shows a comparison of the Axitra ACF simulations with the observed earthquake and noise ACFs. 
