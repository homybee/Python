for i in range(5):
    if i%2 == 0:
        for c in range(5):
            if c%2 == 0:
                if c !=4:
                    print(" ", end="")
                else:
                    print(" ") 
            else:
                print("|", end="")
    else:
        print("------")

