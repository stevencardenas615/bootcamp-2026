def main():
    text = input("Input: ")
    short_text = shorten(text)
    print(short_text)

def shorten(word):
    new_text = ""

    for i in word:
        if i not in ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]:
            new_text += i
        else:
            continue

    return new_text

if __name__ == "__main__":
    main()
