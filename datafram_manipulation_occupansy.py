# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 17:16:25 2021



__author__ = "Harald Norvald Stabbetorp"
__email__ = "harald.norvald.stabbetorp@nmbu.no"""

#Del 1

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



def csv_til_liste(filnavn, header=0):
    df = pd.read_csv(filnavn) # bruker pandas til å lese inn filen
    dl = df.values.tolist() # gjør om til en liste
    return df, dl




# Del 2

def tid_siden_midnatt(liste):
    timer = []#oppretter 2 tomme lister
    minutter = []
    for line in dl: # for at den skal gå igjennom alle verdiene
        columns = line
        time = columns[1] # finner plasseringen til timer
        time = time[-8:-6] # finner verdiene til timer
        minu = columns[1] # finner plasserngen til timer
        minu = minu[-5:-3] # finner verdeinen for minutter og timer
        eksakt = int(time)*60 # ganger antall timer med 6 for å finne minutter
        minu = int(minu)+eksakt # plusser de sammen for å finne nøyaktige minutter
         
        timer.append(time) # legger de i den tomme lista
        minutter.append(minu) # legger det i den tomme lista
    
    return timer, minutter

"""
Brukte dette for å sjekke den største og minste veriden
minutter.sort()

x = minutter[:1]
y = minutter[-1:]
"""

#Del 3

def hent_kolonner(dataframe, kolonne1, kolonne2, lagPlott = True):
    df = dataframe
    k1 = df[kolonne1].to_numpy() #finner kolonne og gjør den om til en numpy array
    k2 = df[kolonne2].to_numpy() #finner kolonne og gjør den om til en numpy array
    
    
    n = len(df) #finner lengden til dataframen
    
    cr = list(range(n)) #finner alle de ulike verdiene i dataframen
    
    if lagPlott == True:
        plt.figure() # gir et nytt plott
        plt.scatter(k1,k2,c=cr) #lager scatterplot
        plt.colorbar() #legger til en colorbar
        plt.xlabel(kolonne1) #gir navn til x-aksen
        plt.ylabel(kolonne2) # gir navn til y-aksen
        plt.savefig('array.png') #lagrer grafen som en som et bilde
    
    return k1, k2 


if __name__=="__main__":
    
    #Del 1
    df, dl = csv_til_liste('occupancy.csv') 

    boxplot = df.boxplot(column=['Temperature'], by='Occupancy')
    plt.suptitle('')
    plt.savefig('boxplot.png')
    
    # Del 2
    timer, minutter = tid_siden_midnatt(dl)
    
    telle_t, ganger= np.unique(np.array(timer), return_counts= True) # teller opp hvor mange ganger målingene er tatt på forkjellige tidspunkt
    
    sortert = np.sort(ganger) #sorterer lista 
    sortert = sortert.tolist() #kovertere til en liste
    x = sortert[0] #finner den minste verdien
    ganger = ganger.tolist()
    
    #bruker en for løkke til å gå igjennom alle verdiene og indeksere når det ble tatt færrest målinger
    for y in range(len(ganger)):
        y = ganger.index(x)
        if y <= y:
            z = ganger.index(x,y+1)
    print('Det er færrest målinger ved disse tidpunktene',y,z )
            
    
    #Del 3
    
    k1, k2 = hent_kolonner(df, 'Humidity', 'CO2')
    
    

    
    
