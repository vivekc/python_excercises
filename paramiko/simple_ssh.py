#!/usr/bin/env python

import paramiko
from __init__ import *

if __name__ == "__main__":
    with paramiko.SSHClient() as s:
        s.load_system_host_keys()
        s.connect(hostname, port, username, password)
        stdin, stdout, stderr = s.exec_command('ifconfig')
        print(stdout.read())

