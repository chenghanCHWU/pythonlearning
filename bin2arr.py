"""
Created on Tue Aug 14 17:58:44 2018
@author: chwu
"""

import matplotlib.pyplot as plt


def read_data(filename):
    with open(filename, 'rb') as infile:
        lines = []
        infile.seek(512)
        byte = infile.read(1)
        lines.append(byte)
        while byte:
        # Do stuff with byte.
            byte = infile.read(1)
            lines.append(int.from_bytes(byte,'little'))
    infile.close
    return lines

plt.plot(read_data('testfile.RAW'))
plt.show()