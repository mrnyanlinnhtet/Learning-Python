import time

def time_fun(fun,*arg,times=1,**keyword):
    start=time.perf_counter()
    for i in range(times):
        fun(*arg,**keyword)
    end=time.perf_counter()
    avg_time=(end-start)/times
    fun(avg_time)
    
time_fun(print,1,2,3,4,5,end='* * * \n',times=5)