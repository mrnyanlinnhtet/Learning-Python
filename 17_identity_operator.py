#Special operator in identity operator ( Can check memory location and type)
# 1. is 
# 2. is not 

#Checking memory location
input1=int(input('Please insert something 1 :'))
input2=int(input('Please insert something 2 :'))

print('Memory Location of input 1 : {}'.format(id(input1)))
print('Memory Location of input 2 : {}'.format(id(input2)))

print('')
print('****************************************************')

if input1 is input2:
    print('They are same location !')
elif input1 is not input2:
    print('They are not same location !')
else:
    print('I have no idea about that !')