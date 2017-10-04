#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 17:43:01 2017

@author: tvieira
"""

#%% Import packages
import os
from utils_url import getFileFromURL
from utils_file import readListFromFile

#%% Get Aedes images
category_sufix = 'aedes'
image_list = '../db/list_' + category_sufix + '.txt'
output_dir = '../db/' + category_sufix + '/'
outfile_prefix = category_sufix + '_'
lines = readListFromFile( image_list )

# Create folder if it doesn't exist
if os.path.exists(output_dir) == False:
    os.mkdir(output_dir)

# Download all images from specific URLs
for i in range(1, len(lines)):
    url_path = lines[i]
    url_path = url_path.replace('/r','').replace('\n', '')
    print('\n')
    print(str(i) + ' ' + url_path)
    file_name, file_extension = os.path.splitext(url_path)
    output_filename = output_dir + outfile_prefix + str(i) + file_extension
    getFileFromURL(url_path, output_filename)

#%% Get Culex images
category_sufix = 'culex'
image_list = '../db/list_' + category_sufix + '.txt'
output_dir = '../db/' + category_sufix + '/'
outfile_prefix = category_sufix + '_'
lines = readListFromFile( image_list )

# Create folder if it doesn't exist
if os.path.exists(output_dir) == False:
    os.mkdir(output_dir)

# Download all images from specific URLs
for i in range(1, len(lines)):
    url_path = lines[i]
    url_path = url_path.replace('/r','').replace('\n', '')
    print('\n')
    print(str(i) + ' ' + url_path)
    file_name, file_extension = os.path.splitext(url_path)
    output_filename = output_dir + outfile_prefix + str(i) + file_extension
    getFileFromURL(url_path, output_filename)

