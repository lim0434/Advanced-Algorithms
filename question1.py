import time
class Node:
    def __init__(self, product):
        self.product = product
        self.next = None

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
        self.count = 0

    def hash_function(self, key):
        hash_value = 0
        for i, char in enumerate(key):
            hash_value += ord(char) * (31**i)
        return hash_value % self.size

    def insert(self, product):
        index = self.hash_function(product.product_id)
        new_node = Node(product)

        if self.table[index] is None:
            self.table[index] = new_node
            self.count += 1
            return True

        current = self.table[index]
        while current:
            if current.product.product_id == product.product_id:
                print(f"Error: Product ID: {product.product_id} already exists!")
                return False
            if current.next is None:
                break
            current = current.next

        current.next = new_node
        self.count += 1
        return True

    def search(self, product_id):
        index = self.hash_function(product_id)
        current = self.table[index]

        while current:
            if current.product.product_id == product_id:
                return current.product
            current = current.next
        return None

    def update(self, product_id, name=None, category=None, price=None, quantity=None):
        product = self.search(product_id)
        if product:
            if name: product.name = name
            if category: product.category = category
            if price is not None: product.price = price
            if quantity is not None: product.quantity = quantity
            return True
        return False

    def delete(self, product_id):
        index = self.hash_function(product_id)
        current = self.table[index]
        prev = None
        while current:
            if current.product.product_id == product_id:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                self.count -= 1
                return True
            prev = current
            current = current.next
        return False

    def display_all(self):
        print("All Product in Inventory:")
        if self.count == 0:
            print("No products in inventory.")
            return
        for i in range(self.size):
            if self.table[i]:
                current = self.table[i]
                while current:
                    print(current.product)
                    current = current.next
        print(f"Total Products: {self.count}\n")

