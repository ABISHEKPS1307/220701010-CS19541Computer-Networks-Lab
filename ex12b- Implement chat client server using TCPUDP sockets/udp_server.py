import socket

def start_udp_server(host='127.0.0.1', port=65432):
    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    
    print(f"Server listening on {host}:{port}...")
    
    while True:
        data, address = server_socket.recvfrom(1024)
        print(f"Client: {data.decode()}")
        
        message = input("Server: ")
        server_socket.sendto(message.encode(), address)

if __name__ == "__main__":
    start_udp_server()
