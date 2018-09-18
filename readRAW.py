# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 17:51:04 2018

@author: KYLAB WY Lee
"""
#%% Get the files pathway

import tkinter as tk  
from tkinter import filedialog  
##import numpy as np
import math
  
root = tk.Tk()              
root.withdraw()             # we don't want a full GUI, so keep the root window from appearing
 
default_dir = r"D:\Python"  # Setting default Folder

fname = filedialog.askopenfilename(title = u'選擇文件', 
                                           initialdir = default_dir,
                                           filetypes = [("allfiles", "*"),("raw files", "*.raw")]
                                           )


#%% Open RAW file in python

Raw_Data = open(fname, "rb").read()

RAW = []
for s in Raw_Data:
    RAW.append(s)

header = RAW[0:512]             #RAW files header

header2 = []                    #RAW files header to String
for s in header:
    header2.append(chr(s))

#%% Acquisition sampling rate ratio
    
splr = header2[39:54]   
splr2 = ''.join(splr)
splr2 = float(splr2)        #Sampling Rate

start = 55
SRn = []
for i in range(header[36]):     #Acquisition sampling rate ratio SRn
    SRtemp = header2[start+i*15+i:start+(i+1)*15+i]
    splrtemp = ''.join(SRtemp)
    splr_float = float(splrtemp)
    SRn.append(splr2/splr_float)

maxi = int(max(SRn))

#%%  Find the Channel 

channel=[]
for i in range(maxi) :
    for j in range(header[36]):
        #matrix[i][j] = i
        if i % SRn[j] == 0:
            channel.append(j)

#%% Data segmentation

Data = []
cont = []
for i in range(header[36]):
    Data.append([])
    cont.append(1)
           
Raw_Data = RAW[512:math.floor((len(RAW)-512)/len(channel))*len(channel)+512]
for i in range(0, len(Raw_Data), len(channel)*2):
    for j in range(len(channel)):
        Data[channel[j]].append(Raw_Data[i + 2*j+1]*256+Raw_Data[i + 2*j])
    



