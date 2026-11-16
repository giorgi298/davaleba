import json
from dataclasses import dataclass, field, asdict

# DAV 1

# def save_json(path, data):
#     with open(path, "w", encoding="utf-8") as f:
#         json.dump(data, f, ensure_ascii=False, indent=2)
#
# def load_json(path, default=None):
#     try:
#         with open(path, "r", encoding="utf-8") as f:
#             return json.load(f)
#     except (FileNotFoundError, json.JSONDecodeError):
#         return default
#
# save_json("test.json", {"name": "ნინო", "scores": [90, 85], "pair": (1, 2)})
# data = load_json("test.json")
# print(data)
# print(type(data.get("pair")))
#
# print(load_json("nonexistent.json", default={}))
# print(load_json("bad.json", default="არასწორი ფაილი"))


# DAV 2

# @dataclass
# class Movie:
#     title: str
#     year: int = 2000
#     rating: float = 0.0
#     genres: list = field(default_factory=list)
#
#     def __post_init__(self):
#         if not (0 <= self.rating <= 10):
#             raise ValueError("რეიტინგი უნდა იყოს 0-დან 10-მდე")
#
# def best_movies(movies, min_rating):
#     filtered = [m for m in movies if m.rating >= min_rating]
#     return sorted(filtered, key=lambda x: x.rating, reverse=True)
#
# m1 = Movie("მონანიება", 1984, 9.1, ["დრამა"])
# m2 = Movie("გზა", 2020, 7.5)
# m3 = Movie("მოგზაურობა", rating=8.2, genres=["თავგადასავალი"])
#
# print(m1)
# m_clone = Movie("მონანიება", 1984, 9.1, ["დრამა"])
# print(m1 == m_clone)
#
# m2.genres.append("კომედია")
# print(m2.genres)
# print(m3.genres)
#
# for m in best_movies([m1, m2, m3], 8.0):
#     print(f"{m.title} {m.rating}")
#
# print(json.dumps(asdict(m1), ensure_ascii=False))
#
# try:
#     Movie("ცუდი", 2000, 11)
# except ValueError as e:
#     print(f"შეცდომა: {e}")