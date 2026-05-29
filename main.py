import products
import store

def display_menu():
    """Displays the main selection menu."""
    print("\n   Store Menu")
    print("  -----------")
    print("1. List all products in Store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")

def handle_list_products(best_buy_store):
    """Handles showing all active products to the user."""
    all_products = best_buy_store.get_all_products()
    if not all_products:
        print("No active products available.")
        return
    for index, product in enumerate(all_products, start=1):
        print(f"{index}. ", end="")
        product.show()

def handle_total_quantity(best_buy_store):
    """Handles showing the total amount of items in store."""
    total_quantity = best_buy_store.get_total_quantity()
    print(f"Total amount in store: {total_quantity}")

def handle_order(best_buy_store):
    """Processes interactive user orders securely step by step."""
    all_products = best_buy_store.get_all_products()
    if not all_products:
        print("No products available to order.")
        return

    shopping_list = []
    print("\nTo finish the order, leave the product number empty and press Enter.")

    while True:
        handle_list_products(best_buy_store)
        product_choice = input("Which product # do you want? ").strip()

        if product_choice == "":
            break

        try:
            product_index = int(product_choice) - 1
            if product_index < 0 or product_index >= len(all_products):
                print("Error: Invalid product number.")
                continue

            chosen_product = all_products[product_index]
            quantity_str = input(f"Amount of {chosen_product.name}: ").strip()
            quantity = int(quantity_str)

            if quantity <= 0:
                print("Error: Quantity must be greater than 0.")
                continue

            shopping_list.append((chosen_product, quantity))
            print(f"Added {quantity}x {chosen_product.name} to shopping list.")

        except ValueError:
            print("Error: Please enter a valid number.")

    if not shopping_list:
        print("Order canceled.")
        return

    # Try-Except fängt Fehler wie unzureichenden Lagerbestand ab
    try:
        price = best_buy_store.order(shopping_list)
        print(f"Order cost: {price} dollars.")
    except ValueError as error:
        print(f"Order failed: {error}")

def start(best_buy_store):
    """Main menu loop dividing input processing into modular functions."""
    while True:
        display_menu()
        choice = input("Please choose a number: ").strip()

        if choice == "1":
            handle_list_products(best_buy_store)
        elif choice == "2":
            handle_total_quantity(best_buy_store)
        elif choice == "3":
            handle_order(best_buy_store)
        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("Error: Invalid choice. Please try again.")

def main():
    """Application setup and entrypoint."""
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250)
    ]
    best_buy = store.Store(product_list)
    start(best_buy)

if __name__ == "__main__":
    main()