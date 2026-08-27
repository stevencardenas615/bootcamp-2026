def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not (2 <= len(s) <= 6 and s.isalnum()):
        return False

    if not s[0:2].isalpha():
            return False

    has_num = False
    for letter in s:
        if letter.isdigit():
            if not has_num and letter == "0":
                return False
            has_num = True
        elif has_num and letter.isalpha():
            return False

    return True

if __name__ == "__main__":
    main()
