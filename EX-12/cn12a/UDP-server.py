import socket

def start_server():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 12345)  # Server listens on port 12345
    server_socket.bind(server_address)
    print(f"Server listening on {server_address}")

    while True:
    
        message, client_address = server_socket.recvfrom(4096)
        print(f"Received message: {message.decode()} from {client_address}")

        server_socket.sendto(message, client_address)
        print(f"Echoed message back to {client_address}")

if __name__ == "__main__":
    start_server()
