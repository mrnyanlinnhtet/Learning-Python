print("Press + : For Add")
print("Press - : For Subtract")
print("Press + : For Multiply")
print("Press + : For Divide")

sign=input("Enter your operation : ")
num1=int(input("Enter fist number : "))
num2=int(input("Enter second number : "))

if sign=='+':
    result=num1+num2
elif sign=='-':
    result=num1-num2
elif sign=='*':
    result=num1*num2
elif sign=='/':
    result=num1/num2
else:
   print('Something went wrong !')
   
print("{} {} {} = {}".format(num1,sign,num2,result))