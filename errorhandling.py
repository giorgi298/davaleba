# DAVALEBA 1
# amount = float(input("ყიდვის თანხა (ლარი): "))
# promo = input("პრომო-კოდი (თუ არ გაქვთ – Enter): ")
#
#
# if amount >= 200:
#     discount_percent = 20
# elif amount >= 100:
#     discount_percent = 10
# elif amount >= 50:
#     discount_percent = 5
# else:
#     discount_percent = 0
#
#
# total = amount * (1 - discount_percent / 100)
#
#
# if promo.strip().upper() == "VIP":
#     print("VIP კოდი: დამატებით -5 ლარი")
#     total -= 5
#
#
# print(f"ფასდაკლება: {discount_percent}%")
# print(f"გადასახდელი: {total:.2f} ლარი")


# davaleba 2
try:
    name = input("სტუდენტის სახელი: ").strip()
    if not name:
        raise Exception("სახელი ცარიელი ვერ იქნება")

    earned = int(input("მიღებული ქულა: "))
    max_score = int(input("მაქსიმალური ქულა: "))

    if max_score == 0:
        raise ZeroDivisionError("მაქსიმალური ქულა 0 ვერ იქნება")

    if earned < 0 or earned > max_score:
        raise Exception("ქულა არასწორ დიაპაზონშია")

except ValueError:
    print("ქულები მთელი რიცხვებით ჩაწერეთ")
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(e)
else:
    initial = name[0]
    percent = (earned / max_score) * 100

    if percent >= 91:
        grade = "A"
    elif percent >= 81:
        grade = "B"
    elif percent >= 71:
        grade = "C"
    elif percent >= 61:
        grade = "D"
    elif percent >= 51:
        grade = "E"
    elif percent >= 41:
        grade = "FX"
    else:
        grade = "F"

    print(f"ინიციალი: {initial}")
    print(f"პროცენტი: {percent:.2f}%")
    print(f"შეფასება: {grade}")
finally:
    print("შეფასების სისტემამ მუშაობა დაასრულა")