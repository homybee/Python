#Defining Functions
# General Format of Function

#def FunctionName(Input): # input is what you want to execute
#    Action               # The details of execution
#    return Output        # The output

#FunctionName()          |# this is at the end of the function but a line come before it

def addOne(Number):
    Number = Number + 1
    return Number


#Var = 15
#print(Var)
Var2 = addOne(2.5)
print(Var2)

def addOneAddTwo(Number1, Number2):
    Number1= Number1 + 1
    Price = Number1 * Number2
    return Price

Price = addOneAddTwo(5,10)
print(Price)
