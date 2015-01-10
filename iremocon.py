# -*- coding: utf-8 -*-
"""
iremocon.py: Send and Recieve Messages with i-remocon
"""
import socket
import configparser

class IRemocon(object):
    """
    Command Sender class
    """

    def __init__(self, config_file):
        """
        Make a New Instance
        """
        config = configparser.ConfigParser()
        config.read(config_file)
        self._host = config.get('remocon', 'HOST')
        self._port = int(config.get('remocon', 'PORT'))

    def SendCommand(self, message):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self._host, self._port))
        s.sendall(message)

        chunks = []
        while True:
            chunk = s.recv(1024)
            chunks.append(chunk)
            if chunk.endswith(b'\r\n'):
                break
        s.close()
        return b''.join(chunks)
