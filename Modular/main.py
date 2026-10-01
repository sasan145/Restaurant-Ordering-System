from menu import MENU
from ordering import take_customer_orders
from display import (
    print_welcome,
    print_menu,
    print_goodbye,
    print_message,
    print_receipt
)
from validation import get_valid_yes_no


def main():
    """Main program flow controller."""

    print_welcome()
    print_menu(MENU)

    wants_to_order = get_valid_yes_no(
        "\nWould you like to place an order? (yes/no): "
    )

    if not wants_to_order:
        print_goodbye()
        return

    customer_orders = take_customer_orders(MENU)

    print_message("\n--- Discount Application ---")

    is_senior_or_pwd = get_valid_yes_no(
        "Are you a Senior Citizen or PWD? (yes/no): "
    )

    discount = 0.20 if is_senior_or_pwd else 0.00

    print_receipt(customer_orders, discount)


if __name__ == "__main__":
    main()
