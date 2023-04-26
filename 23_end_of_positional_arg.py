#Keyword only eop (*)

def my_fun(a,b,*,c):
    print(a,b,c)
    
my_fun(1,2,c=4)

#Keyword argument (**)
def my_fun1(**arg):
    print(arg)


my_fun1(a=2,b=8,c=9)