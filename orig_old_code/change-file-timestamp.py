#!/usr/bin/env python3
# Problem:
# need to change modification time (timestamp) on folders

# Usage:
#
# ref:
# Google: python 3 change file timestamp -> http://www.dreamincode.net/forums/topic/307923-change-timestamp-on-file-to-current-time/
# Google: .python3 os.scandir -> https://www.blog.pythonlibrary.org/2016/01/26/python-101-how-to-traverse-a-directory/ -> https://www.blog.pythonlibrary.org/2013/11/14/python-101-how-to-write-a-cleanup-script/


# Author: AaronLaw
# Last Update: 2017-04-13
import os, time, datetime
import stat as st

folders = []
files = []

# returns a list of all files on the current directory
dir_root = '.'
os.chdir(dir_root)

def change_timestamp(dir_root):
    """
    Change timestamp of file or directory.
    """
    for entry in os.scandir(dir_root):
        print("Affected with timestamp: {} ".format(entry) )
        
        if entry.is_file():
            files.append(entry.path)
        if entry.is_dir():
            folders.append(entry.path)
        st = os.stat(entry)
        atime = st[ST_ATIME] #access time
        mtime = st[ST_MTIME] #modification time

        new_mtime = mtime+(4*3600)
#        print(atime)

        try:
            #modify the file timestamp
            os.utime(entry, (atime, new_mtime))
            #change_timestamp(entry)
        except OSError:
            print("Unable to change timestamp: {}".format(entry.path) )
			
if __name__ == "__main__":
    change_timestamp(dir_root)
    print(files)
    print(folders)