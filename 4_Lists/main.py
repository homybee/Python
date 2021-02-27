"""
Python Easy - Homework 4
Lists
"""
# Creatiing a global Variable list "myUniqueList"

myUniqueList = [ ]      #store unique values
myLeftovers = [ ]       #store duplicate values


# Creating a function to add values

def addData(text):
    #condition if value is not in the list
    if text not in myUniqueList: 
    # output is add the value to the list       
        myUniqueList.append(text)
        print(True)
    #condition if value is in list
    elif text in myUniqueList:
    # output is add value to a different list
        myLeftovers.append(text)
        print(False)

#Testing scenarios
#unique values
addData(4)      
addData(5)
addData(5) # Duplicate value
addData(6)
addData("Kofi")
addData(4) # Duplicate value

#printing all the lists
print(myUniqueList)
print(myLeftovers)



