import re

'''
Understanding the Python re module.
@author: Srinivas Kini
'''

# Python Raw String
print('\tTab')  # \t is considered as a special character.
print(r'\tTab')  # \t is considered as a part of the string.

# Regex meta characters : . ^ { } [ ] ( ) \ | $ * + ?, these are special characters even in the raw string.
# These have to be escaped using a backslash.
# . -> Matches any character except the newline (\n).
# \d -> Any digit (0-9).
# \D -> Not a digit.
# \w -> Word (a-z, A-Z, 0-9, _).
# \W -> Not a word.
# \s -> Whitespace, tab, newline.
# \S -> Not a whitespace, tab, newline.

# Regex Anchors
# \b -> word boundary (like a space, newline or start of a sentence that separates two words)
# \B -> not a word boundary
# ^ -> Beginning of a string
# $ -> End of a string
# [] -> Match characters in these brackets
# [^] -> Match characters not in these brackets

# Charset [] rules
# It will only match the characters one by one
# '-' at the end and the beginning will be the literal '-' eg. [-$#] (read as - or $ or #)
# if it is put in the middle it represents the range eg. [A-Z]
# ^ inside the charset works as a negation operator [^x] (match any character that is not an x)

# Quantifiers
# * -> match 0 or more occurences
# + -> match 1 or more occurences
# ? -> match 0 or 1 occurence
# {3} -> exact number of occurences
# {0,4} -> min,max range of occurences





text_to_search = 'abcdefghijklmnopqrstuvwxyz' \
                 '1234567890' \
                 '@#$%^&*()' \
                 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

pattern_abc = re.compile(r'abc')  # regex to find the pattern abc, case sensitive
matcher_abc = pattern_abc.finditer(text_to_search)  # pattern matching iterator to find the given pattern

for match in matcher_abc:
    print(f'"abc ->"{match.span()}')  # returns the start and end indices of the matches

url = 'srinivaskini.com'  # to match this entire url, escape the . with \.
pattern_url = re.compile(r'srinivaskini\.com')  # escape the . in the url since it is a meta character
matcher_url = pattern_url.finditer(url)

for match in matcher_url:
    print(f'"srinivaskini.com ->"{match.span()}')  # returns the start and end indices of the matches

not_words = re.compile(r'\W').finditer(text_to_search)  # regex for any character that is not a word

for nw in not_words:
    print(f'{nw}')  # @#$%^&*()

word_boundary_str = 'Ha HaHa'
wb_matcher = re.compile(r'\bHa').finditer(word_boundary_str)

for match in wb_matcher:
    print(match.group())  # Will match the first two 'Ha' since they have a word boundary

sentence_start = 'Start of a sentence.'
start_matcher = re.compile(r'^Start').finditer(sentence_start)  # Matches any string that starts with the word 'Start'

for match in start_matcher:
    print(match.group())

sentence_end = 'This is the end'
for match in re.compile(r'end$').finditer(sentence_end): # matches any string that ends with the word 'end'
    print(match.group())