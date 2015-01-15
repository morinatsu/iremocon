#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Turn On Room Light
"""

import datetime
import argparse
from iremocon import IRemocon

parser = argparse.ArgumentParser(description='Turn On RoomLight.')
parser.add_argument('datetime', type=str, help='time when turn on room light')
args = parser.parse_args()

alarm_time = datetime.datetime.strptime(args.datetime, '%Y/%m/%d %H:%M:%S')
t = alarm_time - datetime.datetime(1970,1,1,9,0,0)
command_string = '*tm;350;{seconds:.0f};0\r\n'.format(seconds=t.total_seconds())
remocon = IRemocon('iremocon.yaml')
answer = remocon.SendCommand(command_string.encode('ascii'))
print('Recieved', repr(answer))
