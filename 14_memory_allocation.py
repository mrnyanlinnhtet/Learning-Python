#Memory Address Build in Function
a=10
b=10
print('Memory address of a value : {}'.format(id(a)))
print('Hex value of memory address of a value : {}'.format(hex(id(a))))
print('')

#Checking memory address same value variable 
if hex(id(a)) == hex(id(b)):
    print('They are same address !')
else:
    print('They are difference address !')