# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 20:16:07 2023

@author: ashra
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def male_exp():
    '''Function creates a line plot which shows top 5 countries with life expectancy of male
    in different 4 decades.The argument is a data frame whichh is used to read csv file that 
    contains the life expectancy of male in five top countries.'''
    male_exp=pd.read_csv("C:/Users/ashra/OneDrive/projectexpendi/male_ependiture.csv")
    #plotting the line graphs                             
    plt.plot(male_exp['Country Name'], male_exp['1990'], label=1990, marker="o")
    plt.plot(male_exp['Country Name'], male_exp['2000'], label=2000, marker="o")
    plt.plot(male_exp['Country Name'], male_exp['2010'], label=2010, marker="o")
    plt.plot(male_exp['Country Name'], male_exp['2020'], label=2020, marker="o")
    #Displays the title and label for x and y axis.
    plt.xlabel("COUNTRY")
    plt.ylabel("LIFE EXPECTANCY")
    plt.title("LINE PLOT")
    #Displays the legend 
    plt.legend(loc='upper right', bbox_to_anchor=(1.3,1))
    #Displays grid in line plot
    plt.grid(zorder=0)
    plt.show()
    return

def female_exp():
    '''Function creates a bar plot which displays top 5 countries with life expectancy of female
    in different 4 decades.The argument is a data frame which is used to read csv file that
    contains the life expetancy of female in five top countries.'''
    female_exp=pd.read_csv("C:/Users/ashra/OneDrive/projectexpendi/female_expenditure.csv")
    #plotting bar graph
    plt.bar(female_exp['Country Name'] ,female_exp['2020'], label ='2020')
    plt.bar(female_exp['Country Name'], female_exp['1990'], label ='1990')
    #Displays the title and label for x and y axis
    plt.title("BAR PLOT")
    plt.xlabel("COUNTRY")
    plt.ylabel("LIFE EXPENTANCY FEMALE")
    #Displays the legend 
    plt.legend()
    #Displays the grid in bar plot
    plt.grid(zorder=0)
    plt.show()
    return 

 
def gdp_capita():
    '''Function creates pie chart which shows the GDP of top 5 countries of oldest and latest decade.
    The argument is a data frame which is used to read csv file that contains oldest and latest data.'''
    gdp=pd.read_csv("C:/Users/ashra/OneDrive/projectexpendi/GDP.csv")
    #creating sub plot with one row and two columns
    plt.subplot(1,2,1)
    #plotting the pie chart
    plt.pie(gdp['1990'], shadow=True, labels=gdp['Country Name'], autopct='%1.1f%%', startangle=90)
    plt.title("GDP OF 1990")
    plt.subplot(1,2,2)
    #Creating the partitioning for plots
    plt.pie(gdp['2020'], shadow=True, labels=gdp['Country Name'], autopct='%1.1f%%', startangle=90)
    #Displays the title of pie chart 
    plt.title("GDP OF 2020")
    #Displays the legend
    plt.legend(loc='upper right', bbox_to_anchor=(1.7,1))
    #Displays layout and adjust the space between subplot.
    plt.tight_layout()
    plt.show()            
    return


def all_life():
    '''Function creates a scatter plot which displays the average life expectancy of all including males and
    females of top 5 countries in different 4 decades.The argument which is used to read csv file which contains
    the life expectancy data.'''
    all_life=pd.read_csv("C:/Users/ashra/OneDrive/projectexpendi/all_life.csv")
    #Creating numpy arrays by slcicing elements 
    ind=np.array(all_life.iloc[0:1,4:])
    chn=np.array(all_life.iloc[1:2,4:])
    uk=np.array(all_life.iloc[2:3,4:])
    uae=np.array(all_life.iloc[3:4,4:])
    usa=np.array(all_life.iloc[4:5,4:])
    jpn=np.array(all_life.iloc[5:6,4:])
    #plotting scatter plot with the average values by accessing numpy array
    plt.scatter('INDIA', np.average(ind), label='INDIA', s=400)
    plt.scatter('CHINA', np.average(chn), label='CHINA', s=400)
    plt.scatter('UK', np.average(uk), label='UK', s=400)
    plt.scatter('UAE', np.average(uae), label='UAE', s=400)
    plt.scatter('USA', np.average(usa), label='USA', s=400)
    plt.scatter('JAPAN', np.average(jpn), label='JAPAN', s=400)
    #Displays the title and label for a and y axis
    plt.title("SCATTER PLOT")
    plt.xlabel("COUNTRY")
    plt.ylabel("AVERAGE LIFE EXPECTANCY ")
    #Displays the legend 
    plt.legend(loc='upper right', bbox_to_anchor=(1.4,1), labelspacing = 1.2)
    #creating grid in scatter plot
    plt.grid(zorder=0)
    plt.show()
    return

#Calling the functions
female_exp() 
male_exp()  
gdp_capita()
all_life()    