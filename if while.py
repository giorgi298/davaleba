# /DAVALBA 1


# teksti = input("შეიყვანე სიტყვა: ")
# simbolo_erti = input("რომელი სიმბოლო დავთვალოთ: ")
# count = 0
# 
# for simbolo in teksti:
#     if simbolo == simbolo_erti:
#         count = count + 1
# 
# print(f"სიმბოლო {simbolo_erti} გვხვდები {count}- ჯერ")
# 

# DAVALEBA 2

attempts = 3

while attempts > 0:
    password = input("შეიყვანე პაროლი: ")

    if password == "":
        continue

    if password == "python2024":
        print("წვდომა დაშვებულია")
        break

    attempts -= 1
    print(f"არასწორი პაროლი. დარჩენილი მცდელობა: {attempts}")
else:
    print("ანგარიში დაბლოკილია")