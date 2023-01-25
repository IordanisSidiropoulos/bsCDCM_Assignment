"""
#
# File            : Q2_Reading_Apache2_page.py
# Created          : 24/01/2023 6:03 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Available under GNU Public License (GPL)
# Description     : Reading Apache 2 page (Question 2 [2.0, 2.1, 2.2, 2.3])
#
"""

import urllib.request


def readPageCode():
    """2.0_Scrapping Website Content"""
    print("\nPage Content:\n")

    url = "http://192.168.167.131"

    request2 = urllib.request.urlopen(url)
    request = request2.read()

    print(request)
    print("Apache" in urllib.request.urlopen(url))


if __name__ == "__main__":
    readPageCode()
