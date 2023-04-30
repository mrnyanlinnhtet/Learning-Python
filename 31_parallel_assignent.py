#Before using parallel assignment opeator
x=1
y=2
print('Before exchange variable values are x : {} and y : {}'.format(x,y))
print('')
temp=x
x=y
y=temp
print('After exchange variable values are x : {} and y : {}'.format(x,y))
print('')

#After using parallel assignment operator
x=1
y=2
print('Before using parallel assignment varible values are x : {} and y : {}'.format(x,y))
x,y=y,x
print('After using parallel assignment variable values are x : {} and y : {}'.format(x,y))

print('')

x=0
y=[10,20,40]
x,y[x]=1,2

print('Value of X and Y are {} , {}'.format(x,y))