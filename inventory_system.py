"""Inventory System Module
Handles adding, removing, saving, loading, and checking inventory data.
"""

import json
from datetime import datetime

# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Add an item to inventory."""
    if logs is None:
        logs = []
    if not item:
        return
    if not isinstance(item, str):
        raise TypeError("Item name must be a string.")
    if not isinstance(qty, (int, float)):
        raise TypeError("Quantity must be a number.")
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """Remove quantity of an item from inventory."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        pass


def get_qty(item):
    """Return the current quantity of an item."""
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """Load stock data from a file."""
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
    except FileNotFoundError:
        stock_data = {}


def save_data(file="inventory.json"):
    """Save stock data to a file."""
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f, indent=4)


def print_data():
    """Print current inventory items and quantities."""
    print("Items Report")
    for i, qty in stock_data.items():
        print(i, "->", qty)


def check_low_items(threshold=5):
    """Return a list of items below threshold quantity."""
    return [i for i, qty in stock_data.items() if qty < threshold]


def main():
    """Demo main function for inventory system."""
    add_item("apple", 10)
    add_item("banana", -2)
    # Removed invalid types call (123, "ten") and added type-safe example
    try:
        add_item(123, "ten")
    except TypeError as e:
        print("Error:", e)

    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()


if __name__ == "__main__":
    main()
"""