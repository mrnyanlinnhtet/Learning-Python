li=[1,2,3,4,5,6]
data=7
index=0
found=False

while index < len(li):
    if(li[index] == data):
        found=True
        break
    index += 1
    
if not found:
    li.append(7)
    
print(li)