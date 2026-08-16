def main():
    greeting  = input("Greeting: ").strip().lower()

    if greeting.startswith("hello"):
        return print("$0")
    elif greeting.startswith("h"):
        return print("$20")
    else:
        return print("$100")

main()
