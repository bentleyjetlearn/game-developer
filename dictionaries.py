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
print(d)

#Game dictionary
d={'football':'Ronaldo',
   'basketball':'Le Bron James',
   'athlatics':'Bolt'}
print(d)
print(d['athlatics'])
d['cricket'] = 'Virat'
print(d)

#Vowels counter
x=input('Enter the sentence')
b={'a':0,'e':0, 'i':0, 'o':0, 'u':0} 
for i in x:
    if i in b:
        b[i]+=1

print(b)''' 

#Username and password program
c={'Bentley':'Benronpisani313','Nathan':'Nathanazz516','Tom':'Tomciap412'}
print('select an option\n1.log in \n2.Enter new user')

