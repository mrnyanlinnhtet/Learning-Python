sub_number=int(input('Enter subject number >> '))
pass_mark=float(input('Enter your school of pass marks >> '))
isPassed=True

for sub in range(sub_number):
   marks=float(input('Enter your mark >> '))
   isPassed=isPassed and marks >= pass_mark
   
passed='Pass the exam'
failed='Failed the exam'

result=passed if isPassed else failed

print('{}'.format(result))