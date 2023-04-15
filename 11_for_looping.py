#For Looping with range function
for data in range(11):
   print("Data is : {}".format(data))

print('')
print('**************************************************')
print('')   

#For Looping with index
cities=['Sittwe','Yangon','Mandalay','Pathein','Kyauttaw']
indexNo=0
for index in range(5):
    indexNo+=1
    print('No({}).{}'.format(indexNo,cities[index]))
    
print('')
print('**************************************************')
print('') 

#For Looping with packing and unpacking
pair=[(1,2),(3,4),(5,6),(7,8),(9,10)]

for i,j in pair:
    print('Unpacking data : {} and {}'.format(i,j))
    
print('')
print('**************************************************')
print('') 

#For Looping with exception handling
for num in range(5):
    print('------------------------------')
    try:
        d=10/(num-3)
        print('Data = {}'.format(d))
    except ZeroDivisionError:
        print('Divided by zero !')
    finally:
        print('Alway run')
    print(num)

        