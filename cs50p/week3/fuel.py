def main():
    while True:
        try:
            tank = input("Fraction: ")
            x, y = tank.split("/")
            x = int(x)
            y = int(y)

            if x > y or x < 0:
                pass
            elif x / y >= 0.99:
                return print("F")
            elif x / y <= 0.01:
                return print("E")
            else:
                return print(round((x/y) * 100),"%", sep = "")

        except ValueError:
            pass
        except ZeroDivisionError:
            pass

main()
