import socket

def start_client():

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)  # Server address (same as server's address)

    client_socket.connect(server_address)
    print(f"Connected to server at {server_address}")

    while True:

        message = input("Enter message to send (or 'exit' to quit): ")
        if message.lower() == 'exit':
            print("Exiting...")
            break

        client_socket.sendall(message.encode())

        response = client_socket.recv(1024)
        print(f"Received from server: {response.decode()}")


    client_socket.close()

if __name__ == "__main__":
    start_client()
