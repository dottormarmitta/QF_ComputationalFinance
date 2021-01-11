# © Guglielmo Del Sarto -> guglielmo.delsarto@outlook.com

# #
# I build the class:
# #

# In this exercise, I find convenient to build another class (so not just
# continent) which is able to represent a Country.

class Continent:

    def __init__(self, name, countries):
        """
        Continent has two parameters. A name and a list of Country

        For Country specification, please refer below!
        """
        self.name = name
        self.countries = countries

    def addCountry(self, name, capital, population):
        self.countries.append(Country(name, capital, population))

    def getCapital(self, nameOfCountry):
        for currentCountry in self.countries:
            if currentCountry.getName() == nameOfCountry:
                return currentCountry.getCapital()
        return "Country not found!"
    
    def getTotalPopulation(self):
        totalPop = 0
        for currentCountry in self.countries:
            totalPop += currentCountry.getPopulation()
        return totalPop

    def getCountriesWithG(self):
        nationG = []
        for currentCountry in self.countries:
            if currentCountry.getName()[0] == 'G':
                nationG.append(currentCountry.getName())
        return nationG

class Country:

    # Constructor. Every CLASS has to have this method. An object of type
    # Country is built via this method. In order to build object of type
    # country, one has to do:
    # nameOfCountry = Country("StringWithName", "StringWithCap", population)
    def __init__(self, name, capital, population):
        self.name = name
        self.capital = capital
        self.population = population

    # EVERY object of type Country is able to perform the following
    # methods:
    def getName(self):
        return self.name

    def getCapital(self):
        return self.capital
    
    def getPopulation(self):
        return self.population
    

# #
# Part 2: some testing 
# #
Italy = Country("Italy", "Rome", 60000000)
France = Country("France", "Paris", 70000000)
Germany = Country("Germany", "Berlin", 85000000)
Europe = Continent("Europe", [Italy, France, Germany])
print(Europe.getTotalPopulation())
print(Europe.getCapital("Italy"))
print()
# I want to add a country (which is a class I created)
print(Europe.getCapital("Portugal"))
Europe.addCountry("Portugal", "Lisbon", 30000000)
print(Europe.getCapital("Portugal"))
print(Europe.getCountriesWithG())

America = Continent("America", [])
