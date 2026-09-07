import csv


def average_score(filename):
    score_list = []
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            score = float(row["score"])
            score_list.append(score)

    if not score_list:
        return 0.0

    return sum(score_list)/len(score_list)


def main():
    user_file = input("File name: ")
    try: 
        score = average_score(user_file)
        print(f"Average Score: {score:.2f}")
    except FileNotFoundError:
        print("Error: File not found.")


if __name__ == "__main__":
    main()
