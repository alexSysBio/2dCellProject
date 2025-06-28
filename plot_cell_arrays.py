# -*- coding: utf-8 -*-
"""
Created on Sat Jun 28 11:32:40 2025

@author: Alexandros Papagiannakis, Stanford University, 2025
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec
import warnings
warnings.filterwarnings('ignore')
from PIL import Image


def resize_data_array(array):
    
    pil_image = Image.fromarray(array)
    new_size = (array.shape[1]*2, array.shape[0]*2)    
    
    return np.array(pil_image.resize(new_size, Image.NEAREST))



def plot_resized_array(resized_array, cell_mesh, edge, axis, cmap, v_range, meshcolor):
    
    resized_array = np.nan_to_num(resized_array, nan=0.0)
    
    axis.imshow(resized_array, vmin=v_range[0], vmax=v_range[1], cmap=cmap)
    axis.plot(cell_mesh[0]*2+edge+1, cell_mesh[1]*2+1, linewidth=6, color= meshcolor)
    axis.set_xticks([])
    axis.set_yticks([])
    


def center_data(data, max_shape):
    
    edge = int((max_shape[1]-np.array(data).shape[1])/2)
    
    added_array = np.empty((max_shape[0], edge))
    added_array[:] = np.NaN
#     added_array[:] = 0
    added_array
    new_array = np.concatenate((added_array, data, added_array), axis=1)
    
    return new_array, edge
    
    
    
def plot_cell_projections(array_dict, v_ranges, cmaps, meshcolor, save_path, show=True):
    
    dict_keys = list(array_dict.keys())
    
    max_key = max(array_dict[dict_keys[0]].keys())
    max_shape = array_dict[dict_keys[0]][max_key][0].shape
    print(f'max shape: {max_shape}')

    
    plot_dict = {}

    for i in array_dict[dict_keys[0]]:
        
        chone_array = array_dict[dict_keys[0]][i][0]
        chtwo_array = array_dict[dict_keys[1]][i][0]
        cell_mesh = array_dict[dict_keys[0]][i][1]
        
        chone_array = resize_data_array(np.array(chone_array))
        chtwo_array = resize_data_array(np.array(chtwo_array))
        
        chone_array, edge = center_data(chone_array, (max_shape[0]*2, max_shape[1]*2))
        chtwo_array, edge = center_data(chtwo_array, (max_shape[0]*2, max_shape[1]*2))

    
        plt.figure(figsize=((max_shape[1]/5+max_shape[1]/5), (max_shape[0]/5+max_shape[0]/5)))
        gs = GridSpec(2, 1, width_ratios=[max_shape[1]], height_ratios=[max_shape[0],max_shape[0]])
        gss = [gs[0,0], gs[1,0]]
        
        
        plot_resized_array(chone_array, cell_mesh, edge, plt.subplot(gss[0]), cmaps[0], v_ranges[0], meshcolor)
        plot_resized_array(chtwo_array, cell_mesh, edge, plt.subplot(gss[1]), cmaps[1], v_ranges[1], meshcolor)

        plt.savefig(save_path+'/'+str(i)+'.jpeg')
        if show == True:
            plt.show()
        else:
            plt.close()
        
        plot_dict[i] = (chone_array, chtwo_array, edge)
    
    
    return plot_dict
                   
    