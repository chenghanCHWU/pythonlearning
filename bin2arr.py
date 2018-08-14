# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 17:58:44 2018

@author: kylab
"""

def read_data(filename):
    with open(filename, 'rb') as infile:
        lines = []
        byte = infile.read(1)
        lines.append(byte)
        while byte:
        # Do stuff with byte.
            byte = infile.read(1)
            lines.append(byte)
    infile.close
    return lines
