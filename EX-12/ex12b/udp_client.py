import socket

def start_udp_client(host='127.0.0.1', port=65432):
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        message = input("Client: ")
        client_socket.sendto(message.encode(), (host, port))  
        
        data, server = client_socket.recvfrom(1024)  
        print(f"Server: {data.decode()}")

if __name__ == "__main__":
    start_udp_client()
