def main():
    text = input("cameCase: ")
    new_text = ""

    for i in text:
        if i.islower():
            new_text += i
        else:
            new_text += "_" + i

    print("snake_case:",new_text.lower())

main()
