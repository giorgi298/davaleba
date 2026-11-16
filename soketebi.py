import socket

# dav 1 serveri
#
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
#     server_socket.bind(("127.0.0.1", 5060))
#     server_socket.listen(1)
#     print("სერვერი ელოდება კლიენტს...")
#
#     conn, addr = server_socket.accept()
#     with conn:
#         data = conn.recv(1024)
#         text = data.decode("utf-8")
#         print(f"მივიღეთ: {text}")
#
#         response = text.upper()
#         conn.sendall(response.encode("utf-8"))
#         print("სერვერი დასრულდა")

# dav 2 klienturi nawili

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
#     client_socket.connect(("127.0.0.1", 5060))
#     message = "hello socket"
#     client_socket.sendall(message.encode("utf-8"))
#
#     response_data = client_socket.recv(1024)
#     print(f"პასუხი: {response_data.decode('utf-8')}")