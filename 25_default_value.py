from datetime import datetime

def date_function(msg,*,date_time=None):
    if date_time is None:
        date_time=datetime.now()
        print('{} : {}'.format(msg,date_time))
        
date_function('Date Time data')

