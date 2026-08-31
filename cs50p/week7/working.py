import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = r"^([0-9]{1,2})(?::([0-9]{2}))? (AM|PM) to ([0-9]{1,2})(?::([0-9]{2}))? (AM|PM)$"
    match = re.search(pattern, s.strip())

    if not match:
        raise ValueError

    h1, m1, p1, h2, m2, p2 = match.groups()

    if m1 is None:
        m1 = 0
    else:
        m1 = int(m1)

    if m2 is None:
        m2 = 0
    else:
        m2 = int(m2)

    h1 = int(h1)
    h2 = int(h2)

    if h1 < 1 or h1 > 12 or h2 < 1 or h2 > 12:
        raise ValueError
    if m1 < 0 or m1 > 59 or m2 < 0 or m2 > 59:
        raise ValueError

    if p1 == "PM" and h1 != 12:
        h1 = h1 + 12
    elif p1 == "AM" and h2 == 12:
        h2 = 0

    return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"

if __name__ == "__main__":
    main()
