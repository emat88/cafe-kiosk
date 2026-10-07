# Byte & Brew - Self-Service Kiosk

total_bill = 0.00

while True:
    print("\n--- Byte & Brew Menu ---")
    print("1. Black Coffee - $2.50")
    print("2. Vanilla Latte - $4.00")
    print("3. Blueberry Muffin - $3.00")
    print("4. Complete Order (Checkout)")

    user_input = input("Enter your selection (1-4): ").strip()

    # Reject anything that is not a whole number so int() cannot crash
    if not user_input.isdigit():
        print("Invalid selection. Please choose a valid menu item.")
        continue

    choice = int(user_input)

    if choice == 1:
        total_bill += 2.50
        print(f"Added Black Coffee. Current total: ${total_bill:.2f}")
    elif choice == 2:
        total_bill += 4.00
        print(f"Added Vanilla Latte. Current total: ${total_bill:.2f}")
    elif choice == 3:
        total_bill += 3.00
        print(f"Added Blueberry Muffin. Current total: ${total_bill:.2f}")
    elif choice == 4:
        print(f"Order complete. Your final total is: ${total_bill:.2f}")
        print("Thank you for visiting Byte & Brew!")
        break
    else:
        print("Invalid selection. Please choose a valid menu item.")
