import products

class Store:
    def __init__(self, product_list):
        """Initialisiert den Store mit einer Liste von Produkten."""
        self._products = product_list

    def add_product(self, product):
        """Fügt ein Produkt zum Store hinzu."""
        self._products.append(product)

    def remove_product(self, product):
        """Entfernt ein Produkt aus dem Store."""
        if product in self._products:
            self._products.remove(product)

    def get_total_quantity(self) -> int:
        """Gibt die Gesamtmenge aller Produkte im Store zurück."""
        return sum(product.get_quantity() for product in self._products)

    def get_all_products(self):
        """Gibt eine Liste aller aktiven Produkte zurück."""
        return [product for product in self._products if product.is_active()]

    def order(self, shopping_list) -> float:
        """
        Führt eine Bestellung aus.

        Args:
            shopping_list: Liste von Tupeln (Product, quantity)

        Returns:
            Gesamtpreis der Bestellung

        Raises:
            ValueError: Wenn die Bestellung nicht durchgeführt werden kann
        """
        # Phase 1: Validierung der gesamten Bestellung
        for product, quantity in shopping_list:
            if not product.is_active():
                raise ValueError(f"Produkt {product.name} ist nicht verfügbar")

            if quantity <= 0:
                raise ValueError(f"Ungültige Menge für {product.name}: {quantity}")

            if quantity > product.get_quantity():
                raise ValueError(
                    f"Nicht genügend Bestand für {product.name}. "
                    f"Verfügbar: {product.get_quantity()}, Angefordert: {quantity}"
                )

        # Phase 2: Bestellung durchführen (nur wenn alles validiert wurde)
        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)

        return total_price