import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    octet = r"([0-9]|[1-9][0-9]*)"
    pattern = rf"^{octet}\.{octet}\.{octet}\.{octet}$"
    match = re.search(pattern, ip.strip())

    if not match:
        return False

    for group in match.groups():
        if int(group) < 0 or int(group) > 255:
            return False

    return True

if __name__ == "__main__":
    main()
