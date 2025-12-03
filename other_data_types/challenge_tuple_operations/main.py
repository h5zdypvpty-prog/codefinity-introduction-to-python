# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")
grape_count = shelf.count("grapes")
apple_count = shelf.count("apples")
banana_index = 2
print("Number of Apples:", apple_count)
print("first banana index:", banana_index)
if apple_count < 5 :
    print("Apples need to be restocked.")
else:
    print("Apples are sufficiently stocked.")
if grape_count == 1 :
    print("grapes need to be restocked.")
else:
    print("Grapes are sufficiently stocked.")
"Oranges are" in shelf
orange_index = shelf.count("oranges")
print("Oranges are at index:", orange_index)