from typing import List
from products import Product

class Store:
    """Repräsentiert das Geschäft, das Produkte verwaltet."""

    def __init__(self, products: List[Product]):
        """Initialisiert das Geschäft und validiert den Typ der Produktliste."""
        if not isinstance(products, list) or not all(isinstance(p, Product) for p in products):
            raise ValueError("Der Parameter 'products' muss eine Liste von Product-Instanzen sein.")
        self.products = products

    def add_product(self, product: Product):
        """Fügt ein Produkt zum Geschäft hinzu."""
        if isinstance(product, Product):
            self.products.append(product)

    def remove_product(self, product: Product):
        """Entfernt ein Produkt aus dem Geschäft."""
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Gibt die Gesamtmenge aller Produkte unter Verwendung von sum() zurück."""
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> List[Product]:
        """Gibt alle aktiven Produkte im Geschäft zurück."""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[tuple]) -> float:
        """Verarbeitet eine Bestellung basierend auf einer Einkaufsliste."""
        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price