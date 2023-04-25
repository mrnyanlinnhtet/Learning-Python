#Normal List declaration
my_list=[1,2,3,4]
print("Normal call index : {}".format(my_list[3]))
print('')
print('********************************')
print('')

#Slicing Element 
print('Slicing index 0 to 2 value is {}'.format(my_list[1:]))
print('')
print('********************************')
print('')

#Updating Element
subject_data=['Myanmar','English','Math','Physics','CP']
print('Before Update Data : {}'.format(subject_data))
subject_data[-1]='Computer Science'
print('After Update Data {}'.format(subject_data))
print("")
print('********************************')
print('')

#Remove Element
print('Before Removing Data : {}'.format(subject_data))
subject_data.remove('Myanmar')
print('Removing Data with remove : {}'.format(subject_data))
subject_data.pop(0)
print('Removing Data with pop: {} '.format(subject_data))
del subject_data[0]
print('Removing Data with del: {} '.format(subject_data))
print("")
print('********************************')
print('')

#Adding Data into list
car_list=['Toyota','Tesla','Honda']
print('Before adding data {}'.format(car_list))
car_list.append('Ford')
print('After adding data {}'.format(car_list))
print('Checking Length : {}'.format(len(car_list)))
print("")
print('********************************')
print('')

#Checking List Min or Max and get Reverse value
num_list=[1,2,3,4,5,6]
print('Max value of list : {}'.format(max(num_list)))
print('Min value of list : {}'.format(min(num_list)))
num_list.reverse()
print('Reverse value of list : {}'.format(num_list))
print("")
print('********************************')
print('')

#Searching index with value
fruit=['apple','orange','papaya','mango','banana','strawberry']
fruit_index=fruit.index('papaya')
print('Index of papaya is {}'.format(fruit_index))
print("")
print('********************************')
print('')

#Sum and sort function
my_num_list=[1,3,4,5,6,7,9,0]
print('Sum value is {}'.format(sum(my_num_list)))
my_num_list.sort()
print('Sorting value is {}'.format(my_num_list))
my_num_list.sort(reverse=True)
print('Reverse Sorting value is {}'.format(my_num_list))
fruit.sort()
print('Sorting string value {}'.format(fruit))
fruit.sort(reverse=True)
print('Reverse Sorting string value {}'.format(fruit))
fruit.sort(key=len,reverse=True)
print('Sorting with character length {}'.format(fruit))
print("")
print('********************************')
print('')

#Looping with list
animals=['tiger','dog','duck','bird','hen','cow']

for animal in animals:
    if(animal is 'tiger'):
        print('Tiger is found !')
    else:
        print('Tiger is not found !')
print("")
print('********************************')
print('')


#Removing element in list
number_list=[1,2,3,4,5,6]

for num in number_list[:4]:
    number_list.remove(num)
    print('Removing : {}'.format(num))
    
print(number_list)
print("")
print('********************************')
print('')

#Adding element into list
we_list=[]

for element in range(1,10):
    element = element ** 2
    we_list.append(element)
    print('Appending : {}'.format(element))
    
print(we_list)
print("")
print('********************************')
print('')

#Tuple to list
myTuple=(1,2,3,4,5)
print('Tuple to list : {}'.format(list(myTuple)))


