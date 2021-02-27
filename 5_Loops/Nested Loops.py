# Nested Loops
"""
for row in range(5):                 # a range of 0 -4
    if row%2 == 0:                   # 
        for column in range(1,6):   # range of 1 - 5v
            if column%2 == 1:
                if column != 5:
                    print(" ",end="")
                else:
                    print(" ")
            else:
                print("|",end="")
        #print(" | | ")
    else:
        print("-----")
"""

Length = 3                   
ToPrint = "a"                 
for pos in range(1, Length + 1): 
    print(ToPrint*pos)         
   
for pos in range(Length, 0, -1):
    print(ToPrint*pos)

"""
f = 1
A = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
for i in range(0, 3):
     f =f*i
     for j in range(0, 3):
         A[i][j] = f
print(A)
"""