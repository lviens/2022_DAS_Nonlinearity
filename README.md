# Python codes to detect soil non-linear behavior during earthquakes recorded by Distributed Acoustic Sensing (DAS) 

The codes are for the following manuscript:
- Viens L., L. F. Bonilla, Z. J. Spica, K. Nishida, T. Yamada, S. Shinohara, Nonlinear earthquake response of marine sediments with distributed acoustic sensing ([Preprint link](https://doi.org/10.1002/essoar.10511693.1))

## Description:
* The **Codes** folder contains:

  - **Reproduce_Fig_1cde.py** to reproduce Figure 1cde of the paper (plot strain waveforms for Mv 2.5 earthquake, strain-rate data at station 5000, and compute ACFs)
  - **Reproduce_Fig_2.py** to reproduce Figure 2 (ACFs at two channels for two frequency bands)
  - **Reproduce_Fig_3.py** to reproduce Figure 3 of the paper
  - **Reproduce_Fig_4.py** to reproduce the Figure 4 of the paper.

* The **Data** folder contains:
* - The data to reproduce Figure 1cde are too big for github and are available [here](https://drive.google.com/file/d/13Lk2pSpx4m9JTnw6Am0lyL1xRaNfHypZ/view?usp=sharing). Note that they need to be moved to the **Data** folder before running the **Reproduce_Fig_1cde.py** code
  - The data to reproduce Figures 2-4.
  

* The **Figures** folder contains 6 figures that can be plotted with the 4 codes. 


## Codes and their outputs:

* The **Reproduce_Fig_1cde.py** code reads the strain data of the MV 2.5 earthquake (Warning: the data were downsampled to 50 Hz for this example to reduce the size of the file. Fig. 1c is slightly different from that shown in the manucript as the bandpass filter applied to the data is 2-25 Hz, whereas it is 2-30 Hz in the manuscript). The strain-rate data at channel 5000 (Figure 1d) have a 500 Hz sampling rate and are used to compute the frequency dependent ACFs shown in Figue 1e. This code contains the function used to compute the ACFs using the phase correlation method in the frequency domain.
<p align="center">
<img src="https://github.com/lviens/2022_DAS_Nonlinearity/blob/main/Figures/Fig_1cde.png" width=75%/>
</p>
<br/>
<br/>

* The **Reproduce_Fig_2.py** code shows theACFs computed from the 103 earthquakes bandpass filtered between 10 and 20 Hz at channels (a) 5000 and (b) 7000. (c--d) Same as (a--b) for the data bandpass filtered between 15 and 30 Hz.  In (a--d), the ACFs are sorted by increasing dynamic peak strain values, which are computed after bandpass filtering the strain waveforms in their respective frequency bands. (e--f) Dynamic peak strains after bandpass filtering the earthquake waveforms between 10-20 Hz and 15-30 Hz at channels 5000 and 7000, respectively.
<p align="center">
<img src="https://github.com/lviens/2022_DAS_Nonlinearity/blob/main/Figures/Fig_2.png" width=75%/>
</p>
<br/>
<br/>

* The **Reproduce_Fig_3.py** code shows (a) the dv/v measurements between channels 5000 and 5010 for the 19 frequency bands and the 103 earthquakes. Dynamic peak strains are computed for each event and each station after bandpass filtering the strain data. The central frequency corresponds to the central frequency of the bandpass filter (e.g., 15 Hz for the 10-20 Hz bandpass filter). (b) Same as (a) between channels 7000 and 7010. (c) dv/v measurements from the ACFs computed from the 103 earthquakes bandpass filtered between 5 to 10 Hz between channels 500 and 9000 as a function of the dynamic peak strain. (d) Same as (c) for the 10-20 Hz frequency band. The dv/v color-scale shown in (b) is the same for all panels.
<p align="center">
<img src="https://github.com/lviens/2022_DAS_Nonlinearity/blob/main/Figures/Fig_3ab.png" width=75%/>
</p>
<p align="center">
<img src="https://github.com/lviens/2022_DAS_Nonlinearity/blob/main/Figures/Fig_3cd.png" width=75%/>
</p>
<br/>
<br/>

* The **Reproduce_Fig_4.py** code shows (a) the dv/v measurements computed between a reference ACF, which represents the soil linear response, and average ACF obtained from the earthquakes that generated the five largest peak strains, which captures the nonlinear behavior of sediments, at each channel and each frequency band. (b) Relative velocity changes as a functions of the filtered dynamic peak strain in the 2-4 Hz frequency bands. (c--d) Same as (b) for the 10-20 and 20-40 Hz frequency bands. (e) Relative velocity changes as a function of the average S-wave velocity within the first 30 m of the ground (VS30) for the 2-4 Hz frequency bands. (f--g) Same as (g) for the 10-20 and 20-40 Hz frequency bands. In (b--g), the color-bar corresponds to the channel number.
<p align="center">
<img src="https://github.com/lviens/2022_DAS_Nonlinearity/blob/main/Figures/Fig_4a.png" width=75%/>
</p>
<p align="center">
<img src="https://github.com/lviens/2022_DAS_Nonlinearity/blob/main/Figures/Fig_4b-g.png" width=75%/>
</p>
