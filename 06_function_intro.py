from math import sqrt
import math
#Standart Lib Functions

data=int(input("Enter number of square root : "))
print("The square root of {} is {} .".format(data,sqrt(data)))
print("The value of pi is {} .".format(math.pi))
print("The exp of {} is {}".format(data,math.exp(data)))
print("The hex value of {} is {}".format(data,hex(data)))

#Programmer Defined Functions

def myFun():
    print("Hello my function !");
    
def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b
    
#Function Invoke Process
myFun()

num1=int(input("Enter fist number : "))
num2=int(input("Enter second number : "))

print("Adding : {}".format(add(num1, num2)))
print("Subtrcting : {}".format(sub(num1, num2)))
print("Multiplation : {}".format(mul(num1, num2)))
print("Dividion : {}".format(div(num1, num2)))

