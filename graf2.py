#!/usr/bin/python

from numpy import *
from pandas import *
import matplotlib.pyplot as plt

########################
a=104*array(range(24))
b=2*(array(range(24)))
c=array(arange(0,1,0.1))
d=10*array(range(10))
e=array(arange(0,0.4,0.1))
f=10*array(range(4))
g=52*array(range(26))
h=array(range(26))
##Leer bases de datos######

e1=read_csv("e1.csv")
e2=read_csv("e2.csv")
e3=read_csv("e3.csv")

#########por Run###############
for j in [1,2,3]:
    e1=read_csv("e"+ str(j)+".csv")
    for i in arange(1,10):
        run=e1.loc[e1.run == i]
        datos=run.filter(['v0','v1']).cumsum().max()
        plt.subplots()
        datos.plot(kind='bar',grid=[])
        plt.title("Experiment "+ str(j)+"  Run " + str(i)) 
        #plt.xticks([0,1],['Non-vac','Vac'])
        plt.xlabel("HPV virus type")
        #plt.yticks(c,d)
        plt.ylabel("HPV Infected cases")
        plt.savefig("e"+ str(j)+"_vaccine_vs_nonvaccine_run" + str(i)+".pdf") 
        plt.close()
        
        datos2=run.filter(['infected','sane']).cumsum().max()
        datos2.plot(kind='bar',grid=[])
        plt.title("Experiment "+ str(j)+"  Run " + str(i)) 
        #plt.xticks(a,b)
        plt.xlabel("Infected and sane")
        #plt.yticks(c,d)
        plt.ylabel("People")
        plt.savefig("e"+ str(j)+"_infected_vs_sane_run" + str(i)+".pdf") 
        plt.close()

        datos3=run.filter(['step','vaccinated','v0','v1'])
        datos3=datos3.loc[datos3['step']<1352]
        datos3=datos3.interpolate(method='polynomial',order=5)
        datos3.plot(x='step',y=['vaccinated','v0','v1'],logy=True,grid=[])
        plt.title("Experiment "+ str(j)+"  Run " + str(i)) 
        plt.xticks(g,h)
        plt.xlabel("Years")
        #plt.yticks(c,d)
        plt.ylabel("Population")
        plt.legend(('vacinated','non-vaccine virus','vaccine-virus'),loc='upper right', shadow=True, fancybox=True ,framealpha=1,fontsize='small')
        plt.savefig("e"+ str(j)+"_infected_and_vaccinated_run_logy" + str(i)+".pdf")

        plt.close()

 #       datos3=run.filter(['step','vaccinated','v0','v1'])
        datos3=datos3.loc[datos3['step']<1352]
        datos3=datos3.interpolate(method='polynomial',order=5)
        datos3.plot(x='step',y=['vaccinated','v0','v1'],grid=[])
        plt.title("Experiment "+ str(j)+"  Run " + str(i)) 
        plt.xticks(g,h)
        plt.xlabel("Years")
        plt.yticks(e,f)
        plt.ylabel("Population (%)")
        plt.legend(('vacinated','non-vaccine virus','vaccine-virus'),loc='upper right', shadow=True, fancybox=True ,framealpha=1,fontsize='small')
        plt.savefig("e"+ str(j)+"_infected_and_vaccinated_run" + str(i)+".pdf") 
        plt.close()

        datos3=run.filter(['vaccinated','v0','v1'])
        datos3.plot(subplots=True,colormap='winter',grid=[])
        plt.title("Experiment "+ str(j)+"  Run " + str(i)) 
        #plt.xticks(a,b)
        plt.xlabel("Weeks")
       # plt.yticks(c,d)
        plt.ylabel("Population")
        plt.savefig("e"+ str(j)+"_infected_and_vaccinated_run_subplots" + str(i)+".pdf")
        plt.close()










