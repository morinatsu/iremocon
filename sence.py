#!/usr/bin/env python
#! -*- coding: utf-8 -*-
"""
Display Info of Sencers in i-remocon
"""

from iremocon import IRemocon


remocon = IRemocon('iremocon.yaml')

# send command
answer = remocon.SendCommand(b'*se\r\n').decode('ascii')
print('Recieved', answer)

# parse answer
if answer.startswith('se;ok;'):
    illuminance = float(answer.rstrip('\r\n').split(';')[2])
    humidity = float(answer.rstrip('\r\n').split(';')[3])
    temperature = float(answer.rstrip('\r\n').split(';')[4])
    print('illuminance: {illum:.0f}lx'.format(illum=illuminance))
    print('humidity: {humidity:.0f}%'.format(humidity=humidity))
    print('temperature: {temper:.0f}°C'.format(temper=temperature))
else:
    print('Error')
