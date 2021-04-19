import matplotlib.pyplot as plt
#"countries"will be used at lebel in the pyplot
countries = ['USA', 'India', 'Brazil', 'Russia', 'UK']

#cases is the dictionary total number of cases for five countries
cases = {'USA':29862124, 'India':11285561, 'Brazil':11205972, 'Russia':4360823, 'UK':4234924}

#cauculate the total number of cases in these five countries
#'total' represents the total number of cases
total = 0
for country in(countries):
    case = cases[country]
    total += case

#record a frequency dictionary by deviding cases by total number
#'frequency' frpresent the frequency of these five countries
frequency = cases
sizes = []
for country in(countries):
    frequency[country] = cases[country]/total
    sizes.append(frequency[country])

#draw the pie plot
fig1, ax1 = plt.subplots(1,1)
ax1.pie(sizes, labels=countries, autopct='%1.1f%%',
        shadow=False, startangle=110)
ax1.set_title("percentage of coronavirus cases for fivecountries")
print(cases)
plt.show()
