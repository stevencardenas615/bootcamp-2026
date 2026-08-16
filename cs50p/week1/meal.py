def main():
    current_time = input("What time is it? ").strip()
    converted_time = convert(current_time)

    if 7 <= converted_time <= 8:
        print("breakfast time")
    elif 12 <= converted_time <= 13:
        print("lunch time")
    elif 18 <= converted_time <= 19:
        print("dinner time")

def convert(time):
    hour_str, min_str = time.split(":")

    hour = float(hour_str)
    min = float(min_str)

    return hour + (min/60)

if __name__ == "__main__":
    main()
