"""
#
# File            : Q2.py
# Created          : 22/05/2023 8:29 a.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Available under GNU Public License (GPL)
# Description     : This is the code of the question 2 from the OOPR assignment.
#
"""

# Making a request to the URL
import requests
from bs4 import BeautifulSoup
import re

# Step 1.1: Defining the URL to request
url = "http://192.168.167.131"

# Step 1.2: Sending a Get request to th URL
response = requests.get(url)
html_content = response.content

#Step 2: Print the headers
print("Headers: ")
for header in response.headers:
    print(f"{header}: {response.headers[header]}")

# Step 3: Parsing Html content using beautiful soup
soup = BeautifulSoup(html_content, "html.parser")
text = soup.get_text()

# Step 4: Defining a pattern and splitting the text into lines
pattern = re.compile(r"Apache2", re.IGNORECASE)
lines = text.splitlines()

# Step 5: Count the number of occurencies of "Apache2" in HTML tags
count = 0

for tag in soup.find_all(True):
    for attr in tag.attrs:
        count += tag.attrs[attr].count("apache2")

# Step 6: Counting the number of occurencies of "Apache2" in the next lines
for line_num, line in enumerate(lines, 1):
    matches = re.finditer(pattern, line)
    for match in matches:
        count += 1

# Step 7: Print the total count of occurencies
print("The number of occurences of ´Apache2´ is: ", count)