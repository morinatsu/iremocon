#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Cancel Timer of iRemocon
"""

import sys
import argparse
from iremocon import IRemocon

# Parse Argument
parser = argparse.ArgumentParser(description='Cancel Timer of iRemocon.')
parser.add_argument('number', type=str, help='timer number')
args = parser.parse_args()

remocon = IRemocon('iremocon.yaml')

# make command_string
command_string = '*td;{timer_number}\r\n'.format(timer_number=args.number)

# send command and display result
answer = remocon.SendCommand(command_string.encode('ascii'))
print('Recieved', repr(answer))
