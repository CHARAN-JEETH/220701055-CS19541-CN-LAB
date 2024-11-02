import socket

def udp_chat_server(host='localhost', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"UDP Chat Server running on {host}:{port}")

    while True:
        message, addr = server_socket.recvfrom(1024)
        print(f"Received from {addr}: {message.decode('utf-8')}")
        # Echo the message back to the sender
        server_socket.sendto(message, addr)

if __name__ == "__main__":
    udp_chat_server()
