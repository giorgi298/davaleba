# //DAVALEBA 1
# text = "Python არის მარტივი, Python არის ძლიერი და Python პოპულარულია."
#
# cleaned_text = text.lower().replace(",", "").replace(".", "")
# words = cleaned_text.split()
#
# word_counts = {}
# for word in words:
#     if word in word_counts:
#         word_counts[word] += 1
#     else:
#         word_counts[word] = 1
#
# for word, count in word_counts.items():
#     print(f"{word}: {count}")
#
# max_count = 0
# most_frequent_word = ""
# for word, count in word_counts.items():
#     if count > max_count:
#         max_count = count
#         most_frequent_word = word
#
# print(f"ყველაზე ხშირი: '{most_frequent_word}' ({max_count}-ჯერ)")
# print(f"სხვადასხვა სიტყვა: {len(word_counts)}")

# //DAVALEBA 2
# prices = {"ლეპტოპი": 2500, "მაუსი": 40, "კლავიატურა": 120, "მონიტორი": 650}
# stock = {"ლეპტოპი": 2, "მაუსი": 10, "კლავიატურა": 1, "მონიტორი": 3}
#
# orders = [
#     ("ნინო", "ლეპტოპი", 1),
#     ("გიორგი", "მაუსი", 3),
#     ("ანა", "კლავიატურა", 1),
#     ("ნინო", "მაუსი", 2),
#     ("გიორგი", "კლავიატურა", 1),
#     ("ანა", "ტელეფონი", 1),
#     ("ლუკა", "ლეპტოპი", 1),
#     ("ლუკა", "მონიტორი", 5)
# ]
#
# spent_per_user = {}
# failed_users = set()
# total_revenue = 0

# for name, product, quantity in orders:
#     if product not in prices:
#         print(f" {name}: '{product}' არ იყიდება")
#         failed_users.add(name)
#     elif stock.get(product, 0) < quantity:
#         print(f"⚠️ {name}: {product} – მარაგში მხოლოდ {stock.get(product, 0)} ცალია")
#         failed_users.add(name)
#     else:
#         cost = prices[product] * quantity
#         stock[product] -= quantity
#         print(f"️ {name}: {product} x{quantity} = {cost} ლარი")
#
#         if name not in spent_per_user:
#             spent_per_user[name] = 0
#         spent_per_user[name] += cost
#         total_revenue += cost
#
# print("--- ანგარიში ---")
# for name, spent in spent_per_user.items():
#     print(f"{name}: {spent} ლარი")
#
# print(f"შემოსავალი: {total_revenue} ლარი")
#
# out_of_stock = sorted([p for p, s in stock.items() if s == 0])
# print(f"ამოიწურა: {out_of_stock}")
#
# sorted_failed_users = sorted(list(failed_users))
# print(f"წარუმატებელი შეკვეთა ჰქონდათ: {sorted_failed_users}")