import re
s1 ="Python is a programming laguage with version 3.13"

pat =r"[A-Z][a-z][a-z]"

match_obj= re.search(pat,s1)
print(match_obj)

# \d and \D
# \d matches 1 digit character.It is similar to [0-9]
# \D matches 1 non digit character.


pat =r"[A-Z][a-z][a-z]\D"
match_obj= re.search(pat,s1)
print(match_obj)

# \s and \S
# \s matches any white space character and \S matches any character except whitespace

s2 ="""
hi there
we are learning python
"""

pat =r"[a-z][a-z][a-z]\s"
match_obj= re.search(pat,s2)
print(match_obj)

pat =r"[a-z][a-z][a-z]\S"
match_obj= re.search(pat,s2)
print(match_obj)

# \w matches character [0-9],[a-z],[A-Z],_
# \W matches characters expect [0-9],[a-z],[A-Z],_

s2 ="""
hi there
we are learning python
"""

pat =r"[a-z][a-z][a-z]\w"
match_obj= re.search(pat,s2)
print(match_obj)

pat =r"[a-z][a-z][a-z]\W"
match_obj= re.search(pat,s2)
print(match_obj)
