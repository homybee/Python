# Python Easy - Homework 3
# If statements

def avCalc (x,y,z):         # definition of function 
#Declaring and converting variables in integers
    x = int(x)
    y = int(y)
    z = int(z)
                  
#printing variables
    print(x)                
    print(y)
    print(z)

#if conditions
    if x == y or x == z or y == z:      #condition if two values are equal
        print(True)                     #out True
    
    elif x == y and x == z and y == z:  #Condition is all values are equal
        print(True)
        
    else: print(False)                  #Condition if none of the values are equal

#Calling functions

avCalc(2,"3",1)                 
avCalc("4",4,"4")