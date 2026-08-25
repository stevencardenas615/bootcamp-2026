import random

LEVEL = [1, 2, 3]

def main():
    level = get_level()
    num_errors = 0
    num_correct = 0

    for i in range(10):
        num_tries = 1
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y

        while num_tries <= 4:
            if num_tries == 4:
                num_errors = num_errors + 1
                print(f"{x} + {y} = {answer}")
                break
            else:
                try:
                    user_answer = int(input((f"{x} + {y} = ")))
                    if user_answer == answer:
                        num_correct = num_correct + 1
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("EEE")
                    num_tries = num_tries + 1
                    pass

    print(f"Score: {num_correct}")

def get_level():
    while True:
        try:
            user_choice = int(input("Level: "))

            if user_choice not in LEVEL:
                raise ValueError
            else:
                return user_choice
        except ValueError:
            pass

def generate_integer(level):
    if level not in [1, 2, 3]:
        raise ValueError
    if level == 3:
        return random.randint(100, 999)
    elif level== 2:
        return random.randint(10, 99)
    else:
        return random.randint(0, 9)


if __name__ == "__main__":
    main()
