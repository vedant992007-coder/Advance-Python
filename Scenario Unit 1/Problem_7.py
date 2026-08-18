class Product:
    def __init__(self, product_id, product_name, price):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price

    def category(self):
        if self.price >= 1000:
            return "Expensive"
        else:
            return "Affordable"

    def display(self):
        print("Product ID   :", self.product_id)
        print("Product Name :", self.product_name)
        print("Price        :", self.price)
        print("Category     :", self.category())
        print("-" * 30)


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        print("\nProduct Inventory")
        print("=" * 30)
        for product in self.products:
            product.display()


# Main Program
inventory = Inventory()

# Adding products
inventory.add_product(Product(101, "Laptop", 55000))
inventory.add_product(Product(102, "Notebook", 80))
inventory.add_product(Product(103, "Headphones", 1500))
inventory.add_product(Product(104, "Pen", 20))

# Display all products
inventory.display_products()