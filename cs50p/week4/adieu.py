def main():
    names = []

    try:
        while True:
            x = input("Name: ")
            names.append(x)
    except EOFError:
        print("")
        if len(names) == 1:
            print("Adieu, adieu, to",names[0])
        elif len(names) == 2:
            print(f"Adieu, adieu, to {names[0]} and {names[1]}")
        else:
            farewell = "Adieu, adieu, to "
            for i in range(len(names)):
                n = names[i]
                if i == len(names) - 1:
                    farewell = farewell + "and " + n
                    print(farewell)
                    return
                else:
                    farewell = farewell + n + ", "
main()
