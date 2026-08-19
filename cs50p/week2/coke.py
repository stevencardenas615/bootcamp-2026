def main():
    amount_due = 50
    coin = 0

    while amount_due > 0:
        print("Amount Due:",amount_due)

        coin = int(input("Insert Coin: "))

        if coin in [25, 10, 5]:
            amount_due = amount_due - coin

    if amount_due <= 0:
        print("Change owed:",abs(amount_due))

main()
