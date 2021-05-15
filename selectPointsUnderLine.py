import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



#the line fucntion
def funct(x):
    y=x
    return y


x=np.random.random_sample(1000)
y=np.random.random_sample(1000)




#masking points in red solid line neighborhood 0.1  (you can change the value what you need)
mask_inLines=((np.abs(y-funct(x))<=0.1))


x_in=x[mask_inLines]
y_in=y[mask_inLines]



plt.scatter(x,y,marker='.',edgecolors='None',s=8,label='Total: '+str(len(x))+' points')
plt.scatter(x_in,y_in,marker='x',color='grey',edgecolors='None',s=8,label='RedLine neighborhood 0.1: '+str(len(x_in))+u' points')
line=np.linspace(x.min(),x.max(),100)
plt.plot(line,funct(line),'r-',lw=0.5)
plt.plot(line,funct(line)-0.1,'y--',lw=1)
plt.plot(line,funct(line)+0.1,'g--',lw=1)
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left',prop={'size':8})
plt.show()


#saving data in the lines
new_data=pd.DataFrame({'x':x_in,'y':y_in})
new_data.to_csv('./data_output/'+'inLinesData.csv',index=None)