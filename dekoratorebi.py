# dav 1

# from functools import wraps
#
# def framed(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return f"*** {res} ***"
#     return wrapper
#
# @framed
# def greet(name):
#     """აბრუნებს მისალმებას."""
#     return f"გამარჯობა, {name}"
#
# @framed
# def order_summary(item, quantity=1):
#     return f"{item} x {quantity}"
#
# print(greet("ნინო"))
# print(order_summary("ხაჭაპური", quantity=2))
# print(order_summary("ჩაი"))
# print(greet.__name__, "|", greet.__doc__)

# dav 2

# def make_wallet(balance):
#     def spend(amount):
#         nonlocal balance
#         if amount > balance:
#             return f"არასაკმარისი თანხა (ბალანსი: {balance} ₾)"
#         balance -= amount
#         return f"დაიხარჯა {amount} ₾, დარჩა {balance} ₾"
#     return spend
#
# def make_tax(rate):
#     def add_tax(price):
#         return round(price + (price * rate / 100), 2)
#     return add_tax
#
# nino = make_wallet(100)
# luka = make_wallet(30)
#
# print(nino(40))
# print(nino(70))
# print(luka(25))
# print(nino(60))
#
# georgia_vat = make_tax(18)
# low_tax = make_tax(5)
# print(georgia_vat(100), low_tax(100))
# print(list(map(georgia_vat, [10, 25.5, 99])))