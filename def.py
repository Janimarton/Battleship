def input_func(player, coordinate):
    while True:
        try:
            x = int(input(str(player) + " give me your ships" + coordinate + " position!"))
            if ((x > 5) or x < 1):
                raise ValueError
            else:
                break
        except ValueError:
            print("Enter a number between 1 and 5!")
            return(x)


print(input_func("Kristof", " X "))
