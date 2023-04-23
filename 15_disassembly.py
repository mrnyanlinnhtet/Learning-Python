import dis

a=20
b=30

#Import Byte Code
dis.dis(compile("c=a+b*2","","exec"))
print(dir())