my_data={1,200,3,55,2,1}
print(my_data)
my_data.add(44)
print(my_data)
my_data.remove(44)
print(my_data)
print('')

#Union with two set data
set1=set([1,2,3,4])
set2=set([4,5,6])
set3=set1.union(set2)
print('Union Value with union function : {}'.format(set3))
set4=set1 | set2
print('Union Value with union operator : {}'.format(set4))
print('')

#Intersection with two set data
data1={1,2,3,4}
data2={1,2,5,6}
data3=data1.intersection(data2)
print('Intersection Value with intersecton function : {}'.format(data3))
data4=data1 & data2
print('Intersection Value with intersection operator : {}'.format(data4))
print('')

#Difference between two set data
dif1={1,2,3,4}
dif2={1,2,5,7}
dif3=dif1.difference(dif2)
dif4=dif2.difference(dif1)
print('Difference Value with diffenence function :  For dif1 -> {} and For dif2 -> {}'.format(dif3,dif4))
dif5=dif1-dif2
print('Diffenence Value with difference operator : {}'.format(dif5))

#Forzen set ( mu to immu )
frozenset(dif1)
print('Dif1 is frozen set and it\'s data is {}'.format(dif1))