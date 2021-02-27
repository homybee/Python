#Python is Easy - Homework 5.2
# Dictionaries and Sets

#Atributes of My Favourite Song
# ================================

#Declaring Variables of Dictionary
SongAttrib = {"Title" : "Money, Money, Money", "Album" : "ABBA", "Released Date" : "1 November 1976", "Genre" : "Baroque Pop" , "Lenght" : "3:05" , "Songwriters" : " Benny Andersson, Björn Ulvaeus", "Producers" : "Benny Andersson, Björn Ulvaeus"}

# Printing all attributes in a single loop
for key, value in SongAttrib.items():
	print(key, ':' ,value)  

# Creating function to accept Key and Value
#Function example 1

def GuessSong():
        #Converting variables to string
	    Key = str(input ("Enter the key:-  "))
	    Value = str(input ("Enter the value:-  "))

	    print("*****Guessing Game****\n")
        #Condition if key matches value
	    if SongAttrib.get(Key) == Value:
		    print("match found")
	    else:
		    print("No match found")


GuessSong()

# Function example 2
def GuessSong1(Key,Value):
	    print("*****Guessing Game****\n")
	    if SongAttrib.get(Key) == Value:
		    print("match found")
	    else:
		    print("No match found")

GuessSong1("Album", "ABBA")
GuessSong1("Title", "ABBA")
