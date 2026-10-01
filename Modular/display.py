def print_welcome():
    print("\n==============================")
    print("      WELCOME TO OUR SHOP")
    print("==============================")


def print_menu(menu):
    print("\n========== MENU ==========")

    for item_no, item in menu.items():
        print(f"{item_no}. {item['name']} - ₱{item['price']:.2f}")


def print_message(message):
    print(message)


def print_error(message):
    print(f"Error: {message}")


def print_goodbye():
    print("\nThank you for visiting!")
    print("Goodbye!")


def print_receipt(orders, discount):
    print("\n========== RECEIPT ==========")

    subtotal = 0

    for order in orders:
        item_total = order['price'] * order['qty']
        subtotal += item_total

        print(
            f"{order['name']} x {order['qty']} "
            f"= ₱{item_total:.2f}"
        )

    discount_amount = subtotal * discount
    total = subtotal - discount_amount

    print("-----------------------------")
    print(f"Subtotal: ₱{subtotal:.2f}")
    print(f"Discount: ₱{discount_amount:.2f}")
    print(f"Total:    ₱{total:.2f}")
    print("=============================")
