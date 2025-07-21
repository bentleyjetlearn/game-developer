with open('test.txt','w') as myfile:
    myfile.write('Hi, my name is Bentley. I am12 years old')

with open('test.txt','r') as myfile:
    print(myfile.read())


with open('test.txt','w') as myfile:
    myfile.write(' My hobby is playing the violin')



print('\nAfter adding more text:\n')

with open('test.txt','r') as myfile:
    print(myfile.read())