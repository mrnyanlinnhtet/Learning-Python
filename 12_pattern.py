#Using Enumerate 
name="nyanlinnhtet"
for index,value in enumerate(name):
    print('Index is {index} and value is {value}'.format(index=index,value=value))
    
#Basic Pattern
input=int(input('Enter your row number : '))
for i in range(1,input):
   for z in range(i,0,-1):
        print(z,end='')
   print('')