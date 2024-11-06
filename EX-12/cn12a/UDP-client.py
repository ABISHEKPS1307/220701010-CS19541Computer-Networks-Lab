import socket

def start_client():

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 12345)  # Server address (same as server's address)
    
    while True:

        message = input("Enter message to send (or 'exit' to quit): ")
        if message.lower() == 'exit':
            print("Exiting...")
            break

        client_socket.sendto(message.encode(), server_address)

        response, _ = client_socket.recvfrom(4096)
        print(f"Received from server: {response.decode()}")

    client_socket.close()

if __name__ == "__main__":
    start_client()
