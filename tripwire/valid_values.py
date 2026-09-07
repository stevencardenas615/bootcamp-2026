def sum_valid(values):
    total = 0.0
    for i in values:
        try:
            total += float(i)
        except ValueError:
            pass
    return total

def main():
    string_list = ["10", "abc", "3.5", "", "7"]
    total = sum_valid(string_list)
    print(total)

if __name__ == "__main__":
    main()