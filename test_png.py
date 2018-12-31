# /usr/bin/env python

import os,sys
from pprint import pprint
import urllib
import png

output_buffer = ''
output_buffers = []

HEX2BINMAP={
    '0000':'0',
    '0001':'1',
    '0010':'2',
    '0011':'3',
    '0100':'4',
    '0101':'5',
    '0110':'6',
    '0111':'7',
    '1000':'8',
    '1001':'9',
    '1010':'A',
    '1011':'B',
    '1100':'C',
    '1101':'D',
    '1110':'E',
    '1111':'F'
}

# r=png.Reader(file=urllib.urlopen('http://www.schaik.com/pngsuite/basn0g02.png'))
r=png.Reader(filename='./notice.png')
test_list = r.read()

png_raw_list = list(test_list[2])

def rightAppendZero(input_string):
    append_times = len(input_string) % 4
    for i in range(0,append_times):
        input_string = input_string+'0'

    return input_string

def binStringToHex(bin_string):
    int_temp = HEX2BINMAP[bin_string]
    return int_temp

def makeBCD(bin_string):
    output_hex = ''
    bin_string=rightAppendZero(bin_string)

    for i in range(0,len(bin_string),3+1):
        active_4_bit = bin_string[i:i+4]
        output_hex=output_hex+binStringToHex(active_4_bit)
    return output_hex

for png_raw_bytes in png_raw_list:
    output_buffer=''
    for png_raw_byte in png_raw_bytes:
        if png_raw_byte > 128:
            output_buffer = output_buffer+'1'
        else:
            output_buffer = output_buffer+'0'

    output_buffers.append(output_buffer)

# print('\n'.join(output_buffers))

hex_buffers=[]
for output_buffer in output_buffers:
    hex_buffers.append(makeBCD(output_buffer))

for hex_buffer in hex_buffers:
    print('0x%s,0x%s' % (hex_buffer[0:4],hex_buffer[4:]))
