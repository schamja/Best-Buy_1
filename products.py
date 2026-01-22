class Product:
    def __init__(self, name, price, quantity):
        """Initialisiert ein Produkt mit Validierung."""
        # Validierung der Eingabewerte
        if not name:
            raise ValueError("Der Name darf nicht leer sein")
        if price < 0:
            raise ValueError("Der Preis darf nicht negativ sein")
        if quantity < 0:
            raise ValueError("Die Menge darf nicht negativ sein")

        # Instanzvariablen initialisieren
        self._name = name
        self._price = price
        self._quantity = quantity
        self._active = True

        # Produkt deaktivieren, wenn Menge 0 ist
        if quantity == 0:
            self.deactivate()

