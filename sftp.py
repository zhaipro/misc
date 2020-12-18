import os

import paramiko


def upload(host, port, username, password, ipath, opath):
    transport = paramiko.Transport((host, port))
    transport.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    for fn in os.listdir(ipath):
        ifn = os.path.join(ipath, fn)
        ofn = os.path.join(opath, fn)
        print('put:', ifn, ofn)
        sftp.put(ifn, ofn)
    transport.close()


if __name__ == '__main__':
    pass
