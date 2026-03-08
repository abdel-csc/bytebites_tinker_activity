# ByteBites Models
# Four core classes:
# - Customer: stores name and purchase history
# - MenuItem: stores name, price, category, popularity
# - Menu: holds all MenuItems, supports filtering by category
# - Order: holds selected MenuItems, computes total cost

class Customer:
    def __init__(self, name):
        self.name = name
        self.history = []  # list of Order objects


class MenuItem:
    def __init__(self, name, price, category, popularity):
        self.name = name
        self.price = price
        self.category = category
        self.popularity = popularity


class Menu:
    def __init__(self):
        self.items = []  # list of MenuItem objects

    def filter_by_category(self, category):
        pass  # to be implemented in Part 3


class Order:
    def __init__(self):
        self.items = []  # list of MenuItem objects

    def compute_total(self):
        return sum(item.price for item in self.items)
