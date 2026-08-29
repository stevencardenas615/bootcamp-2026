import csv
import sys

def main():
    students = []
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                last, first = row["name"].split(",")
                first = first.strip()
                students.append({"first": first, "last": last, "house": row["house"]})

        with open(sys.argv[2], "w") as file:
            writer = csv.DictWriter(file, fieldnames = ["first", "last", "house"])
            writer.writeheader()
            for student in students:
                writer.writerow({"first": student['first'], "last": student['last'], "house": student['house']})

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

if __name__ == "__main__":
    main()
