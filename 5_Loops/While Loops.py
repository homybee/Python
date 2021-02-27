# Loops
# While loops
"""
structure of while loop
while (Condition):
    action
    action1
    action2
"""
"""
counter = 1
Sum = 0
while (counter <= 100):
        print(counter)
        Sum = Sum + counter
        counter = counter + 1
print(Sum)
"""
Letters = [ "a","b","c","d","e"]
print(len(Letters))

index = 0
while (index < len(Letters)):
    print(index)
    print(Letters[index])
    index = index + 1

height = 5000
velocity = 50
times = 0

while (height > 250 ):
    height = height - velocity
    times = times + 1

print(height)
print(times)
