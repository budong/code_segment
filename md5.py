#!/usr/local/python2.7/bin/python2.7
import hashlib

def md5Checksum(filePath):
    with open(filePath, 'rb') as fh:
        m = hashlib.md5()
        while True:
            data = fh.read(8192)
            if not data:
                break
            m.update(data)
        return m.hexdigest()

print('The MD5 checksum of text.txt is', md5Checksum('/tmp/mumayidianzishichangMumayiMarket_V1.7.2_mumayi_7a9f5.apk'))
