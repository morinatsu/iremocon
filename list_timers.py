#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
List Registerd Timers
"""

import datetime
from iremocon import IRemocon

remocon = IRemocon('remocon.yaml')
answer = remocon.SendCommand(b'*tl\r\n').decode('ascii')
print('Recieved: ', repr(answer))
