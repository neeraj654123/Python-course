fh= open("file2.txt","rt")

# content =fh.read(10) 
# print(content)
# print(type(content))

# line1 =fh.readline()
# line2 =fh.readline()
# line3 =fh.readline()
# line4 =fh.readline()
# print(line1)
# print(line2)
# print(line3)
# print(line4)

lines =fh.readlines()
print(lines)

for line in lines:
    print(line.strip())
fh.close()
