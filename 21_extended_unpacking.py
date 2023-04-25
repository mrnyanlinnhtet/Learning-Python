#Extended Unpacking List and tuple 
a,*b=[1,2,3,4,5]
print('Value of a is {}'.format(a))
print('Value of b is {}'.format(b))
print('')
print('***********************')
print('')
l1=[1,2,3,4]
l2=[5,6,7,8]
list=[*l1,*l2]
print('Value of list is {}'.format(list))
a,*b,(c,*d,e)=[1,2,3,'STARK TECH']
print('Value of a is {}, b is {}, c is {} , d is {} and e is {}'.format(a,b,c,d,e))

#Arbitrary Argument

def get_num(*arg):
    print("Value of arbitrary arg is {}.".format(arg))
    
get_num(1,2,3,4)