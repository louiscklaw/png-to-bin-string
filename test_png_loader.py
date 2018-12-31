#!/usr/bin/env python
# coding:utf-8

import os
import sys
import logging
import traceback
from pprint import pprint
import subprocess


input_dir='./pngs/weather/16'

def testPNGLoader(input_dir):
    filenames = os.listdir(input_dir)
    filenames_with_path = []
    for filename in filenames:
        filenames_with_path.append(os.path.join(input_dir, filename))

    return filenames_with_path

if __name__ == '__main__':
    filenames_with_path = testPNGLoader(input_dir)
    for filename in filenames_with_path:
        command = 'python3 ./test_png.py %s' % filename
        command_result = subprocess.check_output(command.split(' '))
        print(command_result.decode('utf-8'))
