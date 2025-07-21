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
c = {'Bentley': 'Benronpisani313', 'Nathan': 'Nathanazz516', 'Tom': 'Tomciap412'}

print('Select an option:\n1. Log in\n2. Enter new user')
q = input('Select option (1 or 2): ')

if q == '1':
    username = input('Enter the username: ')
    if username in c:
        password = input('Enter the password: ')
        if c[username] == password:
            print('Login successful!')
        else:
            print('Incorrect password.')
    else:
        print('Username not found.')

elif q == '2':
    new_user = input('Enter a new username: ')
    if new_user in c:
        print('Username already exists. Please try another one.')
    else:
        new_pass = input('Enter a password for the new user: ')
        c[new_user] = new_pass
        print('New user added successfully!')

else:
    print('Invalid option. Please choose 1 or 2.')