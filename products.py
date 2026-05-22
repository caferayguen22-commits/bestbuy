class Product:
    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Der Produktname darf nicht leer sein.")
        if price < 0:
            raise ValueError("Der Preis darf nicht negativ sein.")
        if quantity < 0:
            raise ValueError("Die Menge darf nicht negativ sein")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Menge darf nicht negativ sein.")
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity) -> float:
        if not self.active:
            raise ValueError("Dieses Produkt ist derzeit nicht aktiv.")
        if quantity > self.quantity:
            raise ValueError("Nicht genügend Bestand im Lager!")
        if quantity <= 0:
            raise ValueError("Kaufmenge muss größer als 0 sein.")

        self.quantity -= quantity

        if self.quantity == 0:
            self.active = False

        return quantity * self.price

if __name__ == "__main__":

    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()