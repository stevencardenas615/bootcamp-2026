from datetime import date
import inflect
import sys

p = inflect.engine()

def main():
    birth_date = input("Date of Birth: ")
    try:
        dob = date.fromisoformat(birth_date)
    except ValueError:
        sys.exit("Invalid date")

    print(get_minutes(dob, date.today()))

def get_minutes(birth, today):
    diff = today - birth
    minutes = diff.days * 24 * 60

    words = p.number_to_words(minutes, andword= "")
    return f"{words.capitalize()} minutes"


if __name__ == "__main__":
    main()
