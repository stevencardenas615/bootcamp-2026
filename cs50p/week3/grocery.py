def main():
    list = {}
    try:
        while True:

            selection = input("").upper()

            if selection in list:
                list[selection] = list[selection] + 1
            else:
                list[selection] = 1

    except EOFError:
        list = dict(sorted(list.items()))

        for selection in list:
            print(f"{list[selection]} {selection}")
        return

main()
