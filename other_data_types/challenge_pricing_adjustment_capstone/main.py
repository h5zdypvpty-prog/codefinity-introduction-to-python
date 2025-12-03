grocery_inventory = {"Milk": ("Dairy", 3.50, 28), "Eggs": ("Dairy", 4.50, 30), "Bread": ("Bakery", 2.99, 15), "Apples": ("Produce", 1.50, 50)}

print(" eggs are too expensive, reducing the price by $1.")
grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)})
print("inventory after adding tomatoes:", grocery_inventory)

print(" milk needs to be restocked. increasing stock by 20 units.")
print("updated inventory:", grocery_inventory)