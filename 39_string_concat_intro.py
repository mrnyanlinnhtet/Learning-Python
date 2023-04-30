greet='Hello buddy how do you do '
name='Nyan'

print(name*2)
print(greet + ' ?')
print('')
space=input('Enter String value with sapce >> ')
print('Using with strip method : ', space.strip())
print('')
print('Find buddy word index in : {}'.format(greet.find('buddy')))
print('swapcase',greet.swapcase())
print('swapcase',greet.title())