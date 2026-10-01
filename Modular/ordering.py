from display import print_message, print_error
from validation import get_valid_yes_no


def take_customer_orders(menu_dict):
    """Handles the loop of getting the menu item and quantity from the user."""

    orders = []
    is_ordering = True

    while is_ordering:
        print_message(
            "\nPlease type the item number (e.g., '1' for Cheeseburger)"
        )

        item_choice = input("Enter Item No: ").strip()

        if item_choice not in menu_dict:
            print_error("Item number not found on the menu. Please try again.")
            continue

        while True:
            try:
                item_name = menu_dict[item_choice]['name']

                qty = int(
                    input(f"How many {item_name}(s) would you like? ")
                )

                if qty <= 0:
                    print_error("Quantity must be 1 or more.")
                else:
                    break

            except ValueError:
                print_error(
                    "Invalid input. Please enter a whole number."
                )

        orders.append({
            'name': menu_dict[item_choice]['name'],
            'price': menu_dict[item_choice]['price'],
            'qty': qty
        })

        is_ordering = get_valid_yes_no(
            "\nWould you like to order another item? (yes/no): "
        )

    return orders
