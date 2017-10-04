# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 08:46:56 2017

@author: tvieira
"""

def cvImgToJPEG (input_img_fname, output_img_fname):
    from PIL import Image
    img = Image.open(input_img_fname)
    rgb = img.convert('RGB')
    rgb.save(output_img_fname)