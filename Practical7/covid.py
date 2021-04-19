#The code for importing the .csv file works
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("/Users/caishuo/Desktop/IBI1_2020-21/pratical7")
covid_data = pd.read_csv("full_data.csv")

#There is correct code for showing all columns, and every second row between (andincluding) 0 and 10
covid_data.iloc[0:12:2, :]

#You have successfully used a Boolean to show “total cases” for all rows corresponding to Afghanistan.
covid_data.loc[covid_data.loc[:,"location"] == "Afghanistan", 'total_cases']

#You have correctly computed the mean and median of new cases for the entire world.
np.mean(covid_data.loc[covid_data.loc[:,"location"] == "World", 'new_cases'])
np.median(covid_data.loc[covid_data.loc[:,"location"] == "World", 'new_cases'])

#You have successfully created a boxplot of new cases worldwide.
boxprops = dict(color  = 'lightblue',facecolor = 'paleturquoise', linewidth=2.0)
medianprops = dict(linestyle='-.', linewidth=2.0, color='teal')
capprops = dict(color = 'teal', linewidth=2.0)
whiskerprops = dict(color = 'lightblue', linewidth=2.0)
labels = ['new cases worldwide']
#plot
fig, ax = plt.subplots()
ax.boxplot(covid_data.loc[covid_data.loc[:,"location"] == "World", "new_cases"],
    patch_artist=True,
    boxprops = boxprops,
    medianprops = medianprops,
    capprops = capprops,
    whiskerprops = whiskerprops,
    labels = labels)
ax.set_title('World New Cases',fontsize=20)
# names for axes
for ax in [ax]:
    ax.set_ylabel('case distribution')

# horizontal grid
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
               alpha=0.5)

plt.show()

#You have successfully plotted both new cases and new deaths worldwide.
world_dates = covid_data.loc[covid_data.loc[:,'location'] == "World", 'date']
world_new_cases = covid_data.loc[covid_data.loc[:,'location'] == "World", 'new_cases']
plt.figure(figsize=(7,7))
plt.plot(world_dates, world_new_cases, 'b+')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
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
ax1 = fig.add_axes([0.13,0.17,0.8,0.75])
ax1.plot(world_dates, Spain_new_cases, 'b+', label = 'Spain_new_cases')
ax1.plot(world_dates, Spain_total_cases, 'r+', label = 'Spain_total_cases')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
ax1.set_ylabel('number')
ax1.set_xlabel('date')
ax1.set_title('development of new cases and total cases in Spain')

ax1.legend()
plt.show()
