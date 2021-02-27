# Dictionaries and Sets

# Sets = { "a", "b", "c", "b", "c"}
# if "c" in Sets:
#     print("confirmed")

# print(Sets)

# NameList = [ ]
# for r in range(5):
#     Name = input("Please enter your name: ")
#     NameList.append(Name)

# print(NameList)

# NameSet = set(NameList)
# print(NameSet)

# if "a" in NameSet:
#     print("found")

# NameDictionary = { }
# for Name in NameList:
#     if Name in NameDictionary:
#         NameDictionary[Name]  += 1 
#     else:
#         NameDictionary[Name] = 1

# print(NameDictionary)


"""Blackshoes = {42:2, 41:3, 40:4, 39:1, 38:0}
print(Blackshoes)
while True:
    buysize = int(input("Select shoe size \n"))
    if not buysize in Blackshoes:
        print("size not available")
        continue
    if buysize <= 0:
        print("requested sound not found")
        break
    if Blackshoes[buysize] > 0:
        Blackshoes[buysize] -= 1
    else:
        print("Size  out of stock")
    print(Blackshoes)
"""

# dict = {}
# # dict[1] = 2
# dict['1'] = 4
# # dict[1] += 2
# count = 0

# for key in dict:
#     count += dict[key]

# print(count)


s = {"1","2","3","4","5"}
If 3 in s:
print("3")