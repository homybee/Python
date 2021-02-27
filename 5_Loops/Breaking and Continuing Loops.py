# Breaking and Continuing in Loops

# participant = ["Kofi", "Ama", "Yaw", "Afia", "Akwasi"]

# position = 1

# for name in participant:
#         if name == ("Kofi"):
#             print( "Index = " + str(participant.index("Kofi") ))
#             print("participant name = " + name)
#             break
#         position = position + 1

# print("Position = " + str(position))

Multiples_of_3 = [ ]
for num in range(22):
    if num%3 == 0:
        Multiples_of_3.append(num)
        print(num)
        continue
     
print(Multiples_of_3)

"""X = "abcd"
for i in range(len(X)):
    print(i)"""