#!/usr/bin/env python

import paramiko
import os

hostname = ''
port = 22
username = ''
password = ''
dir_path = ''  # Remote directory to be parsed

if __name__ == "__main__":
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    files = sftp.listdir(dir_path)
    for f in files:
        print('Retrieving', f)
        sftp.get(os.path.join(dir_path, f), f)
    t.close()
