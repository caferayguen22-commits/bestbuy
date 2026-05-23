import products
import store

def start(best_buy_store):
    while True:
        print("\n   Store Menu")
        print("  -----------")
        print("1. List all products in Store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice == "1":
            all_products = best_buy_store.get_all_products()
            for product in all_products:
                product.show()

        elif choice == "2":
            total_quantity = best_buy_store.get_total_quantity()
            print(f"Total amount in store: {total_quantity}")

        elif choice == "3":
            all_products = best_buy_store.get_all_products()

            shopping_list = [(all_products[0], 1), (all_products[1], 2)]

            price = best_buy_store.order(shopping_list)
            print(f"Order cost: {price} dollars.")

        elif choice == "4":
            print("Goodbye")
            break

        else:
            print("Error: Invalid choice. Please try again.")

if __name__ == "__main__":
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250)
    ]
    best_buy = store.Store(product_list)
    start(best_buy)