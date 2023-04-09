import secrets

print('Printing Integer Number Using Secrets Module')
print('')
print("*********************************")
print('')
#secret module randint() 
secureGenerator=secrets.SystemRandom();
integerRandom=secureGenerator.randint(0,9)
print('Integer random number value is {}'.format(integerRandom))
print('')
print("*********************************")
print('')
#secret module randrang() function
rangRandom=secureGenerator.randrange(0,10,2)
print('Using randrang() value : {}'.format(rangRandom))
print('')
print("*********************************")
print('')
#secret module choice() fuction
name=['Nyan','Linn','Htet','Tony','Stark']
choinceName=secureGenerator.choice(name)
print('Secure Choice Number is {}.'.format(choinceName))
print('')
print("*********************************")
print('')
#secret module sample() function
sampleName=secureGenerator.sample(name,3)
print('Secure sample number is {}'.format(sampleName))
print('')
print("*********************************")
print('')
#secret module uniform() function
uniformName=secureGenerator.uniform(1.5,10.5)
print('Secure uniform number is {}.'.format(uniformName))
print('')
print("*********************************")
print('')
#token byte function
print('Token byte random value {}'.format(secrets.token_bytes(2)))
print('')
print("*********************************")
print('')
#token hex function(1 byte 2 hex)
print('Token hex random value {}'.format(secrets.token_hex(4)))
print('')
print("*********************************")
print('')
resetInfo='https://nyanlinnhtet/ultron/reset='
resetInfo+=secrets.token_urlsafe(32)
print('Token URL Safe value {}'.format(resetInfo))