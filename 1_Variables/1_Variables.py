# Variables - 9th April, 2020

# Creating  Global Variables

One = 1
Two = 2
Three = 3

print(One)
print(Two)
print(Three)

Two = 4 

print(One)
print(Two)
print(Three)

Decimal = 2.5
StringVar = "homy"

print(One)
print(Two)
print(Three)
print(Decimal)
print(StringVar)

#Creating Local Variables
def KofiFunction():
    newVar = "World"
    print(newVar)     #Local Variable, cannot be called outside function
    print(StringVar)  #Global Variable, can be called anywhere  
    return 

KofiFunction()

#Performing basic Calculations
Sum = One + Two  # One and Two already declared at the top
print(Sum)

One = One + 6
print(One)
Four = 4
Four = Four + 2
print(Four)
Two += 10
Sum = One + Two
print(Sum)




