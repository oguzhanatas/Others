'this code shows what is difference between normal processing and multiprocessing'
'you can change the all functions what you need.'
import numpy as np
import multiprocessing
import time

##########this section is a function which wants to test###########################################
'to test the processing times, a function which includes some for loops one within the other.'
def func(arg):
    out=[]
    for i in arg:
        for j in arg:
            for k in arg:
                out.append(i+j+k*5)
    return out

###########this section is to save what time you run this code#####################################
'to record the test time, a local time module'
totaltimes=open('data_output/multiTotalTimes.txt','a')
totaltimes.write('-------------------------------\n')
totaltimes.write(str(time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime()))+'\n')
totaltimes.write('-------------------------------\n')

###########this section is to run no multiprocessing###############################################
'run the function several times via for loop to get how long it takes.'
start_time=time.time()
for i in np.arange(100,200,25):#generate some values to run the function
    print('for ',i,', no multi is running...')
    out=func(np.random.random_sample(i))
end_time=time.time()
elapsed=end_time-start_time
totaltimes.write('noMulti total time: '+str(elapsed)+' seconds\n')
print('noMulti total time: ',elapsed,' seconds')

###########this section is to run multiprocessing module###########################################
'using multiprocessing module, we run a function several times via for loop to get how long it takes.'
start_time=time.time()
for i in np.arange(100,200,25):#generate some values to run the function
    print('for ',i,' multi is running...')
    out = multiprocessing.Process(target=func,args=([np.random.random_sample(i)])).start()
end_time=time.time()
elapsed=end_time-start_time
totaltimes.write('Multi total time: '+str(elapsed)+' seconds\n')
totaltimes.write('-------------------------------\n')
print('Multi total time: ',elapsed,' seconds')

###################################################################################################
totaltimes.close()

'for i in np.arange(100,200,25) == for i in [100,125,150,175]'