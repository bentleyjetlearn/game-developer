list = [[1,2,3],[4,5,6],[7,8,9]]
print(len(list))
print(len(list[0]))
print(list[1][1])
print(list)

for i in list:
    print(i)

for i in range (len(list)):
    for j in range(len(list[0])):
        print(list[i][j],end=' ')
    print()

#create matrix by taking input
matrix=[]
r=int(input('enter no.of rows'))
c=int(input('enter no. of coloumns'))
for i in range(r):
    temp=[]
    for j in range(c):
        num=int(input('enter the number'))
        temp.append(num)
    matrix.append(temp)
print(matrix)
