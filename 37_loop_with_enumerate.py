num_list=[1,2,3,4,5,6]

for index,value in enumerate(num_list):
    print('Index : {} => Value is {}'.format(index,value))
    num_list[index] *=2
    
    
print('')
print('List data are {}'.format(num_list))

