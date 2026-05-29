from typing import List
from products import Product

class Store:
    """Manages the inventory of products in the store."""

    def __init__(self, products: List[Product]):
        """Initializes the store and ensures type validation for all items."""
        if not isinstance(products, list) or not all(isinstance(p, Product) for p in products):
            raise ValueError("Der Parameter 'products' muss eine Liste von Product-Instanzen sein.")
        self.products = products

    def add_product(self, product: Product):
        """Adds a valid Product instance to the store."""
        if isinstance(product, Product):
            self.products.append(product)

    def remove_product(self, product: Product):
        """Removes a product from the store if it exists."""
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Returns the total stock of all items using a pythonic sum."""
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> List[Product]:
        """Returns all currently active products."""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[tuple]) -> float:
        """Processes an order from a shopping list containing tuples of (Product, quantity)."""
        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price