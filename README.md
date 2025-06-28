# twod_project

This repository contains all functions used to generate average two-dimensional cell projections from birth to division.
This repository uses data from two dataframes to generate the average cell projections:
1. The first dataframe includes the cell division cycle trajectories. This is a Pandas dataframe that includes one column with the cell cycle information ('cc_phase'), a cell length column ('cell_length_px') and a column with the average cell cycle growth rate ('cc_gr'), calculated per cell cycle trajectory ('cell_trajectory_id'). This information is used to plot specific growth rate bins, for specific cell cycle ranges.
2. The second dataframe incldues the relative cell coordinates of all fluorescent pixels within the cell segmentation mask. It includes a column ('scaled_length') with the relative cell length from the old (-1) to the new (1) pole, with zero being the cell centroid, as well as the minimum distance of each pixel from the central line of the cell, oriented using the cross product ('width'). This dataframe is generated using the medial axis definition provided here: https://github.com/alexSysBio/Cell_medial_axis_definitions/blob/main/Bivariate_medial_axis_estimation.py. In this second dataframe, the fluorescent pixels are included in columsn marked with the predix 'fluor_pixels_' followed by the channel name (e.g., 'gfp', '2', '3' etc.). This code accommodates two fluorescent channels, but it can be modified to incliude more.


Examples of the two dataframe formats can be found in the BioImages archive: https://www.ebi.ac.uk/biostudies/bioimages/studies/S-BIAD1658 and the https://ftp.ebi.ac.uk/biostudies/fire/S-BIAD/658/S-BIAD1658/Files/CJW7323_microfluidics.zip folder. Dataframe 1 (or 'mother_df') corresponds to the dataframe titled 'CJW7323_microfluidics_normal_growth', whereas the Dataframe 2 (or 'oned_df') corresponds to the the dataframe titled 'CJW7323_one_dimensional_fluorescence_microfluidics'. 

Please cite:
Nonequilibrium polysome dynamics promote chromosome segregation and its coupling to cell growth in Escherichia coli

Alexandros Papagiannakis, Qiwei Yu, Sander K. Govers, Wei-Hsiang Lin,  Ned S. Wingreen, Christine Jacobs-Wagner

eLife2025;14:RP104276 DOI: https://doi.org/10.7554/eLife.104276.3
