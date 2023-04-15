#Pyramid Triangle Pattern
row=int(input('Please Enter Row : '))
size=row
for j in range(1,row):
    
    for i in range(size):
        print(end=" ")
    size=size-1
    for k in range(1,(j*2)):
        print('*',end="")
       
    print('')