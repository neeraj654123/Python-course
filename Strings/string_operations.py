# strip  -used to remove extra spaces
# replace - used to replace character word in string 
# count - used to count no. of substring
# upper,lower,title,capatilize - used to change cases of string 
# startswith - used to check given string start with particular character or word or words
# endswith - used to check given string end with particular character or word or words


a='  python is good,python is awesome'
b='python'
print(a.strip())
print(a.replace('python','java',1))
print(a.count(b))
print(a.upper())
print(a.lower())
print(a.title())
print(b.capitalize())
print(b.startswith("w"))
print(b.endswith("n"))