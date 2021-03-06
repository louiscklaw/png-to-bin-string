#!/usr/bin/env python
# coding:utf-8

import os
import sys
import logging
import traceback
from pprint import pprint

HASHTAG='0x2400, 0x2400, 0x7C00, 0x2400, 0x4800, 0x7C00, 0x4800, 0x4800, 0x0000, 0x0000, 0x4800, 0x7C00, 0x4800, 0x4800, 0x0000, 0x0000'
CHAR_W='0x0000, 0x0000, 0x5400, 0x5400, 0x5400, 0x6C00, 0x2800, 0x2800, 0x0000, 0x0000'
TEST_PATTERN='0x1400,0x0000,0x4101,0x5554,0x4104,0x0001,0x1410,0x0001,0x0040,0x1554,0x0140,0x4000,0x0141,0x0000,0x0141,0x0000,0x0141,0x0000,0x0141,0x0000,0x0141,0x0000,0x0140,0x4000,0x0040,0x1554,0x0010,0x0001,0x0004,0x0001,0x0001,0x5554'

CELSIUS_16_PNG='0x1400,0x0000,0x4101,0x5554,0x4104,0x0001,0x1410,0x0001,0x0040,0x1554,0x0140,0x4000,0x0141,0x0000,0x0141,0x0000,0x0141,0x0000,0x0141,0x0000,0x0141,0x0000,0x0140,0x4000,0x0040,0x1554,0x0010,0x0001,0x0004,0x0001,0x0001,0x5554'

THERMOMETER_1_16_PNG="0x0005,0x5000,0x0010,0x0400,0x0010,0x0400,0x0010,0x0400,0x0010,0x0400,0x00,0x4000,0x0141,0x0000,0x0141,0x0000,0x0141,0x0000,0x0141,0x0000,0x0141,0x0000,0x0140,0x4000,0x00011,0x4400,0x0011,0x4400,0x0011,0x4400,0x0041,0x4100,0x0105,0x5040,0x0110,0x0440,0x0110,0x0440,0x0110,0x0440,0x0105,0x5040,0x0040,0x0100,0x0015,0x5400"

THERMOMETER_16_PNG="0x0005,0x5000,0x0010,0x0400,0x0011,0x4400,0x0011,0x4400,0x0011,0x4400,0x0010,0x4000,0x0141,0x0000,0x0141,0x0000,0x0141,0x0000,0x0141,0x0000,0x0141,0x0000,0x0140,0x4000,0x001,0x4400,0x0011,0x4400,0x0011,0x4400,0x0041,0x4100,0x0105,0x5040,0x0110,0x0440,0x0110,0x0440,0x0110,0x0440,0x0105,0x5040,0x0040,0x0100,0x0015,0x5400"

teststring=THERMOMETER_16_PNG

HEX2BINMAP=['0000', '0001', '0010', '0011',
                 '0100', '0101', '0110', '0111',
                 '1000', '1001', '1010', '1011',
                 '1100', '1101', '1110', '1111']

def getHex2BinMap(int):
    return HEX2BINMAP[int]

def printHexPattern(teststring):
    a=teststring.replace(' ','').split(',')
    a_double = [[a[i], a[i+1]] for i in range(0,len(a),2)]
    pprint(a_double)
    for a in a_double:
        for b in a:
            c = b[2:]
            for d in c:
                cache=getHex2BinMap(int(d,16))
                cache=cache.replace('0',' ').replace('1','X')
                print(cache,end='')
        print()

def main():
    printHexPattern(teststring)

if __name__ == '__main__':
    main()
