import re

with open("student_details","rt") as f:
    data = f.read()

pattern =r"\b[a-z]+[\w.-]+[@][a-z]+[.][a-z]"
match_obj =re.finditer(pattern,data)
print(match_obj)

for matches in match_obj:
    print(matches)