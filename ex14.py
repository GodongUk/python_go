def basket_total(*prices):
    if not prices:
        return 0
    return sum(prices)

def item_total(**moon):
    return moon


total = basket_total(6000,5000)
print(total)


items = [("pen", 1500), ("book", 12000), ("tv", 3000000), ("computer", 4000000),("apple", 3000)]

print(sorted(items, key = lambda item: item[1], reverse=True))
print(sorted(items, key = lambda item: len(item[0])))






