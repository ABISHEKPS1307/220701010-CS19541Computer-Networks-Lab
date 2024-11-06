import socket

def start_server():
 
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)  
    server_socket.bind(server_address)
    server_socket.listen(1)  
    print(f"Server listening on {server_address}")

    while True:
  
        connection, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")
        
        try:
            while True:
               
                data = connection.recv(1024)
                if not data:
                    break  
                
                print(f"Received message: {data.decode()} from {client_address}")
                
               
                connection.sendall(data)
                print(f"Echoed message back to {client_address}")

        finally:
           
            connection.close()
            print(f"Connection closed with {client_address}")

if __name__ == "__main__":
    start_server()
