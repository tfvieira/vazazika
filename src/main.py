#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 17:43:01 2017

@author: tvieira
"""

#%% Download images from the Internet
from getImgsFromURLs import getImgsFromCategory
#category = 'aedes'
#category = 'culex'
#category = 'tire'
category = 'bucket'
getImgsFromCategory(category)

#%%
from utils_file import rmCorruptedImgs
rmCorruptedImgs('../db/' + category + '/')

#%%
import os
from utils_image import cvImgToJPEG
folder = '../db/' + category + '/'
lst = os.listdir(folder)
for i in range(0, len(lst)):
    imgfilename = folder + lst[0]
    cvImgToJPEG(imgfilename)