#Part 2
class Product:
    def __init__(self, product_id, name, category, price, quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return (f"Product ID: {self.product_id}, Name: {self.name}, Category: {self.category}，"
                f"Price: RM{self.price:.2f}, Qty: {self.quantity}")

    def display_details(self):
        print(f"Product ID:{self.product_id}")
        print(f"Name:{self.name}")
        print(f"Category:{self.category}")
        print(f"Price:RM{self.price:.2f}")
        print(f"Quantity:{self.quantity}")

def initialize_inventory():
    hash_table = HashTable(size=10)

    products = [
        Product("P001", "Pampers Diapers", "Diaper", 45.00, 100),
        Product("P002", "Baby Blanket", "Bedding", 29.24, 50),
        Product("P003", "Musical Toy", "Toy", 35.50, 30),
        Product("P004", "Organic Baby Food", "Food", 24.99, 75),
        Product("P005", "Baby Pillow", "Bedding", 10.00, 120),
        Product("P006", "Baby Bottle", "Feeding", 12.99, 80),
        Product("P007", "Stroller", "Transport", 199.89, 15),
        Product("P008", "Baby Shampoo", "Bathing", 25.25, 40),
        Product("P009", "Baby nipple", "Accessories", 5.35, 200),
        Product("P010", "Baby Socks", "Clothing", 9.99, 25),
    ]

    print("\nInsert products into hash table")
    for product in products:
        hash_index = hash_table.hash_function(product.product_id)
        hash_table.insert(product)
        print(f"Added: {product.name:<30} [Hash Index: {hash_index}]")

    print(f"Successfully insert {hash_table.count} products!")
    print(f"Hash Table Size: {hash_table.size} buckets")
    print(f"Load Factor: {hash_table.count / hash_table.size:.2f}")

    return hash_table, products

#Part 3
def menu(hash_table):
    while True:
        print("INVENTORY SYSTEM:")
        print("1. Insert - Add New Product")
        print("2. Search - Find Product by ID")
        print("3. Update - Edit Product Details")
        print("4. Delete - Delete Product")
        print("5. Display All - View All Products")
        print("6. Exit - Exit System")

        choice = input(f"\nEnter your choice (1-6): ").strip()

        if choice == '1':
            print("Insert New Product")
            product_id = input("Product ID: ").strip()
            name = input("Product Name: ").strip()
            category = input("Category: ").strip()

            try:
                price = float(input("Price (RM): "))
                quantity = int(input("Quantity: "))
            except ValueError:
                print("Error: Invalid input for price or quantity!")
                continue

            product = Product(product_id, name, category, price, quantity)
            if hash_table.insert(product):
                print(f"\n{name} successfully added to inventory!")

        elif choice == '2':
            print("Search Product")
            product_id = input("Enter Product ID to search: ").strip()

            start_time = time.perf_counter_ns()
            product = hash_table.search(product_id)
            end_time = time.perf_counter_ns()
            search_time = end_time - start_time

            if product:
                print(f"\nProduct found in {search_time} nanoseconds!")
                product.display_details()
            else:
                print(f"\nProduct ID: {product_id} not found in inventory.")

        elif choice == '3':
            print("Update Product")
            product_id = input("Enter Product ID to update: ").strip()
            product = hash_table.search(product_id)

            if not product:
                print(f"\nProduct ID: {product_id} not found.")
                continue

            print("\nProduct Details:")
            product.display_details()
            print("\nEnter new details (press Enter to keep current details):")

            name = input(f"Name ({product.name}): ").strip() or None
            category = input(f"Category ({product.category}): ").strip() or None
            price_input = input(f"Price (RM{product.price}: ").strip()
            price = float(price_input) if price_input else None
            quantity_input = input(f"Quantity ({product.quantity}): ").strip()
            quantity = int(quantity_input) if quantity_input else None

            if hash_table.update(product_id, name, category, price, quantity):
                print("\nProduct update successful!")

        elif choice == '4':
            print("Delete Product")
            product_id = input("Enter Product ID to delete: ").strip()

            if hash_table.delete(product_id):
                print(f"\nProduct {product_id} deleted from inventory!")
            else:
                print(f"\nProduct ID: {product_id} not found.")

        elif choice == '5':
            hash_table.display_all()

        elif choice == '6':
            print("Thank you and goodbye!")
            break
        else:
            print("\nInvalid choice! Please enter 1-6.")

#Part 4
class ArrayStorage:
    def __init__(self):
        self.products = []

    def insert(self, product):
        self.products.append(product)

    def search(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None

def performance_comp(hash_table, products):
    print("Performance Comparison")

    array_storage = ArrayStorage()
    for product in products:
        array_storage.insert(product)

    print(f"\nTotal: {len(products)} products")
    print("Test: Search for 5 different products\n")

    search_prod = ["P001", "P005", "P010", "P003", "P007"]
    hash_times = []
    for product_id in search_prod:
        start = time.perf_counter_ns()
        result = hash_table.search(product_id)
        end = time.perf_counter_ns()
        hash_times.append(end - start)

    array_times = []
    for product_id in search_prod:
        start = time.perf_counter_ns()
        result = array_storage.search(product_id)
        end = time.perf_counter_ns()
        array_times.append(end - start)

    print("Search Result:")
    print("-" * 80)
    print(f"{'Product ID':<15} {'Hash Table (ns)':<20} {'Array (ns)':<20} {'Difference':<15}")
    print("-" * 80)

    for i, product_id in enumerate(search_prod):
        diff = array_times[i] - hash_times[i]
        print(f"{product_id:<15} {hash_times[i]:<20} {array_times[i]:<20} {diff:+} ns")

    avg_hash = sum(hash_times) / len(hash_times)
    avg_array = sum(array_times) / len(array_times)

    print("-" * 80)
    print(f"{'AVERAGE':<15} {avg_hash:<20.2f} {avg_array:<20.2f} {avg_array - avg_hash:+.2f} ns")

def main():
    print("Baby Products Inventory Management System")
    print("-" * 80)

    hash_table, products = initialize_inventory()

    input("\nPress Enter to start Inventory System")
    menu(hash_table)
    print("\nInventory System session has ended.")

    input("\nPress Enter to start performance comparison")
    performance_comp(hash_table, products)

if __name__ == "__main__":
    main()

