#!/usr/local/python2.7/bin/python2.7

import os

class diskwalk(object):
    """API  for getting directory walking collections"""
    def __init__(self,path):
        self.path = path

    def enumaratepaths(self):
        """Return the path to all the files in a directory recursively"""
        path_collection = []
        for dirpath,dirnames,filenames in os.walk(self.path):
            for file in filenames:
                fullpath = os.path.join(dirpath,file)
                path_collection.append(fullpath)
        return path_collection

    def enumaratefiles(self):
        """Return all the files in a directory as a list"""
        file_collection = []
        for dirpath,dirnames,filenames in os.walk(self.path):
            for file in filenames:
                file_collection.append(file)
        return file_collection

    def enumaratedir(self):
        """Return all the directories in a directory as a list"""
        dir_collection = []
        for dirpath,dirnames,filenames in os.walk(self.path):
            for dir in dirnames:
                dir_collection.append(dir)

        return dir_collection

