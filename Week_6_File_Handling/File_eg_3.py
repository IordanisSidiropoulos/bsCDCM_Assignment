"""
#
# File            : File_eg_3.py
# Created          : 20/01/2023 4:22 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Available under GNU Public License (GPL)
# Description     :
#
"""

import os

def file_processing(file_name):
    """Using seek with files"""

    file_obj = open(file_name, "r+")

    #file_obj.seek(0)  # rewind the file, start at 0 position

    # 2
    #file_obj.seek(10, 0)
    # Move 10 bytes forward from the start at file 0=SEEK_SET

    # 3
    #file_obj.seek(1, os.SEEK_SET)
    # Move one byte forward from the beginning

    # 4
    #file_obj.seek(0, os.SEEK_CUR)
    # Seek the current position, offset must be 0

    # 5
    #file_obj.seek(0, os.SEEK_END)
    # Reset the current position

    all_file_contents = file_obj.read()  # Read the files from the set position
    print(all_file_contents)