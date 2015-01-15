# -*- coding: utf-8 -*-
"""
iremocon.py: Send and Recieve Messages with i-remocon
"""
import socket
import json
import configparser

class IRemocon(object):
    """
    Command Sender class
    """

    def __init__(self, config_file):
        """
        Make a New Instance
        """
        def invert_dict(src_dict, inverted_dict, key_str):
            """ make invert dict from dict """
            for k in src_dict:
                new_key = ''.join([key_str, '[', k, ']'])
                if not (isinstance(src_dict[k], dict)):
                    inverted_dict[str(src_dict[k])] = new_key
                else:
                    inverted_dict = invert_dict(src_dict[k], inverted_dict, new_key)
            return inverted_dict


        config = configparser.ConfigParser()
        config.read(config_file)
        self._host = config.get('network', 'HOST')
        self._port = int(config.get('network', 'PORT'))
        self._remocon_filename = config.get('remocon code', 'filename')
        f = open(self._remocon_filename, encoding='utf-8')
        self.code = json.load(f)
        f.close()
        self.inverted_code = invert_dict(self.code, {}, '')

    def SendCommand(self, message):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(60)
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
