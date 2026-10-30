
"""Manage restaurant orders and print kitchen tickets using polymorphism."""


class Order:
    """Represent a general restaurant order."""

    def __init__(self, items):
        """Initialize an order with a list of items."""
        self.items = items

    def print_ticket(self):
        """Print the kitchen ticket."""
        raise NotImplementedError("Subclasses must implement print_ticket()")


class DineInOrder(Order):
    """Represent a dine-in restaurant order."""

    def __init__(self, table_number, items):
        """Initialize a dine-in order."""
        super().__init__(items)
        self.table_number = table_number

    def print_ticket(self):
        """Print a dine-in kitchen ticket."""
        print("\n--- DINE-IN TICKET ---")
        print(f"Table Number: {self.table_number}")
        print(f"Items: {', '.join(self.items)}")


class TakeoutOrder(Order):
    """Represent a takeout restaurant order."""

    def __init__(self, order_number, items):
        """Initialize a takeout order."""
        super().__init__(items)
        self.order_number = order_number

    def print_ticket(self):
        """Print a takeout kitchen ticket."""
        print("\n--- TAKEOUT TICKET ---")
        print(f"Order Number: {self.order_number}")
        print(f"Items: {', '.join(self.items)}")


class DeliveryOrder(Order):
    """Represent a delivery restaurant order."""

    def __init__(self, address, items):
        """Initialize a delivery order."""
        super().__init__(items)
        self.address = address

    def print_ticket(self):
        """Print a delivery kitchen ticket."""
        print("\n--- DELIVERY TICKET ---")
        print(f"Address: {self.address}")
        print(f"Items: {', '.join(self.items)}")


def main():
    """Collect restaurant orders and print kitchen tickets."""

    orders = []

    print("Restaurant Ordering System")
    print("Order types: dine-in, takeout, delivery")
    print("Type 'done' to finish ordering.")

    while True:
        order_type = input("\nEnter order type: ").strip().lower()

        if order_type == "done":
            break

        if order_type == "dine-in":
            table_number = input("Enter table number: ")
            items = input("Enter items (comma-separated): ").split(",")
            order = DineInOrder(table_number, [item.strip() for item in items])

        elif order_type == "takeout":
            order_number = input("Enter order number: ")
            items = input("Enter items (comma-separated): ").split(",")
            order = TakeoutOrder(order_number, [item.strip() for item in items])

        elif order_type == "delivery":
            address = input("Enter delivery address: ")
            items = input("Enter items (comma-separated): ").split(",")
            order = DeliveryOrder(address, [item.strip() for item in items])

        else:
            print("Invalid order type. Try again.")
            continue

        orders.append(order)
        print("Order added successfully!")

    print("\n========== KITCHEN PRINTER ==========")

    for order in orders:
        order.print_ticket()

    print("\nAll tickets printed. Thank you!")


if __name__ == "__main__":
    main()
