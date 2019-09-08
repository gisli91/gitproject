years = int(input("Years: "))

# Birth every 7 seconds, immigration every 35 seconds and a death every 13 seconds

#Here are my variables which I'll use as a starting point for this project, I.e the current population

base_population = 307357870


#here are the calculations for population increase/decrease per year

popultion = 0

births = (86400 / 7) * 365
immigration = (86400 / 35) * 365
deaths = (86400 / 13) * 365 

#Here I modify the population with the given parameters if the given years are eaqual to or greather than 0

if years >= 0:
    popultion = int(base_population + (births * years) + (immigration * years) - (deaths * years))
    print("New population after", years, "years is", popultion)

else:
    print("Invalid input!")

