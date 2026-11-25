owned_items = {"book","pen"}
wish_items = {"pen", "bag"}

sum_items = sorted(owned_items & wish_items)
print(sum_items)

