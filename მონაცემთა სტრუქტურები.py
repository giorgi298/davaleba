# dav1
# def demo_o1(data):
#     steps = 0
#     for _ in range(1):
#         steps += 1
#     return steps
#
# def demo_on(data):
#     steps = 0
#     for _ in data:
#         steps += 1
#     return steps
#
# def demo_on2(data):
#     steps = 0
#     for _ in data:
#         for _ in data:
#             steps += 1
#     return steps
#
# numbers = [10, 20, 30, 40, 50]
#
# print("O(1):", demo_o1(numbers))
# print("O(n):", demo_on(numbers))
# print("O(n^2):", demo_on2(numbers))

# dav2
# class Stack:
#     def __init__(self):
#         self.items = []
#
#     def push(self, item):
#         self.items.append(item)
#
#     def pop(self):
#         return self.items.pop()
#
#     def is_empty(self):
#         return len(self.items) == 0
#
#
# def reverse_text(text):
#     s = Stack()
#     for ch in text:
#         s.push(ch)
#     res = ""
#     while not s.is_empty():
#         res += s.pop()
#     return res
#
#
# def is_palindrome(text):
#     clean = text.replace(" ", "").lower()
#     return clean == reverse_text(clean)
#
#
# print(reverse_text("Python"))
# print(reverse_text("გამარჯობა"))
# print(is_palindrome("აი ია"))
# print(is_palindrome("Level"))
# print(is_palindrome("Python"))