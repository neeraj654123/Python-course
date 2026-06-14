# Keys of dict can be of multiple data type
# allowed : string,int,bool,tuple,float because they are immutable
# not allowed : list ,set ,dict because they are mutable

student1= {'id':123,'name':'rohan','marks':{'eng':88,'math':96,'science':78}}
# print(student1['marks']['math'])
print(student1.keys())
print(student1.values())
print(student1.items())    