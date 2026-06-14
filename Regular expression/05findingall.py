import re

message ="The current Python version is 3.13 and the previ"
pat = r"[A-Z][a-z]"
matchobj= re.findall(pat,message)
# print(matchobj)


phone ="john-3858232567 ,carol-8436398765 and jim -1234567890,45787573489572,47835346792563579234"
pat =r"[0-9]{10}"
matchobj=re.findall(pat,phone)
# print(matchobj)

# \b  matches a position

pat =r"\b[0-9]{10}\b"
matchobj=re.findall(pat,phone)
# print(matchobj)

# finditer()

pat =r"\b[0-9]{10}\b"
matchobj_iter=re.finditer(pat,phone)
print(matchobj_iter)

for match in matchobj_iter:
    print(match)