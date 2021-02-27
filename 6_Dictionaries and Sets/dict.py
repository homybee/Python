#Atributes of My Favourite Song
# ================================

#Declaring Variables
SongAttrib = {"Title" : "Money, Money, Money", "Album" : "ABBA", "Released Date" : "1 November 1976", "Genre" : "Baroque Pop" , "Lenght" : "3:05" , "Songwriters" : " Benny Andersson, Björn Ulvaeus", "Producers" : "Benny Andersson, Björn Ulvaeus"}

for key, value in SongAttrib.items():
	print(key, ':' ,value)

def GuessSong(Key,Value):
		#Key = str(input ("Enter the key"))
		#Value = str(input ("Enter the value"))
		print("*****Guessing Game****\n")
		if SongAttrib.get(Key) == Value:
			return True
		else:
			print("Wrong match")
			
					
GuessSong("Album","ABBA")


