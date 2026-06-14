marks1 ={'maths':80.5,'physics':90,'chemistry':78.5}
marks2={'sst':67,"science":87}
# get 
print(marks1.get('eng',88))

marks1['eng']=88
print(marks1)

marks1.update(marks2)
print(marks1)

marks1.pop('eng')
print(marks1)