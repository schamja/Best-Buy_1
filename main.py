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
            for i, product in enumerate(all_products, 1):
                # Verwende show() als String-Return
                print(f"{i}. {product.show()}")
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

            shopping_list = []

            # Verfügbare Produkte anzeigen
            print("------")
            for i, product in enumerate(all_products, 1):
                print(f"{i}. {product.show()}")
            print("------")
            print("When you want to finish order, enter empty text.")

            while True:
                prod_idx = input("Which product # do you want? ").strip()

                # Leere Eingabe oder nicht-numerische Eingabe beendet die Bestellung
                if prod_idx == "" or not prod_idx.isdigit():
                    if prod_idx != "" and not prod_idx.isdigit():
                        print("Finishing order...")
                    break

                try:
                    idx = int(prod_idx) - 1

                    if not (0 <= idx < len(all_products)):
                        print("Error: Invalid product number. Please try again.")
                        continue

                    amount = input("What amount do you want? ").strip()

                    # Wenn Menge leer ist, zur nächsten Produktauswahl
                    if amount == "":
                        print("No amount entered. Please select a product again.")
                        continue

                    if not amount.isdigit():
                        print("Error: Please enter a valid number for amount.")
                        continue

                    qty = int(amount)

                    if qty <= 0:
                        print("Error: Amount must be greater than 0.")
                        continue

                    shopping_list.append((all_products[idx], qty))
                    print("Product added to list!")

                except ValueError:
                    print("Error: Please enter valid numbers.")
                except Exception as e:
                    print(f"Error: {e}")

            # Bestellung durchführen
            if shopping_list:
                print("\n--- Your Order ---")
                for product, qty in shopping_list:
                    print(f"  {product.name}: {qty} units")
                print("------------------")

                try:
                    total_price = best_buy.order(shopping_list)
                    print("********")
                    print(f"Order made! Total payment: ${total_price:.2f}")
                    print("********")
                except Exception as e:
                    print(f"Error while making order! {e}")
            else:
                print("No products selected. Order cancelled.")

        elif choice == "4":
            print("Bye!")
            break

        else:
            print("Invalid choice, please try again.")


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


if __name__ == "__main__":
    main()