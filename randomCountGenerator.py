import numpy as np
import matplotlib.pyplot as plt


#generate random noise count in range
count_list=np.random.uniform(low=3.-np.sqrt(3.),high=3.+np.sqrt(3.),size=(10**3,))
#generate photon count in range
photon_list=np.random.uniform(low=20.-np.sqrt(20.),high=20.+np.sqrt(20.),size=(10**3,))
#select random photon count in the photon list
select_photon=np.random.choice(photon_list,size=5)
#select random count in the noise count list
select_count=np.random.choice(count_list,size=5)


#replace some random count with the photon count
for j in  range(len(select_photon)):	
	for n,i in enumerate(count_list):
		if i==select_count[j]:
			count_list[n]=select_photon[j]
	
			
			
spec_list=np.array(count_list)

indexs=[]
values=[]
replacements=[]

for jj,zz in enumerate(spec_list):
    if zz>10:
        indexs.append(jj)
        values.append(zz)
        replacements.append(np.logspace(np.log(zz/np.exp(1.63333)),np.log(2.),20))

indexss=[]
for i in indexs:
    indexss.append(np.linspace(i,i+19,20))

for i in range(5):
    for ii in range(20):
        try:
            spec_list[int(indexss[i][ii])]=replacements[i][ii]
        except IndexError:
            None

time=np.linspace(0,100,len(spec_list))



fig=plt.figure(figsize=(10,5))
ax=fig.add_subplot(111)
ax.plot(time*0.0005,spec_list,lw=0.8)
ax.set_ylabel("Intensity")
ax.set_xlabel("time ($s$)")
plt.show()
