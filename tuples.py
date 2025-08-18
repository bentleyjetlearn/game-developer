'''x=(1,2,3,4,5)
print(type(x))
print(x[3])
print(x[2:5])
address=(25,'Benja',"St.John's road", 'New york', 'England', 57863)
(doornum, place, streetname, city, country, zipcode)=address
print(country)'''

#enter a storing competition details
list=[]
for i in range(5):
    print('-'*20)
    groupname=input('enter the name of the group ')
    sizeofgroup=input('enter the size of the group ')
    dateofcompetition=input('enter the date of the competition ')
    venue=input('enter the name of the place ')
    typeofmedal=input('enter the type of medal ')
    details=(groupname, sizeofgroup, dateofcompetition, venue, typeofmedal)
    list.append(details)
print(list)
