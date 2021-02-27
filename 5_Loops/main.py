# Python Made Easy - Homework 5
# Loops

Set = [ ]
for num in range(1,100):       
    if num%3 == 0 and num%5 == 0:
        num = "FizzBuzz"
    elif  num%3 == 0:
        num = "Fiz"
    elif num%5 == 0 :
        num = "Buzz"
    elif num>1:
        for n in range(2,num):
            if num%n == 0 :
                break
        else:
            num = "prime"

    Set.append(num)

print(Set)
