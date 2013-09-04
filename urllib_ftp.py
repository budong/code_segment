#!/usr/local/python2.7/bin/python2.7

"""
url retriever

Usage:
url_retrieve_urllib.py URL FILENAME

URL:
if the URL is an FTP URL the format should be:
ftp://[username[:password]@hostname/filename
If you want to use absolute paths to the file to download,
you should make the URL look somthing like this:
ftp://user:password@host/%2Fpath/to/myfile.txt
Notice the '%2F' at the beginning of the path to the file.

FILENAME:
absolute or relative path to the filename to save download file as
"""

import urllib
import sys

if '-h' in sys.argv or '--help' in sys.argv:
    print __doc__
    sys.exit(1)

if not len(sys.argv) == 3:
    print 'URL and FILENAME are mandatory'
    print __doc__
    sys.exit(1)

url = sys.argv[1]
filename = sys.argv[2]
print url,filename
urllib.urlretrieve(url,filename)

