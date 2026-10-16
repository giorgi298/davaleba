orders = ["ყავა", "ჩაი", "ყავა", "წვენი", "ჩაი", "ყავა", "წყალი"]

unique_orders = []
for item in orders:
    if item not in unique_orders:
        unique_orders.append(item)

print(f"უნიკალური: {unique_orders}")

frequency = [(item, orders.count(item)) for item in unique_orders]
print(f"სიხშირე: {frequency}")

max_count = 0
most_popular = ""
for product, count in frequency:
    if count > max_count:
        max_count = count
        most_popular = product

print(f"ყველაზე პოპულარული: {most_popular} ({max_count}-ჯერ)")

last_three = orders[-1:-4:-1]
print(f"ბოლო 3 შეკვეთა: {last_three}")