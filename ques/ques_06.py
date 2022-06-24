string = input()

items_list = {
    "A": {
        "price": 50,
        "count": 3,
        "discount_price": 130,
    },
    "B": {
        "price": 30,
        "count": 2,
        "discount_price": 45,
    },
    "C": 20,
    "D": 15,
}

items_count = {}

for ch in string:
    print("ch--", ch)

    if ch in items_count:
        items_count[ch] += 1
    else:
        items_count[ch] = 1

print("items_count", items_count)

total = 0

for key in items_count:

    if type(items_list[key]) == dict :
        rem = items_count[key] % items_list[key]['count']
        div = items_count[key] // items_list[key]['count']
        total += rem*items_list[key]['price'] + div * items_list[key]['discount_price']
    else:
        total += items_list[key] * items_count[key]

print("Total Price: ", total)


