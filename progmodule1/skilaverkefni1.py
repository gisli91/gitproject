years = int(input("Years: "))

#base population, and base year 2019

base_population = 307357870
population = base_population

base_year = 2019




births = 0
deaths = 0
immigrants = 0

#Births per year
births = (86400 / 7) * 365

#Deaths per year
deaths = (86400 / 13) * 365

#Immigration per year
immigrants = (86400 / 35) * 365


if years > base_year:
    for x in range (base_year, years):
        population = population + births + immigrants - deaths 
if years < base_year:
    for x in range (base_year, years):
        population = population - births - immigrants + deaths

       


print(births, deaths, immigrants)
print(population)