from .product import Product


class ProductRepository():

    def __init__(self) -> None:
        self.products = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> Product:
        matches = [p for p in self.products if p.name == product_name]
        if matches:
            return matches[0]

    def remove(self, product_name: str) -> None:
        match = self.find(product_name)
        if match:
            self.products.remove(match)

    def __repr__(self) -> str:
        retval = [f'{product.name}: {product.quantity}' for product in self.products]
        return '\n'.join(retval)
