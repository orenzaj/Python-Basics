# This is a class that will implement Inventory.
# It will be like the bag of a game.

from items import Item
from items import Weapon

class Inventory:
    def __init__(self):
        self.slots = []

    def add(self, item):
        self.slots.append(item)

    def __len__(self):
        return len(self.slots)

    def __contains__(self, item):
        return item in self.slots

    def __iter__(self):
        for item in self.slots:
            yield item

        # == yield from self.slots


# Make item
coin = Item('Coin', "A shiny coin")

# Make weapons
staff = Weapon('Staff', 'A magical staff', 35)
sword = Weapon('Staff', 'A sharp sword', 50)

# Make a bag and add the item
inventory = Inventory()
inventory.add(coin)
inventory.add(staff)

# Check amount of item in bag
print(sword in inventory)
print(coin in inventory)
print(len(inventory))


for item in inventory:
    print(item.description)
