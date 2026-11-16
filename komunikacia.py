
# dav 1

# import requests
#
# def get_user(user_id):
#     url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()
#     elif response.status_code == 404:
#         return None
#     else:
#         response.raise_for_status()
#
# for uid in [1, 2, 999]:
#     try:
#         user = get_user(uid)
#         if user:
#             print(f"{user['name']} | {user['email']} | {user['address']['city']}")
#         else:
#             print(f"მომხმარებელი {uid} ვერ მოიძებნა")
#     except Exception as e:
#         print(f"Error: {e}")import requests
#
# def get_user(user_id):
#     url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()
#     elif response.status_code == 404:
#         return None
#     else:
#         response.raise_for_status()
#
# for uid in [1, 2, 999]:
#     try:
#         user = get_user(uid)
#         if user:
#             print(f"{user['name']} | {user['email']} | {user['address']['city']}")
#         else:
#             print(f"მომხმარებელი {uid} ვერ მოიძებნა")
#     except Exception as e:
#         print(f"Error: {e}")

# dav 2

import requests


def crud_tour():
    base_url = "https://jsonplaceholder.typicode.com"

    create_res = requests.post(f"{base_url}/posts", json={"title": "ახალი პოსტი", "body": "ტექსტი", "userId": 1})
    create_data = create_res.json()
    print(f"CREATE: {create_res.status_code}, id={create_data.get('id')}")

    new_id = create_data.get('id')
    read_res = requests.get(f"{base_url}/posts/{new_id}")
    print(f"READ {new_id}: {read_res.status_code}")

    put_res = requests.put(f"{base_url}/posts/1", json={"title": "სრულიად შეცვლილი", "body": "ტექსტი", "userId": 1})
    put_data = put_res.json()
    print(f"UPDATE (PUT): {put_res.status_code}, title={put_data.get('title')}")

    patch_res = requests.patch(f"{base_url}/posts/1", json={"title": "ნაწილობრივ შეცვლილი"})
    patch_data = patch_res.json()
    print(f"UPDATE (PATCH): {patch_res.status_code}, title={patch_data.get('title')}")

    delete_res = requests.delete(f"{base_url}/posts/1")
    print(f"DELETE: {delete_res.status_code}, {delete_res.json()}")


crud_tour()