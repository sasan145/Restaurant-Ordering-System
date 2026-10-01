from menu import Menu
from restaurant import Restaurant

def main():
    # FIX: Instantiate Menu() instead of passing the class itself
    restaurant = Restaurant(Menu())

    print("==============================")
    print("     WELCOME TO OUR SHOP")
    print("==============================")

    restaurant.display_menu()

    answer = input("\nWould you like to place an order? (yes/no): ").lower()

    if answer == "no":
        print("Thank you for visiting!")
        return

    restaurant.take_order()

    discount_answer = input("\nAre you a Senior Citizen or PWD? (yes/no): ").lower()

    discount = 0.20 if discount_answer == "yes" else 0.00

    restaurant.print_receipt(discount)

if __name__ == "__main__":
    main()