import re
phones ="karl-1234567890 , carol-0987654321 , john -5674893001"
pattern =r"\d{10}"
pattern_compiled= re.compile(pattern)
Result =re.findall(pattern_compiled,phones)
print(Result)

with open("student_details","rt") as f:
    data =f.read()

print(data,type(data))

ph_matches =re.finditer(pattern_compiled,data)
print(ph_matches)

for matches in ph_matches:
    print(matches)