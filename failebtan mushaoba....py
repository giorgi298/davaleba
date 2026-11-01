import os

def save_scores(path, scores):
    with open(path, "w", encoding="utf-8") as file:
        for name, score in scores.items():
            file.write(f"{name}:{score}\n")

def add_score(path, name, score):
    with open(path, "a", encoding="utf-8") as file:
        file.write(f"{name}:{score}\n")

def read_scores(path):
    result = {}
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            name, score = line.strip().split(":")
            result[name] = int(score)
    return result

os.makedirs("data", exist_ok=True)

save_scores("data/scores.txt", {"ნინო": 92, "გიორგი": 78, "ანა": 85})
add_score("data/scores.txt", "დათო", 64)
add_score("data/scores.txt", "მარიამი", 97)

with open("data/scores.txt", encoding="utf-8") as file:
    print(file.read(), end="")

scores = read_scores("data/scores.txt")
print(scores)

print("სტუდენტები:", len(scores))

avg = round(sum(scores.values()) / len(scores), 1)
print("საშუალო ქულა:", avg)

best_student = max(scores, key=scores.get)
print("საუკეთესო:", best_student, scores[best_student])

with open("data/passed.txt", "w", encoding="utf-8") as file:
    for name, score in scores.items():
        if score >= 80:
            file.write(f"{name}\n")

passed = []
with open("data/passed.txt", "r", encoding="utf-8") as file:
    for line in file:
        passed.append(line.strip())

print("ჩააბარეს (80+):", passed)