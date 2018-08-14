"""
Created on Tue Aug 14 17:58:44 2018
@author: chwu
"""
# read binary file to integer array
# c is how many byte you want to skip

def read_data(filename,c):
    with open(filename, 'rb') as infile:
        lines = []
        if c>0:
            infile.seek(c)
        byte = infile.read(1)
        lines.append(byte)
        while byte:
        # Do stuff with byte.
            byte = infile.read(1)
            lines.append(int.from_bytes(byte,'little'))
    infile.close
    return lines
