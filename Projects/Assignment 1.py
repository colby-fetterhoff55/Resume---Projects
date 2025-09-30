import time

# Simulated database of drivers (includes username followed by passowrd)
drivers = {"driver1": "password123", "driver2": "securepass"}

# Simulated orders (order ID followed by details)
orders = {
    101: {"customer": "John Doe", "items": ["Pizza", "Soda"], "address": "123 Main St", "price": 25.50},
    102: {"customer": "Jane Smith", "items": ["Pasta", "Water"], "address": "456 Elm St", "price": 18.75},
}

def login():
    """Handles driver login."""
    print("Welcome to Simply Delivery!")
    while True:
        username = input("Enter username: ") #asks the user to login to the database
        password = input("Enter password: ")
        if username in drivers and drivers[username] == password:
            print("Login successful!\n")
            return username
        else:
            print("Invalid credentials, please try again.")

def view_orders(): #function required to view current orders
    """Displays available orders."""
    print("Assigned Orders:")
    for order_id, details in orders.items():
        print(f"Order {order_id}: {details['items']} for {details['customer']} at {details['address']} - ${details['price']}")
    print()

def take_payment(): #does not actually take payments but mocks what the payment select screen looks like
    """Simulates payment processing."""
    order_id = int(input("Enter order ID to process payment: "))
    if order_id in orders:
        print(f"Processing payment for order {order_id}...")
        time.sleep(2)  # Simulate transaction delay
        print("Payment successful!\n")
        del orders[order_id]
    else:
        print("Invalid order ID.\n")

def clock_out(): #function which handels clocking in and out of the system
    """Handles clocking out and calculating earnings."""
    hours = float(input("Enter hours worked: "))
    tips = float(input("Enter total tips earned: "))
    wage = 15.00  # Assume $15/hr
    total_earnings = (hours * wage) + tips
    print(f"Shift Summary: Hours Worked: {hours}, Tips: ${tips}, Total Earnings: ${total_earnings}\n")
    print("Clocking out... Goodbye!")
    exit()

def main(): #main function with menu options
    """Main loop for user interaction."""
    user = login()
    while True:
        print("1. View Orders")
        print("2. Process Payment")
        print("3. Clock Out")
        choice = input("Select an option: ")
        
        if choice == "1":
            view_orders()
        elif choice == "2":
            take_payment()
        elif choice == "3":
            clock_out()
        else:
            print("Invalid option, try again.\n")

if __name__ == "__main__":
    main()