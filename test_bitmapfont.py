#!/usr/bin/env python
# coding:utf-8

import os
import sys
import logging
import traceback
from pprint import pprint

HASHTAG='0x2400, 0x2400, 0x7C00, 0x2400, 0x4800, 0x7C00, 0x4800, 0x4800, 0x0000, 0x0000, 0x4800, 0x7C00, 0x4800, 0x4800, 0x0000, 0x0000'
CHAR_W='0x0000, 0x0000, 0x5400, 0x5400, 0x5400, 0x6C00, 0x2800, 0x2800, 0x0000, 0x0000'
TEST_PATTERN='0x0000,0x0500,0x0000,0x1040,0x0001,0x4040,0x0554,0x0040,0x1540,0x0040,0x5540,0x0050,0x5540,0x0044,0x5540,0x0044,0x1540,0x0050,0x0554,0x0040,0x0411,0x4040,0x0410,0x1040,0x0410,0x0500,0x0410,0x0000,0x0140,0x0000'

teststring=TEST_PATTERN

HEX2BINMAP=['0000', '0001', '0010', '0011',
                 '0100', '0101', '0110', '0111',
                 '1000', '1001', '1010', '1011',
                 '1100', '1101', '1110', '1111']

def getHex2BinMap(int):
    return HEX2BINMAP[int]

def main():

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
if __name__ == '__main__':
    main()
