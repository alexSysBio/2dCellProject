# -*- coding: utf-8 -*-
"""
Created on Sat Jun 28 11:24:47 2025

@author: Alexandros Papagiannakis, Stanford University, 2025
"""

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')




def smooth_cell_mesh(mesh_x, mesh_y, smoothing=4):
    
    mesh_df = pd.DataFrame()
    mesh_df['x'] = mesh_x
    mesh_df['y'] = mesh_y
    mesh_df = pd.concat([mesh_df, mesh_df.head(smoothing)])
    mesh_df['smooth_x'] = mesh_df.x.rolling(smoothing,center=True).mean()
    mesh_df['smooth_y'] = mesh_df.y.rolling(smoothing,center=True).mean()
    
    return mesh_df.smooth_x, mesh_df.smooth_y


def get_cell_mesh(res_df, length_bins):
    
    width_vec = res_df.sort_values('length_bin').groupby(['length_bin']).width.quantile(0.9975).tolist()
    
    mesh_x = []
    mesh_y = []
    for ln in range(length_bins):
        mesh_x.append(ln)
        mesh_y.append((width_vec[ln]/6)*20)
    
    mesh_x = mesh_x[1:-1]
    mesh_y = mesh_y[1:-1]
    
    mesh_x = mesh_x + mesh_x[::-1]+[mesh_x[0]]
    mesh_y = mesh_y + list(20-np.array(mesh_y[::-1]))+[mesh_y[0]]
    
    mesh_x, mesh_y = smooth_cell_mesh(mesh_x, mesh_y)
    
    return mesh_x, mesh_y


