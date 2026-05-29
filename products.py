class Product:
    """Represents a product in the Best Buy store."""

    def __init__(self, name: str, price: float, quantity: int):
        """Initializes a product with validation."""
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
        """Returns the current stock quantity."""
        return self.quantity

    def set_quantity(self, quantity: int):
        """Updates the stock quantity and deactivates if stock hits 0."""
        if quantity < 0:
            raise ValueError("Menge darf nicht negativ sein.")
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False

    def is_active(self) -> bool:
        """Returns whether the product is active."""
        return self.active

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product."""
        self.active = False

    def show(self):
        """Prints the product details to the console."""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, requested_quantity: int) -> float:
        """Processes the purchase of a specific quantity."""
        if not self.active:
            raise ValueError("Dieses Produkt ist derzeit nicht aktiv.")
        if requested_quantity > self.get_quantity():
            raise ValueError("Nicht genügend Bestand im Lager!")
        if requested_quantity <= 0:
            raise ValueError("Kaufmenge muss größer als 0 sein.")

        # Shovals wichtigste Korrektur: Kapselung über Getter/Setter wahren
        new_quantity = self.get_quantity() - requested_quantity
        self.set_quantity(new_quantity)

        return requested_quantity * self.price