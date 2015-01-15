#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Turn On Room Light
"""

import datetime
import argparse
from iremocon import IRemocon

# Parse Argument
parser = argparse.ArgumentParser(description='Turn On RoomLight.')
parser.add_argument('datetime', type=str,
                    help='date & time when turn on room light')
args = parser.parse_args()

remocon = IRemocon('iremocon.yaml')

# remocon code to turn on room light
turn_on = remocon.code['6畳']['全灯']

# make command_string
alarm_time = datetime.datetime.strptime(args.datetime,
                                        '%Y/%m/%d %H:%M:%S')
t = alarm_time - datetime.datetime(1970, 1, 1, 9, 0, 0)
command_string = \
    '*tm;{REMOCON_CODE};{seconds:.0f};0\r\n'.format(
        REMOCON_CODE=turn_on, seconds=t.total_seconds())

# send command and display result
answer = remocon.SendCommand(command_string.encode('ascii'))
print('Recieved', repr(answer))
