#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 18:37:43 2017

@author: tvieira
"""

#%% Read the list of images from a .txt file
def readListFromFile( filename ):
    """Return a list containing all lines from text file"""
    try:
        with open( filename ) as f:
            lines = f.readlines()
            return lines
    except:
        #e = sys.exc_info()[0]
        print( 'Error reading file ' + filename )

def rmCorruptedImgs (folder):
    """Remove corrupted images from directory 'folder'"""
    import os
    from PIL import Image
    # Get the list of files contained in the folder.
    try:
        flist = os.listdir(folder)
    except:
        print('Directory not found.')
    # Iterate over all files and remove those that cannot be opened.
    for i in range(0, len(flist)):
        fname = folder + flist[i]
        print(str(i) + 'th file ' + fname)
        try:
            img = Image.open(fname)
        except:
            print('Unable to open image file. Removing: ' + fname)
            os.remove(fname)