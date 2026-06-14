import re
message ="the current python version is 3.13 and the previous are 3.12,3.11,3.10"

match_object = re.search("\d[0-9]",message)
print(match_object)

match_object = re.search("[0-9].[0-9][0-9]",message)
print(match_object)

match_object = re.search("[0-9].[0-9]","254/A")
print(match_object)

# . matches any character expect newline character(\n) and [.] will match exact . character
