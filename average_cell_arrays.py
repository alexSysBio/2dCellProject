# -*- coding: utf-8 -*-
"""
Created on Sat Jun 28 11:28:38 2025

@author: Alexandros Papagiannakis, Stanford University, 2025
"""

import pandas as pd
import warnings
import numpy as np
warnings.filterwarnings('ignore')
import average_cell_mesh as mesh
import pickle


def get_projection_dataframe(mother_df, oned_df, cc_range):
    
    plot_df = mother_df[mother_df.cc_phase.between(*cc_range)]
    cc_df = oned_df[oned_df.cell_id.isin(plot_df.cell_id)]
    
    print(cc_df.cell_id.unique().shape[0], 'cells in cell cycle range:', cc_range)
    print('mean cell length:', plot_df.cell_length_px.mean()*0.066, 'um / 60th quant:', 
          plot_df.cell_length_px.quantile(0.6)*0.066, '/ 40th quant:', 
          plot_df.cell_length_px.quantile(0.4)*0.066)
    length_bins =  int((100/4.5)*plot_df.cell_length_px.mean()*0.066)
    
    print('mean cell division cycle phase:', plot_df.cc_phase.mean())
    print('length bins:', length_bins)
    res_df = cc_df[cc_df.width.between(-6,6)]
    res_df['length_bin'] = pd.cut(oned_df['scaled_length'], 
                                  bins=length_bins, labels=False)
    res_df['width_bin'] = pd.cut(oned_df['width'], bins=40, labels=False)
    
    res_df['abs_width'] = res_df.width.abs()
    
    return length_bins, res_df


def get_binned_projection(res_df, channel):
    """
    Channel should be the suffix (integer or string) and the column of the fluorescence statistic should be called 'fluor_pixels_(channel)'
    """
    
    if 'fluor_pixels_'+str(channel) in res_df.columns:
        print('generating the cell projection for channel fluor_pixels_'+str(channel))
    else:
        raise ValueError(f'Make sure the dataframe contains a fluor_pixels_{channel} column')
    
    grouped_df = res_df.groupby(['width_bin', 'length_bin'], as_index=False)['fluor_pixels_'+str(channel)].mean()
    data = grouped_df.pivot(index='width_bin', columns='length_bin', values='fluor_pixels_'+str(channel))
    
    return data


def generate_movie_arrays(oned_df, mother_df, cc_range, gr_range, channels):
    
    mother_df_gr = mother_df[mother_df.cc_gr.between(*gr_range)]
    
    array_dict = {}
    
    for ch in channels:
        array_dict[ch] = {}
        
    i = 0
    for cc in np.arange(*cc_range):

        length_bins, res_df = get_projection_dataframe(mother_df_gr, oned_df, (cc,cc+cc_range[2]))
        mesh_x, mesh_y = mesh.get_cell_mesh(res_df, length_bins)
        
        for ch in channels:
            data = get_binned_projection(res_df, ch)
            array_dict[ch][i] = data, (mesh_x, mesh_y)
        i+=1
    return array_dict
        


def save_cell_arrays(array_dict, save_path):
    
    with open(save_path, 'wb') as handle:
        pickle.dump(array_dict, handle)
        
        
        
def load_cell_arrays(load_path):
    
    with open(load_path, 'rb') as handle:
        array_dict = pickle.load(handle)
    
    return array_dict




