import products
import store


def start(best_buy):
    """Startet die interaktive Benutzeroberfläche für den Store."""
    while True:
        print("\n   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice == "1":
            # Alle aktiven Produkte anzeigen
            all_products = best_buy.get_all_products()
            print("------")


        elif choice == "2":
            # Gesamte Menge im Store anzeigen
            total = best_buy.get_total_quantity()
            print(f"Total amount in store: {total}")

        elif choice == "3":
            all_products = best_buy.get_all_products()

            if not all_products:
                print("No products available in store.")
                continue



def main():
    """Hauptfunktion zum Starten des Programms."""
    # Setup initial stock of inventory
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250)
    ]

    best_buy = store.Store(product_list)
    start(best_buy)
    return

if __name__ == "__main__":
    main()