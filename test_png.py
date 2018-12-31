# /usr/bin/env python

import os,sys
from pprint import pprint
import urllib
import png

output_buffer = ''
output_buffers = []

hex_buffers=[]
out_hexs = []
out_hex_string =''


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

HEX2BINMAP_list=['0000', '0001', '0010', '0011',
                 '0100', '0101', '0110', '0111',
                 '1000', '1001', '1010', '1011',
                 '1100', '1101', '1110', '1111']

input_file = sys.argv[1]
input_filename = os.path.basename(input_file)
output_var_name = input_filename.replace('.','_').replace('-','_').upper()[4:]

# r=png.Reader(file=urllib.urlopen('http://www.schaik.com/pngsuite/basn0g02.png'))
r=png.Reader(filename=sys.argv[1])
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


def getHex2BinMap(int):
    return HEX2BINMAP_list[int]

def printHexPattern(teststring):
    print('\nprinthexpattern\n')
    a=teststring.replace(' ','').split(',')
    a_double = [[a[i], a[i+1]] for i in range(0,len(a),2)]
    for a in a_double:
        for b in a:
            c = b[2:]
            for d in c:
                cache=getHex2BinMap(int(d,16))
                cache=cache.replace('0',' ').replace('1','X')
                print(cache,end='')
        print()

def main():
    for png_raw_bytes in png_raw_list:
        output_buffer=''
        for png_raw_byte in png_raw_bytes:
            if png_raw_byte > 128:
                output_buffer = output_buffer+'1'
            else:
                output_buffer = output_buffer+'0'

        output_buffers.append(output_buffer)

    print('parsed 0 1 pattern')
    for output_buffer in output_buffers:
        print(output_buffer)
        hex_buffers.append(makeBCD(output_buffer))

    print()

    for hex_buffer in hex_buffers:
        out_hexs.append('0x%s,0x%s' % (hex_buffer[0:4],hex_buffer[4:]))

    output_string = ','.join(out_hexs)

    # generated pattern
    print('\n generated pattern\n')
    printHexPattern(output_string)

    #
    print('\nhexed code:')
    print('%s="%s"' % (output_var_name, output_string))


if __name__ =='__main__':
    main()
