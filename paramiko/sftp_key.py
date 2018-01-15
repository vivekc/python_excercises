import paramiko
import os

hostname = ''
port = 22
username = ''
dir_path = ''  # remote directory to be read
pkey_file = '~/.ssh/id_rsa'

if __name__ == "__main__":
    key = paramiko.RSAKey.from_private_key_file(pkey_file)
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, pkey=key)
    sftp = paramiko.SFTPClient.from_transport(t)
    files = sftp.listdir(dir_path)
    for f in files:
        print('Retrieving', f)
        sftp.get(os.path.join(dir_path, f), f)
    t.close()