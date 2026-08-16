def main():
    answer = input("What is the Answer to the Great Question of Life, the Unverse, and Everything? ").strip().lower()

    match answer:
        case "42" | "forty-two" | "forty two":
            return print("Yes")
        case _:
            return print("No")

main()
