# TicTac 

def drawField():
    for i in range(5):
        if i%2 == 0:
            for c in range(5):
                if c!= 4:
                    if c%2 == 0:
                        print(" ", end = "")
                    else:
                        print("|", end = "")
                else:
                    print(" ")
        else:
            print("-" * 5)


drawField()
