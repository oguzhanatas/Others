import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



#the line fucntion
def funct(x,y,deg):
    p=np.polyfit(x,y,deg)
    line=np.poly1d(p)
    return line

#generate random x and y
x=np.random.random_sample(1000)
y=np.random.random_sample(1000)

#generate a line
linex=np.linspace(x.min(),x.max(),len(x))
liney=funct(linex,y,3)

#masking points in red solid line neighborhood 0.1  (you can change the value what you need)
linewidth=0.2
mask_inLines=((np.abs(y-liney(x))<=linewidth))

#masking x and y points in the selected width
x_in=x[mask_inLines]
y_in=y[mask_inLines]


#scatter plot raw x and y points
plt.scatter(x,y,marker='.',edgecolors='None',s=8,label='Total: '+str(len(x))+' points')
#scatter plot selected x and y points
plt.scatter(x_in,y_in,marker='x',color='grey',edgecolors='None',s=8,label='RedLine neighborhood 0.1: '+str(len(x_in))+u' points')
#plot the lines with selected width
plt.plot(linex,liney(linex),'r-',lw=0.5)
plt.plot(linex,liney(linex)-linewidth,'y--',lw=1)
plt.plot(linex,liney(linex)+linewidth,'g--',lw=1)
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left',prop={'size':8})
plt.savefig('./fig_output/'+'inLinesData.png')
plt.show()



#saving data in the lines
new_data=pd.DataFrame({'x':x_in,'y':y_in})
new_data.to_csv('./data_output/'+'inLinesData.csv',index=None)