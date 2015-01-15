#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
List Registerd Timers
"""

import datetime
from iremocon import IRemocon

def reparse_time(seconds):
    date_time = datetime.datetime(1970, 1, 1, 9, 0, 0) + \
        datetime.timedelta(seconds=int(seconds))
    return date_time.strftime('%Y/%m/%d %H:%M:%S')

remocon = IRemocon('iremocon.yaml')

# send command
answer = remocon.SendCommand(b'*tl\r\n').decode('ascii')
print('Recieved: ', repr(answer))

# parse answer
if answer.startswith('tl;ok;'):
    head = answer.rstrip('\r\n').split(';')[0:2]
    body = answer.rstrip('\r\n').split(';')[3:]
    while len(body) > 0:
        seq = body.pop(0)
        code = remocon.inverted_code[body.pop(0)]
        time = reparse_time(body.pop(0))
        repeat = body.pop(0)
        print('Seq: {seq}, Code: {code}, Time: {time}'.format(seq=seq,
            code=code, time=time))
else:
    print('error')
