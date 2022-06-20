# Python codes to detect soil non-linear behavior during earthquakes recorded by Distributed Acoustic Sensing (DAS) 

The codes are for the following manuscript:
- Viens L., L. F. Bonilla, Z. J. Spica, K. Nishida, T. Yamada, S. Shinohara, Nonlinear earthquake response of marine sediments with distributed acoustic sensing (Submitted, pre-print link coming soon)

## Description:
* The **Codes** folder contains:

  - **Reproduce_Fig_1cde.py** to reproduce Figure 1cde of the paper (plot strain waveforms for Mv 2.5 earthquake, strain-rate data at station 4000, and compute ACFs)
  - **Reproduce_Fig_2.py** to reproduce Figure 2 (ACFs at two channels for two frequency bands)
  - **Reproduce_Fig_3.py** to reproduce Figure 3 of the paper
  - **Reproduce_Fig_4.py** to reproduce the Figure 4 of the paper.

* The **Data** folder contains:
* - The data to reproduce Figure 1cde are too big for github and are available [here](https://drive.google.com/file/d/13Lk2pSpx4m9JTnw6Am0lyL1xRaNfHypZ/view?usp=sharing). Note that they need to be moved to the **Data** folder before running the **Reproduce_Fig_1cde.py** code
  - The data to reproduce Figures 2-4.
  

* The **Figures** folder contains 6 figures that can be plotted with the 4 codes. 


## Codes and their outputs:

* The **Reproduce_Fig_1cde.py** code reads the strain data of the MV 2.5 earthquake (Warning: the data were downsampled to 50 Hz for this example to reduce the size of the file. Fig. 1c is slightly different from that shown in the manucript as the bandpass filter applied to the data is 2-25 Hz, whereas it is 2-30 Hz in the manuscript). The strain-rate data at channel 4000 (Figure 1d) have a 500 Hz sampling rate and are used to compute the frequency dependent ACFs shown in Figue 1e. This code contains the function used to compute the ACFs using the phase correlation method in the frequency domain.

![Figure 1](https://github.com/lviens/2022_DAS_Nonlinearity/blob/main/Figures/Fig_1cde.png)


* The **Reproduce_Fig_2.py** code shows the ACFs at channels 5000 and 7000 in the 10-20 and 15-30 Hz frequency bands.
![Figure 2](https://github.com/lviens/2022_DAS_Nonlinearity/blob/main/Figures/Fig_2.png)

* The **Reproduce_Fig_3.py** code shows the dv/v results at two stations for all the frequency bands and the dv/v results along the cable for two frequency bands. 
![Figure 3a-b](https://github.com/lviens/2022_DAS_Nonlinearity/blob/main/Figures/Fig_3ab.png)
![Figure 3cd](https://github.com/lviens/2022_DAS_Nonlinearity/blob/main/Figures/Fig_3cd.png)

* The **Reproduce_Fig_4.py** code shows the dv/v measurements computed between weak and strong ground motions.
![Figure 4a](https://github.com/lviens/2022_DAS_Nonlinearity/blob/main/Figures/Fig_4a.png)
![Figure 4b-g](https://github.com/lviens/2022_DAS_Nonlinearity/blob/main/Figures/Fig_4b-g.png)

