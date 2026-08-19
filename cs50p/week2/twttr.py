def main():
    text = input("Input: ")
    new_text = ""

    for i in text:
        if i not in ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]:
            new_text += i
        else:
            continue

    print("Output:",new_text)

main()
