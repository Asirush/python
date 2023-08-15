def drow_line(length, direction, symbol):
    for i in length:
        if direction=="horizontal":
            print(symbol)
        else:
            for j in length:
                print(symbol + '\n')
                
if "___main____" == __name__:
    drow_line(5, "horizontal", "A")