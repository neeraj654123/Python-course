import re

message ="The current Python version is 3.13 and the prev"

# ^ - only checks at the starting point

pat =r"^[a-z]{4}"
match_obj = re.search(pat,message)
print(match_obj)

# $ - only checks at the ending point

pat =r"[a-z]{4}$"
match_obj = re.search(pat,message)
print(match_obj)

# () - group + | or

emails ="abc_4695@example.com lkfdl words hjow nkns@fg.edu"

pat =r"com|edu"
match_obj = re.search(pat,emails)
print(match_obj)