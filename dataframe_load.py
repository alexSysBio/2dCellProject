# -*- coding: utf-8 -*-
"""
Created on Sat Jun 28 11:47:57 2025

@author: Alexandros Papagiannakis, Stanford University, 2025
"""

import pandas as pd


def load_cell_cycle_dataframe(save_path):
    if 'CJW7323_microfluidics_normal_growth' not in save_path:
        print('The loaded dataframe should include the cell cycle trajectories, with the average cell cycle growth rate, and a cell length column.')
        print('..for example see the CJW7323_microfluidics_normal_growth dataframe provided at https://ftp.ebi.ac.uk/biostudies/fire/S-BIAD/658/S-BIAD1658/Files/CJW7323_microfluidics.zip')
    return pd.read_pickle(save_path, compression='zip')


def load_pixel_projections(save_path):
    if 'CJW7323_one_dimensional_fluorescence_microfluidics' not in save_path:
        print('The loaded dataframe should include the relative cell coordinates of all fluorescent pixels in each channel (ch2, ch3, etc) as well as a cell ID column.')
        print('..for example see the CJW7323_one_dimensional_fluorescence_microfluidics dataframe provided at https://ftp.ebi.ac.uk/biostudies/fire/S-BIAD/658/S-BIAD1658/Files/CJW7323_microfluidics.zip')
    return pd.read_pickle(save_path, compression='zip')
