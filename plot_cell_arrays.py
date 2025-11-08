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
from scipy import ndimage


def resize_data_array(array, rescale_factor):
    pil_image = Image.fromarray(array)
    new_size = (array.shape[1]*rescale_factor, array.shape[0]*rescale_factor)    
    return np.array(pil_image.resize(new_size, Image.NEAREST))


def get_resized_mesh(cell_mesh, edge, rescale_factor):
    rescaled_mesh_zero = cell_mesh[0]*rescale_factor + edge + rescale_factor/2
    rescaled_mesh_one = cell_mesh[1]*rescale_factor + rescale_factor/2
    return rescaled_mesh_zero, rescaled_mesh_one
        

def remove_nans(array):
    return np.nan_to_num(array, nan=0.0)


def plot_resized_array(resized_array, rescaled_cell_mesh, axis, cmap, v_range, meshcolor, rescale_factor, show_mesh):
    # resized_array = np.nan_to_num(resized_array, nan=0.0)
    axis.imshow(resized_array, vmin=v_range[0], vmax=v_range[1], cmap=cmap)
    # axis.plot(cell_mesh[0]*2+edge+1, cell_mesh[1]*2+1, linewidth=6, color= meshcolor)
    if show_mesh:
        axis.plot(rescaled_cell_mesh[0], rescaled_cell_mesh[1], linewidth=6*rescale_factor/2, color= meshcolor)
    axis.set_xticks([])
    axis.set_yticks([])
    axis.spines['right'].set_visible(False)
    axis.spines['left'].set_visible(False)
    axis.spines['top'].set_visible(False)
    axis.spines['bottom'].set_visible(False)
    


def center_data(data, max_shape):
    
    edge = int((max_shape[1]-np.array(data).shape[1])/2)
    
    added_array = np.empty((max_shape[0], edge))
    added_array[:] = np.nan
#     added_array[:] = 0
    added_array
    new_array = np.concatenate((added_array, data, added_array), axis=1)
    
    return new_array, edge
    


def smooth_array(array, gaussian_sigma):
    return ndimage.gaussian_filter(array, gaussian_sigma)
    

def rescale_array(array, rescale_factor):
    return array.repeat(rescale_factor, axis=0).repeat(rescale_factor, axis=1)

    
def plot_cell_projections(array_dict, v_ranges, cmaps, meshcolor, rescale_factor, gaussian_sigma, show_mesh, image_format, save_path, show=True):
    
    dict_keys = list(array_dict.keys())
    
    max_key = max(array_dict[dict_keys[0]].keys())
    max_shape = array_dict[dict_keys[0]][max_key][0].shape
    max_shape = np.array(max_shape)*rescale_factor

    print(f'max shape: {max_shape}')

    
    plot_dict = {}

    for i in array_dict[dict_keys[0]]:
        
        chone_array = array_dict[dict_keys[0]][i][0]
        chtwo_array = array_dict[dict_keys[1]][i][0]
        cell_mesh = array_dict[dict_keys[0]][i][1]
        
        chone_array = resize_data_array(np.array(chone_array), rescale_factor)
        chtwo_array = resize_data_array(np.array(chtwo_array), rescale_factor)
        chone_array, edge = center_data(chone_array, (max_shape[0], max_shape[1]))
        chtwo_array, edge = center_data(chtwo_array, (max_shape[0], max_shape[1]))
        
        chone_array = remove_nans(chone_array)
        chtwo_array = remove_nans(chtwo_array)
        
        if gaussian_sigma > 0:
            chone_array = smooth_array(chone_array, gaussian_sigma)
            chtwo_array = smooth_array(chtwo_array, gaussian_sigma)
            
        cell_mesh = get_resized_mesh(cell_mesh, edge, rescale_factor)

        plt.figure(figsize=(max_shape[1]/5, max_shape[0]/5))
        plt.style.use('dark_background')
        gs = GridSpec(2, 1, 
                      width_ratios=[max_shape[1]], height_ratios=[max_shape[0],max_shape[0]],
                      wspace=0.0, hspace=0.3)
        gss = [gs[0,0], gs[1,0]]
        
        
        plot_resized_array(chone_array, cell_mesh, plt.subplot(gss[0], facecolor='black'), cmaps[0], v_ranges[0], meshcolor, rescale_factor, show_mesh)
        plot_resized_array(chtwo_array, cell_mesh, plt.subplot(gss[1], facecolor='black'), cmaps[1], v_ranges[1], meshcolor, rescale_factor, show_mesh)
        
        plt.savefig(save_path+'/'+str(i)+image_format)
        if show == True:
            plt.show()
        else:
            plt.close()
        
        plot_dict[i] = (chone_array, chtwo_array, edge)
    
    
    return plot_dict
                   
    