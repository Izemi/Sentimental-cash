def main():
    # Continuously ask the user for the total amount they need to pay
    while True:
        try:
            change_owed = float(input("Enter the total amount owed: "))
            if change_owed >= 0:
                break
            else:
                print("Please ensure the total amount owed is non-negative.")
        except ValueError:
            print("Invalid input. Ensure you enter a non-negative number.")

    # Convert the dollar amount to cents and round to the nearest penny
    cents_owed = round(change_owed * 100)

    # Initialize counters for each type of coin
    num_quarters = 0
    num_dimes = 0
    num_nickels = 0
    num_pennies = 0

    # Determine the quantity of each coin needed
    while cents_owed >= 25:
        num_quarters += 1
        cents_owed -= 25
    while cents_owed >= 10:
        num_dimes += 1
        cents_owed -= 10
    while cents_owed >= 5:
        num_nickels += 1
        cents_owed -= 5
    num_pennies = cents_owed

    # Display the total count of coins to give as change
    total_coins = num_quarters + num_dimes + num_nickels + num_pennies
    print(total_coins)


# Execute the main program to calculate change
main()
