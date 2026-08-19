def main():
    available_foods = {
        "apple": "Calories: 130",
        "avocado": "Calories: 50",
        "sweet cherries": "Calories: 100",
        "banana": "Calories: 110",
        "kiwifruit": "Calories: 90",
        "pear": "Calories: 100"
        }
    selection = input("Item: ").lower().strip()

    if selection in available_foods:
         print(available_foods[selection])

main()
