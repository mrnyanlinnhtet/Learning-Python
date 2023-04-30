num_list=[1,2,3,4,5,6]
index=0
found=False

my_choice=int(input('Enter you want to find number >> '))

while not found and (len(num_list)-1):
    if num_list[index] == my_choice:
        print('Found number at index {}'.format(index))
        found=True
    else:
        index+=1

print('>>>>>>>>>>>>>>> Terminate')