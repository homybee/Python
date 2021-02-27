# Loops
# For loop
""" Structure of For Lopp
for x in Hello
    print(x)
"""
word = "hello"
letters = [ ]

for x in word:
    print(x)
    if x == "e":
        print("Letter e found")
    
    letters.append(x)

print(letters)

for l in letters:
    print(l)

Numbers = [1, 2, 3, 4, 5]

for n in Numbers:
    if n%2 == 1:
        print("Odd number")
        letters.append(n)
    print(n)
print(letters)

lotto = [ ]
for num in range(5,15):
    lotto.append(num)
    print(num)
print(lotto)