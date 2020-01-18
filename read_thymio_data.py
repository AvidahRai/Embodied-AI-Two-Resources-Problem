#!/usr/bin/env python3
# Convert binary format data files from Thymio to ASCII CSV
#
# Input file assumed to consist of 16-bit binary signed numbers
#
# by Matthew Lewis
# University of Hertfordshire
# November 2018

import sys

# Columns to output (edit this if more than one variable being recorded)
DATA_COLUMNS = 1


# Function to read 16 bits from open file
def read16bits(file):
    dat = file.read(2)
    val = dat[0] + 256*dat[1]
    if val >= 0x8000: # negative number
        val = val - 0x10000
    return val


#
# Code entry point
#

if len(sys.argv)<2:
    raise Exception("Missing argument: input filename required")

# Open file and use it
with open(sys.argv[1], 'rb') as file:
    col = 0 # counter for columns - so newlines can be added
    while True:
        try:
            val = read16bits(file)
        except IndexError:
            break # End of file
        print(val, end='')
        col += 1
        if col==DATA_COLUMNS: # end of line
            col = 0
            print() # newline
        else:
            print(', ', end='')
