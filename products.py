class Product:
    """Repräsentiert ein Produkt im Best Buy Geschäft."""

    def __init__(self, name: str, price: float, quantity: int):
        """Initialisiert ein Produkt mit Name, Preis und Menge."""
        if not name:
            raise ValueError("Der Produktname darf nicht leer sein.")
        if price < 0:
            raise ValueError("Der Preis darf nicht negativ sein.")
        if quantity < 0:
            raise ValueError("Die Menge darf nicht negativ sein.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """Gibt die aktuelle Menge des Produkts zurück."""
        return self.quantity

    def set_quantity(self, quantity: int):
        """Setzt die Menge des Produkts und deaktiviert es, wenn die Menge 0 ist."""
        if quantity < 0:
            raise ValueError("Menge darf nicht negativ sein.")
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False

    def is_active(self) -> bool:
        """Gibt zurück, ob das Produkt aktiv ist."""
        return self.active

    def activate(self):
        """Aktiviert das Produkt."""
        self.active = True

    def deactivate(self):
        """Deaktiviert das Produkt."""
        self.active = False

    def show(self):
        """Gibt die String-Repräsentation des Produkts auf der Konsole aus."""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, requested_quantity: int) -> float:
        """Führt den Kauf einer bestimmten Menge aus."""
        if not self.active:
            raise ValueError("Dieses Produkt ist derzeit nicht aktiv.")
        if requested_quantity > self.get_quantity():
            raise ValueError("Nicht genügend Bestand im Lager!")
        if requested_quantity <= 0:
            raise ValueError("Kaufmenge muss größer als 0 sein.")

        # Nutzung von set_quantity & get_quantity wahrt das Kapselungsprinzip
        new_quantity = self.get_quantity() - requested_quantity
        self.set_quantity(new_quantity)

        return requested_quantity * self.price