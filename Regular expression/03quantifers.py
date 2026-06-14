# +,*,?,{n}
import re

message ="The current Python version is 3.13 and the previous are 3.12,3.11,3.10"

pat =r"[a-z]{4}"
match_obj = re.search(pat,message)
print(match_obj)

pat =r"[A-Z][a-z]{5}"
match_obj = re.search(pat,message)
print(match_obj)

pat =r"[A-Z][a-z]{2,5}"
match_obj = re.search(pat,message)
print(match_obj)

# + => matches 1 or more repitions with the previous pattern 

pat =r"[A-Z][a-z]+"
match_obj = re.search(pat,message)
print(match_obj)

# ? => matches 1 or 1 repitions with the previous pattern 

pat =r"[A-Z][a-z]?"
match_obj = re.search(pat,message)
print(match_obj)

# * => matches 0 or more repitions with the previous pattern 

pat =r"[A-Z][a-z]*"
match_obj = re.search(pat,message)
print(match_obj)