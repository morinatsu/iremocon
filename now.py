#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Get Time of i-remocon
"""

import datetime
from iremocon import IRemocon

remocon = IRemocon('remocon.yaml')
answer = remocon.SendCommand(b'*tg\r\n').decode('ascii')
if answer.startswith('tg;ok;'):
    seconds = int(answer.rstrip('\r\n').rpartition(';')[2])
    now = datetime.datetime(1970, 1, 1, 9, 0, 0) + datetime.timedelta(seconds=seconds)
    print('Time of i-remocon: ', now)
else:
    print('error')

