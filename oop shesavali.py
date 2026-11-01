# dav 1
# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#
#     def info(self):
#         print(f"{self.title} – {self.author}, {self.pages} გვ.")
#
# b1 = Book("ვეფხისტყაოსანი", "შოთა რუსთაველი", 250)
# b2 = Book("კადმოსის მემკვიდრენი", "ჯემალ ქარჩხაძე", 320)
# b3 = Book("ბახტრიონი", "ილია ჭავჭავაძე", 180)
#
# b1.info()
# b2.info()
# b3.info()

# dav 2
# class Car:
#     wheels = 4
#
#     def __init__(self, brand, color, year):
#         self.brand = brand
#         self.color = color
#         self.year = year
#
# c1 = Car("BMW", "შავი", 2020)
# c2 = Car("Toyota", "თეთრი", 2018)
#
# print(c1.brand, c1.wheels)
# print(c2.brand, c2.wheels)
#
# c2.wheels = 3
#
# print(c1.wheels)
# print(c2.wheels)
# print(Car.wheels)


# dav 3

# class Player:
#     players_count = 0
#
#     def __init__(self, name, level=1):
#         self.name = name
#         self.level = level
#         Player.players_count += 1
#
# print(Player.players_count)
#
# p1 = Player("ანა")
# p2 = Player("დავითი", 5)
# p3 = Player(name="მარიამი", level=3)
#
# print("სულ მოთამაშე:", Player.players_count)
# print(p1.name, p1.level)
# print(p2.name, p2.level)
# print(p3.name, p3.level)