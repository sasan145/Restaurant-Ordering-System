class Restaurant:
    def __init__(self, menu):
        self.menu = menu
        self.orders = []

    def display_menu(self):
        # FIX: Delegate to the Menu class's display_menu method
        # instead of incorrectly treating the Menu object as a dict
        self.menu.display_menu()

    def take_order(self):
        while True:
            item_choice = input("\nEnter Item No: ").strip()

            # FIX: Check against self.menu.items dictionary
            if item_choice not in self.menu.items:
                print("Item number not found.")
                continue

            # FIX: Retrieve the MenuItem object
            item = self.menu.get_item(item_choice)

            while True:
                try:
                    # FIX: Access object attributes (item.name) instead of dict keys (item['name'])
                    qty = int(
                        input(f"How many {item.name}(s) would you like? ")
                    )

                    if qty <= 0:
                        print("Quantity must be 1 or more.")
                    else:
                        break

                except ValueError:
                    print("Please enter a whole number.")

            self.orders.append({
                "name": item.name,      # FIX: Use attribute access
                "price": item.price,    # FIX: Use attribute access
                "qty": qty
            })

            another = input("Would you like to order another item? (yes/no): ").lower()

            if another == "no":
                break

    def print_receipt(self, discount=0):
        print("\n========== RECEIPT ==========")

        subtotal = 0

        for order in self.orders:
            total = order["price"] * order["qty"]
            subtotal += total

            print(f"{order['name']} x {order['qty']} = ₱{total:.2f}")

        discount_amount = subtotal * discount
        final_total = subtotal - discount_amount

        print("-----------------------------")
        print(f"Subtotal: ₱{subtotal:.2f}")
        print(f"Discount: ₱{discount_amount:.2f}")
        print(f"Total:    ₱{final_total:.2f}")