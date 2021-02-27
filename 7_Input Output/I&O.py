# Dictionaries

TargetCities = ["London", "Paris", "New York", "Utah", "Iceland" ]

CitiesFile = open("TargetedCities", "w")

for cities in TargetCities:
    CitiesFile.write(cities + "\n" )

CitiesFile.close()

new = "Thailand \n"
new1 = "Ghana \n"
new2 = "Togo \n"
new3 = "Canada"
with open ("TargetedCities", "a") as  CitiesFile:
    CitiesFile.write(new )
    CitiesFile.write(new1)
    CitiesFile.write(new2)
    CitiesFile.write(new3)
    
with open("TargetedCities", "r") as  CitiesFile:
    for line in CitiesFile:
        print(line, end = "")






# TheWholeFile = CitiesFile.read()

# print(TheWholeFile)

#print("done")