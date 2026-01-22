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

    @property
    def name(self):
        """Gibt den Produktnamen zurück."""
        return self._name

    @property
    def price(self):
        """Gibt den Preis zurück."""
        return self._price

    @property
    def quantity(self):
        """Gibt die aktuelle Menge zurück."""
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        """Setzt die Menge und deaktiviert bei 0."""
        if value < 0:
            raise ValueError("Menge kann nicht negativ sein.")
        self._quantity = value
        if value == 0:
            self.deactivate()

    def get_quantity(self) -> int:
        """Gibt die aktuelle Menge zurück (alternative Methode)."""
        return self._quantity

    def set_quantity(self, quantity):
        """Aktualisiert die Menge und deaktiviert das Produkt, falls 0 erreicht ist."""
        self.quantity = quantity  # Nutzt den Property Setter

    def is_active(self):
        """Prüft, ob das Produkt aktiv ist."""
        return self._active

    def activate(self):
        """Aktiviert das Produkt."""
        self._active = True

    def deactivate(self):
        """Deaktiviert das Produkt."""
        self._active = False

    def show(self) -> str:
        """Gibt die Produktinformationen als String zurück."""
        status = "Active" if self._active else "Inactive"
        return f"{self._name}, Price: {self._price}, Quantity: {self._quantity} ({status})"

    def buy(self, quantity) -> float:
        """Kauft eine Menge des Produkts und gibt den Gesamtpreis zurück."""
        if not self.is_active():
            raise ValueError(f"Produkt {self._name} ist nicht verfügbar")

        if quantity <= 0:
            raise ValueError("Die Kaufmenge muss größer als Null sein")

        if quantity > self._quantity:
            raise ValueError(f"Nicht genügend Bestand auf Lager! Verfügbar: {self._quantity}")

        total_price = self._price * quantity
        self.quantity = self._quantity - quantity  # Nutzt den Property Setter
        return float(total_price)