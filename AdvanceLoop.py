
def PlayingBoard(rows, columns):
    max_columns = 100
    max_rows = 21
    rows = int(rows)
    columns = int(columns)
    if columns <= max_columns and rows <= max_rows:
        for row in range(rows):
            if row % 2 == 0:
                for col in range(1, columns):
                    if col % 2 == 1:
                        if col != columns - 1:
                            print(" ", end="")
                        else:
                            print(" ")
                    else:
                        print("|", end="")
            else:
                print("-" * columns)
        return True
    else:
        reason = ""
        if columns > max_columns and rows > max_rows:
            reason = "columns and rows"
        elif columns > max_columns:
            reason += "columns"
        elif rows > max_rows:
            reason += "rows"
        print("Sorry, cannot create the board")
        return False

PlayingBoard(20,100)