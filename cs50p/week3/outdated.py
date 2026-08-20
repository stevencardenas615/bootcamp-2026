months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
def main():
        while True:
            try:
                user_date = input("Date: ").strip()
                if "/" in user_date:
                    user_date = user_date.split("/")
                    if int(user_date[0]) > 12 or int(user_date[1]) > 31:
                        raise ValueError
                    print(f"{user_date[2]}-{int(user_date[0]):02}-{int(user_date[1]):02}")
                    return
                elif user_date[0].isalpha():
                    user_date = user_date.split()
                    if "," not in user_date[1]:
                        raise ValueError
                    elif int(user_date[1].strip(",")) > 31:
                        raise ValueError
                    else:
                        user_date[0] = months.index(user_date[0]) + 1
                        print(f"{user_date[2]}-{user_date[0]:02}-{int(user_date[1].strip(",")):02}")
                        return
                else:
                    pass
            except (ValueError, IndexError):
                pass

main()
