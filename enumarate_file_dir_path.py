#!/usr/local/python2.7/bin/python2.7

import os
path = "/tmp"

def enumaratepaths(path=path):
    """Return the path to all the files in a directory recursively"""
    path_collection = []
    for dirpath,dirnames,filenames in os.walk(path):
        for file in filenames:
            fullpath = os.path.join(dirpath,file)
            path_collection.append(fullpath)
    return path_collection

def enumaratefiles(path=path):
    """Return all the files in a directory as a list"""
    file_collection = []
    for dirpath,dirnames,filenames in os.walk(path):
        for file in filenames:
            file_collection.append(file)
    return file_collection

def enumaratedir(path=path):
    """Return all the directories in a directory as a list"""
    dir_collection = []
    for dirpath,dirnames,filenames in os.walk(path):
        for dir in dirnames:
            dir_collection.append(dir)

    return dir_collection

if __name__ == "__main__":
    print "\nRecursive listing of all paths in a dir:"
    for path in enumaratepaths():
        print path
    print "\nRecurisive listing of all files in dir:"
    for file in enumaratefiles():
        print file
    print "\nRescurisive listing of all dirs in dir:"
    for dir in enumaratedir():
        print dir
