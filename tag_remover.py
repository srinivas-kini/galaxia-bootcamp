"""
Removes the XML tags from the response body and dumps the contents into a text file.
@author: Srinivas Kini
"""

import requests
import re

response = requests.get('https://httpbin.org/#/')
# Group 1 matches XML tags without any attributes, Group 2 removes the <> from attributed XML tags.
xml_tag_pattern = re.compile(r'(</?[a-zA-Z0-9]+>)|(<|>|/>)|(["=])|([a-zA-Z0-9]+\s[a-zA-Z0-9]+=)')
response_str = re.sub(xml_tag_pattern, '', response.text)
# print(response_str)
lines = response_str.split('\n')

for line in lines:
    print(line)

with open('contents.txt', 'w', encoding='utf-8', newline='') as contents:
    contents.write(response_str)
