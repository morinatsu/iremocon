#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Send Free Command to iRemocon
"""

import sys
import argparse
from iremocon import IRemocon

# Parse Argument
parser = argparse.ArgumentParser(description='Send Free Command to iRemocon.')
parser.add_argument('command', type=str, help='comand_string to send')
args = parser.parse_args()

remocon = IRemocon('iremocon.yaml')

# make command_string
command_string = '{command_string}\r\n'.format(command_string=args.command)

# send command and display result
answer = remocon.SendCommand(command_string.encode('ascii'))
print('Recieved', repr(answer))
