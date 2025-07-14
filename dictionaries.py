'''d={'France':'Paris',
   'Italy':'Rome',
   'Malta':'Valletta'}
print(d)
#find length of dictionary
print(len(d))
#acess value
print(d['Malta'])
print(d.get('India','unknown'))
#adding new key-value pair
d['Norway'] = 'Oslo' 
print(d)
print(d.keys())
print(d.values())
#Looping over dictionary
for i in d:
    print(i,d[i])

for key,value in d.items():
    print(key,value)
#delete a key-value pair
del d['France']
print(d)'''

#Game dictionary
d={'football':'Ronaldo',
   'basketball':'Le Bron James',
   'athlatics':'Bolt'}
print(d)
print(d['athlatics'])
d['cricket'] = 'Virat'
print(d)