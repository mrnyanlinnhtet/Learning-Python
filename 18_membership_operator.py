list1=[1,2,3,4,5]
list2=[6,7,9,1]

def overlap(arg1,arg2):
    a=0
    b=0
    
    for i in arg1:
        a+=1
    for j in arg2:
        b+=1
        
    for k in range(0,a):
        for j in range(0,b):
            if(arg1[k] == arg2[j]):
                return 1
    return 0

if overlap(list1,list2) == 1:
    print('They have overlap !')
elif overlap(list1,list2) == 0:
    print('They are not overlap')