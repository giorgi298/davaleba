import asyncio
import time

#
# async def deliver(order, seconds):
#     print(f"{order}: გაიგზავნა")
#     await asyncio.sleep(seconds)
#     print(f"{order}: მიტანილია")
#
#
# orders = [("შკვეთა #1", 1.0), ("შკვეთა #2", 1.5), ("შკვეთა #3", 2.0)]
#
#
# async def main_dav1():
#     start_seq = time.perf_counter()
#     for order, secs in orders:
#         await deliver(order, secs)
#     end_seq = time.perf_counter()
#     seq_time = end_seq - start_seq
#     print(f"ზედიზედ: {seq_time:.1f} წმ")
#
#     start_gather = time.perf_counter()
#     await asyncio.gather(*(deliver(order, secs) for order, secs in orders))
#     end_gather = time.perf_counter()
#     gather_time = end_gather - start_gather
#     print(f"ერთდროულად: {gather_time:.1f} წმ")
#
#     speedup = seq_time / gather_time if gather_time > 0 else 0
#     print(f"აჩქარება: {speedup:.1f}x")


# dav 1 ratom udris ertdrovuli dro yvelaze grzel shekvetas imis gamoc rom yvelaze nelia imas elodeba boloshi
#
# asyncio.run(main_dav1())
#
#
# async def square(number):
#     await asyncio.sleep(1)
#     return number * number
#
#
# async def main_dav2():
#     numbers = [1, 2, 3, 4, 5, 6, 7, 8]
#
#     start_time = time.perf_counter()
#     squares = await asyncio.gather(*(square(n) for n in numbers))
#     end_time = time.perf_counter()
#
#     for n, s in zip(numbers, squares):
#         print(f"{n}^2 = {s}")
#
#     print(f"ჯამი: {sum(squares)}")
#     print(f"დრო: {end_time - start_time:.1f} წმ")
#
#
# # dav 2 ratom aris 1 wami da ara 8 gather-it ertdrovulad eshveba yvelaperi da sleep-ebi paralelurad gadis
#
# asyncio.run(main_dav2())
#
#
# async def load_user(user_id):
#     await asyncio.sleep(1)
#     return {"id": user_id, "name": f"მომხმარებელი {user_id}"}
#
#
# async def main_dav3():
#     start = time.perf_counter()
#     users = await asyncio.gather(*(load_user(user_id) for user_id in (1, 2, 3)))
#     end = time.perf_counter()
#     print(users)
#     print(f"დრო: {end - start:.1f} წმ")


# dav 3 load_user da main funqciebi unda iyos rom amushavdes da asynqronulad datvirtos
#
# asyncio.run(main_dav3())