import re

# sub

s1 ="Sunday,Monday,Tuesday,Monday,Sunday,Saturday"
pat =r"S[a-z]+"
replacement="Friday"
result =re.sub(pat,replacement,s1)
print(result)


message="""We are learning re. Using RE we can search forapattern for a given string.
Using sub(), we can replace the pattern with a given string as well"""

patt= r"\bre\b"
replace =" Regular Expression"


result =re.sub(patt,replace,message,flags=re.IGNORECASE)
print(result)

