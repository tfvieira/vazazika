#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 17:43:01 2017

@author: tvieira
"""

#%% Download images from the Internet
from getImgsFromURLs import getImgsFromCategory
categories = ['aedes', 
              'culex', 
              'tire', 
              'bucket', 
              'trash']
category = categories[4]
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

#%%
import os
from utils_image import cvImgToJPEG
category = 'aedes'
folder = '../db/' + category + '/'
lst = os.listdir(folder)
for i in range(0, len(lst)):
    from PIL import Image
    name = folder + lst[i]
    img = Image.open(name)
    a, b = os.path.splitext(name)
    if b != '.jpg':
        rgb = img.convert('RGB')
        rgb.save(a + '.jpg')
        os.remove(name)
