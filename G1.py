
def show_menu():
    print("\n--- SHOPPING LIST MENU ---")
    print("1. View List")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Clear List")
    print("5. Exit")

def main():
    shopping_list = []

    while True:
        show_menu()
        choice = input("\nChoose an option (1-5): ")

        if choice == '1':
            if not shopping_list:
                print("\nYour list is empty.")
            else:
                print("\nYour Current List:")
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item['name']} - Quantity: {item['quantity']}")

        elif choice == '2':
            item_name = input("Enter the item to add: ").strip()

            if item_name:
                try:
                    quantity = int(input("Enter quantity: "))

                    if quantity > 0:
                        shopping_list.append({
                            "name": item_name,
                            "quantity": quantity
                        })

                        print(f"'{item_name}' (Qty: {quantity}) added to the list.")
                    else:
                        print("Quantity must be greater than 0.")

                except ValueError:
                    print("Please enter a valid number for quantity.")

            else:
                print("Item name cannot be empty.")

        elif choice == '3':
            if not shopping_list:
                print("Nothing to remove.")
                continue
