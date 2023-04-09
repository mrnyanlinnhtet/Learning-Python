import random

#Random for floating point between 0 to 1
print('')
print('Random for floating point number between 0 to 1 is {}'.format(random.random()))
print('')
print("*********************************")
print('')
#Random for integer number
print('Printing random for integer using randint() is {}'.format(random.randint(0,9)))
print('')
print("*********************************")
print('')
print('Printing random for integer using randrange() is {}'.format(random.randrange(0,10,2)))
print('')
print("*********************************")
print('')
#Random for choice using list or set or turple or something
cars=['tesla','toyota','muzeda','honda','ford']
print('Using random.choice() value is {}'.format(random.choice(cars)))
print('')
print("*********************************")
print('')
#Random for sample 
print('Using random.sample() value is {}'.format(random.sample(cars,3)))
print('')
print("*********************************")
print('')
#Random for seed
random.seed()
print('Using random.seed(arg) value is {}'.format(random.random()))
print('')
print("*********************************")
print('')
#Random for shuffle
print('Before Shuffle, data are : {}'.format(cars))
random.shuffle(cars)
print('After Shuffle, data are : {}'.format(cars))
print('')
print("*********************************")
print('')
#Random for uniform
print('Using random.uniform() value is {}'.format(random.uniform(1.0,10.0)))
print('')
print("*********************************")
print('')
#Random for triangular
print('Using random.triangular() value is {}'.format(random.triangular(10.5,20.5,10.0)))