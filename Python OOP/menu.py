class MenuItem:
    def __init__(self, item_no, name, price):
        self.item_no = item_no
        self.name = name
        self.price = price

class Menu:
    def __init__(self):
        self.items = {
            "1": MenuItem("1", "Cheeseburger", 100),
            "2": MenuItem("2", "Chicken Burger", 120),
            "3": MenuItem("3", "French Fries", 60),
            "4": MenuItem("4", "Soft Drink", 40)
        }

    def display_menu(self):
        print("\n========== MENU ==========")

        for item in self.items.values():
            # FIX: Corrected broken f-string concatenation and added spacing
            print(f"{item.item_no}. {item.name} - ₱{item.price:.2f}")

    def get_item(self, item_no):
        return self.items.get(item_no)