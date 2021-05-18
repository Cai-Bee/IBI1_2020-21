#The code for importing the .csv file
import os
#sys is used for getting the directory of this file
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#The following sentence works when the whole cript work.
#(Even the code are download to another conputer, this command can change working directory to where this py file are)
os.chdir(sys.path[0])
#The following sentence works when typing commands directly to my terminal.
os.chdir("/Users/caishuo/github/IBI1_2020-21/Practical7")
covid_data = pd.read_csv("full_data.csv")

#There is correct code for showing all columns, and every second row between (andincluding) 0 and 10
table1 = covid_data.iloc[0:12:2, :]
print("\n>all columns, and every second row between (andincluding) 0 and 10")
print(table1)

#used a Boolean to show “total cases” for all rows corresponding to Afghanistan.
table2 = covid_data.loc[covid_data.loc[:,"location"] == "Afghanistan", 'total_cases']
print("\n>total cases” for all rows corresponding to Afghanistan")
print(table2)

#computed the mean and median of new cases for the entire world.
world_new_cases = covid_data.loc[covid_data.loc[:,"location"] == "World", 'new_cases']
mean = str(np.mean(world_new_cases))
median = str(np.median(world_new_cases))
print("\n>the mean and median of new cases for the entire world are respectively "+mean+" and "+median)

#created a boxplot of new cases worldwide.
boxprops = dict(color  = 'lightblue',facecolor = 'paleturquoise', linewidth=2.0)
medianprops = dict(linestyle='-.', linewidth=2.0, color='teal')
capprops = dict(color = 'teal', linewidth=2.0)
whiskerprops = dict(color = 'lightblue', linewidth=2.0)
labels = ['new cases worldwide']
    #plot
fig1 = plt.figure()
ax1 = fig1.add_subplot(1,1,1)
ax1.boxplot(covid_data.loc[covid_data.loc[:,"location"] == "World", "new_cases"],
    patch_artist=True,
    boxprops = boxprops,
    medianprops = medianprops,
    capprops = capprops,
    whiskerprops = whiskerprops,
    labels = labels)

ax1.set_title('World New Cases',fontsize=20)
    # names for axes
ax1.set_ylabel('case distribution')
    # horizontal grid
ax1.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
plt.show()

#plotted both new cases and new deaths worldwide.
world_dates = covid_data.loc[covid_data.loc[:,'location'] == "World", 'date']
world_new_cases = covid_data.loc[covid_data.loc[:,'location'] == "World", 'new_cases']
world_new_deaths = covid_data.loc[covid_data.loc[:,'location'] == "World", 'new_deaths']
fig2 = plt.figure(figsize=(7,7))
ax2 = fig2.add_axes([0.11,0.20,0.8,0.70])
plt.plot(world_dates, world_new_cases, 'b.', label = 'world_new_cases')
plt.plot(world_dates, world_new_deaths, 'r+', label = 'world_new_deaths')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.title("new cases and new deaths worldwide")
plt.xlabel("date")
plt.ylabel("number")
plt.legend()
plt.show()

#There is code to answer the question stated in file question.txt
#Question： How have new cases and total cases developed over time in Spain?
#The code to answer the question runs without errors
#The code to answer the question does what it is meant to do
#All plots are clearly labelled
world_dates = covid_data.loc[covid_data.loc[:,'location'] == "World", 'date']
Spain_new_cases = covid_data.loc[covid_data.loc[:,"location"] == "Spain",'new_cases']
Spain_total_cases = covid_data.loc[covid_data.loc[:,"location"] == "Spain",'total_cases']
fig = plt.figure(figsize=(7,7))
ax3 = fig.add_axes([0.13,0.17,0.8,0.75])
ax3.plot(world_dates, Spain_new_cases, 'c^', label = 'Spain_new_cases')
ax3.plot(world_dates, Spain_total_cases, 'mv', label = 'Spain_total_cases')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
ax3.set_ylabel('number')
ax3.set_xlabel('date')
ax3.set_title('development of new cases and total cases in Spain')
plt.xlabel("date")
plt.ylabel("number")
ax3.legend()
plt.show()
