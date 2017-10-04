# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 08:24:18 2017

@author: tvieira
"""

#%% Import libraries
import urllib

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

#%% Get file from url
def downloadFileFromURL (url, file_name):
    url_obj = urllib.URLopener()
    try:
        url_obj.retrieve(url, file_name)
    except:
        #e = sys.exc_info()[0]
        print( 'Error reading url ' + url )

#%% Get images for specific category
# Categories can be:
# aedes
# culex
# tire
# bucket
# trash
def getImgsFromCategory (category):
    import os
    from utils_url import getFileFromURL
    image_list = '../db/list_' + category + '.txt'
    output_dir = '../db/' + category + '/'
    outfile_prefix = category + '_'
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