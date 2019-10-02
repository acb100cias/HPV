#!/usr/bin/python

from numpy import *
from pandas import *
import matplotlib.pyplot as plt

########################
a=52*array(range(24))
b=(array(range(24)))
c=array(arange(0,1,0.1))
d=10*array(range(10))
e=array(arange(0,0.2,0.01))
f=10*array(range(2))

##Leer bases de datos######

e1=read_csv("e1.csv")
e2=read_csv("e2.csv")
e3=read_csv("e3.csv")

##############promedio#################

for j in [1,2,3]:
    e1=read_csv("e"+ str(j)+".csv")
    time=[]
    inf=[]
    vac=[]
    sane=[]
    v0=[]
    v1=[]
    v2=[]
    v3=[]
    e1s=list(e1.groupby('step'))
    for i in arange(len(e1s)):
        time.append(i+1)
        inf.append(e1s[i][1]['infected'].mean())
        sane.append(e1s[i][1]['sane'].mean())
        vac.append(e1s[i][1]['vaccinated'].mean())
        v0.append(e1s[i][1]['v0'].mean())
        v1.append(e1s[i][1]['v1'].mean())
        v2.append(e1s[i][1]['v2'].mean())
        v3.append(e1s[i][1]['v3'].mean())

    datos={'time':time,'infected':inf,'sane':sane,'vaccinated':vac,'v0':v0,'v1':v1,'v2':v2,'v3':v3}
    datos=DataFrame(datos)
    datos=datos.loc[datos['time'] < 1352]
    datos=datos.filter(['vaccinated','v0','v1'])
    datos=datos.interpolate(method='nearest')
    plt.figure()
    datos.plot(grid=[])
    plt.title("Experiment "+ str(j)) 
    plt.xticks(a,b)
    plt.xlabel("Years")
    #plt.yticks(e,f)
    plt.ylabel("% People")
    plt.legend(('vacinated','non-vaccine virus','vaccine-virus'),loc='upper right', shadow=True, fancybox=True ,framealpha=1,fontsize='small')
    plt.savefig("e"+ str(j)+"_vaccine_and_non_vaccine_mean"+".pdf") 
    plt.close()

    plt.figure()
    datos.plot(logx=True,logy=True,grid=[])
    plt.title("Experiment "+ str(j)) 
    plt.xticks()
    plt.xlabel("Years")
    #plt.yticks(e,f)
    plt.ylabel("% People")
    plt.legend(('vacinated','non-vaccine virus','vaccine-virus'),loc='upper right', shadow=True, fancybox=True ,framealpha=1,fontsize='small')
    plt.savefig("e"+ str(j)+"_vaccine_and_non_vaccine_mean_logx"+".pdf") 
    plt.close()
        
    
    
    
