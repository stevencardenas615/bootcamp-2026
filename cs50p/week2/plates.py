def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if 6 >= len(s) >= 2 and s.isalnum():
        if s[0:2].isalpha():
            if s[len(s)//2 : (len(s)//2) + 1] == "0":
                return False
            elif s[-1].isdigit() or s.isalpha():
                return True
        else:
            return False
    else:
        return False

main()
