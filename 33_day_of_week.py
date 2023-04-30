days_of_weeks=('MON','TUE','WED','THU','FRI','SAT','SUN')
input_day_num=int(input('Enter Day Number >> '))

if input_day_num >= 0 and input_day_num <= 6:
    days=days_of_weeks[input_day_num]
    print('You are choice {}'.format(days))
else:
    print('Can\'t not decide ! ')
