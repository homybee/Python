# Python is Easy - Homework 5.2
# Advanced Loops

# creating a function draw_board

def draw_board(rows,columns):
    # setting variables to innteger
    rows = int(rows) 
    columns = int(columns)

    if rows <= 21 and columns <= 254:  # condition if input is within heaight and lenght
        
        #for loop to print shape
        for r in range(rows):
            if r % 2 == 0:
                for l in range(1, columns):
                    if l%2 == 1:
                        if l != columns - 1: 
                            print(" ", end="")
                        else:
                            print(" ")
                    else:
                        print("|", end="")
            else:
                print("-" * columns)
        return True # condition if the size iss within lenght and height range
    else: # condition if its not within range
        print("rows should not be higher than 21")
        print("colums should not be higher than 254")
        return False


draw_board("19",200)  #function can convert string values to integers


