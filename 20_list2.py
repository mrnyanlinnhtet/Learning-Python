#Returning Function to Function

def square(num):
    return num**2


def cube(num):
    return num**3

nums=input('Which operation do you want to do ? : ')
numbers=int(input('Please insert number : '))
def operation(num):
    if num == 'square':
        return square
    else:
        return cube

result=operation(nums)
print(result(numbers))
print('')
print('******************************')
print('')

#Function to Function calling
def function_call(fun,num):
    return fun(num)

result=function_call(square,2)
print('Function to function calling result is {}'.format(result))