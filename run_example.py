# -*- coding: utf-8 -*-
"""
Created on Sat Jun 28 11:40:07 2025

@author: Alexandros Papagiannakis, Stanford University, 2025
"""

import dataframe_load as dload
import average_cell_arrays as avcel
import plot_cell_arrays as arplt
import cmasher as cmr


bio_path = r"D:\Shares\Data_01\Alex Papagiannakis\BioStudies_Data\eLife_Papagiannakis_etal\CJW7323_microfluidics"

mother_df = dload.load_cell_cycle_dataframe(bio_path+'/CJW7323_microfluidics_normal_growth')
oned_df = dload.load_pixel_projections(bio_path+'/CJW7323_one_dimensional_fluorescence_microfluidics')


cc_range = (0,1,0.025)
gr_range = (0.65,2)
v_ranges = [(270,580),(100,275)]
meshcolor='white'
cmaps = (cmr.ember,cmr.cosmic)

array_dict = avcel.generate_movie_arrays(oned_df, mother_df, cc_range, gr_range, [2,3])
avcel.save_cell_arrays(array_dict, r"D:\Shares\Data_01\Alex Papagiannakis\Python\Analysis_functions\2D_cell_projections"+'/2D_cell_arrays_dict')
array_dict = avcel.load_cell_arrays(r"D:\Shares\Data_01\Alex Papagiannakis\Python\Analysis_functions\2D_cell_projections"+'/2D_cell_arrays_dict')

plot_dict = arplt.plot_cell_projections(array_dict, v_ranges, cmaps, meshcolor, 
                                        r"D:\Shares\Data_01\Alex Papagiannakis\Python\Analysis_functions\2D_cell_projections\cell_projections")