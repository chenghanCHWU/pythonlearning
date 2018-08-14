# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 19:42:53 2018

@author: kylab
"""

import matplotlib.pyplot as plt
import bin2arr

data=bin2arr.read_data('testfile.RAW',512)
plt.plot(data)
plt.show
