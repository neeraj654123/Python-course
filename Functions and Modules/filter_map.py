# filter(function,seqence)

seq =[1,2,3,4]
filtered_output =filter(lambda x: True if x%2!=0 else False,seq)
mapped_output =map(lambda x: True if x%2!=0 else False,seq)
print(list(filtered_output))
print(list(mapped_output))
