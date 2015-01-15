#!/env/python
#! -*- coding:utf-8 -*-
"""
Display Info of Sencers in i-remocon
"""

from iremocon import IRemocon


remocon = IRemocon('iremocon.yaml')
answer = remocon.SendCommand(b'*se\r\n').decode('ascii')
print('Recieved', answer)

