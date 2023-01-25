"""
#
# File            : File_eg_ZIP_4.py
# Created          : 20/01/2023 4:38 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Available under GNU Public License (GPL)
# Description     : Creating a Zip file
#
"""

import os
import zipfile


def zip_file_processing1():
    """Zip file demo"""

    os.chdir(os.path.normpath("/Users/iordAnisMusic/Desktop/ZIP TEST FOLDER"))

    newZip = zipfile.ZipFile('new_Zip_Test_File.zip', 'a')  # Create a zip file can be r, w, a for read/write/append
    newZip.write('New_song_file.txt')  # adding a file in the zip file

    print("{}".format(newZip.printdir()))  # Show contents of the file
