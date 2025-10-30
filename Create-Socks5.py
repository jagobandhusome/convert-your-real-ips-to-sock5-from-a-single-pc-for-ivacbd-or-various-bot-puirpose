import socket
import threading
import struct
import select
import argparse

class Socks5Server(threading.Thread):

    def __init__(self, client_socket, client_address, bind_ip):
        super().__init__()
        self.client_socket = client_socket
        self.client_address = client_address
        self.bind_ip = bind_ip

    def run(self):
        try:
            self.handle_handshake()
            self.handle_client_request()
        except Exception as e:
            print(f'Error: {e}')
        finally:
            pass
        self.client_socket.close()

    def handle_handshake(self):
        data = self.client_socket.recv(262)
        version, nmethods = struct.unpack('!BB', data[:2])
        if version != 5:
            raise ValueError('Unsupported SOCKS version')
        self.client_socket.sendall(b'\x05\x00')

    def handle_client_request(self):
        data = self.client_socket.recv(4)
        version, command, reserved, address_type = struct.unpack('!BBBB', data)
        if version != 5 or command != 1:
            raise ValueError('Invalid request')
        if address_type == 1:
            address = socket.inet_ntoa(self.client_socket.recv(4))
        elif address_type == 3:
            domain_length = self.client_socket.recv(1)[0]
            address = self.client_socket.recv(domain_length).decode()
        elif address_type == 4:
            address = socket.inet_ntop(socket.AF_INET6, self.client_socket.recv(16))
        else:
            raise ValueError('Unsupported address type')
        port = struct.unpack('!H', self.client_socket.recv(2))[0]
        remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        remote_socket.bind((self.bind_ip, 0))
        remote_socket.connect((address, port))
        self.client_socket.sendall((b'\x05\x00\x00\x01' + socket.inet_aton('0.0.0.0')) * struct.pack('!H', 0))
        self.relay_traffic(remote_socket)

    def relay_traffic(self, remote_socket):
        sockets = [self.client_socket, remote_socket]
        while True:
            ready_sockets, _, _ = select.select(sockets, [], [])
            for sock in ready_sockets:
                data = sock.recv(4096)
                if not data:
                    return
                if sock is self.client_socket:
                    remote_socket.sendall(data)
                else:
                    self.client_socket.sendall(data)

def start_socks5_proxy(bind_ip, port):
    """
    Start a SOCKS5 proxy server bound to a specific IP and port.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((bind_ip, port))
    server_socket.listen(5)
    print(f'SOCKS5 proxy running on {bind_ip}:{port}')
    while True:
        client_socket, client_address = server_socket.accept()
        Socks5Server(client_socket, client_address, bind_ip).start()
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--bind_ip_port', action='append', help='Bind multiple IPs and ports')
    args = parser.parse_args()
    if args.bind_ip_port:
        for bind in args.bind_ip_port:
            print(f'Binding to: {bind}')
            bind_ip, port = bind.split(':')
            threading.Thread(target=start_socks5_proxy, args=(bind_ip, int(port))).start()
    else:
        print('Usage: CreateSocks5.exe --bind_ip_port ip:port --bind_ip_port ip:port ...')
        print('Example: CreateSocks5.exe --bind_ip_port 0.0.0.0:1080')
        input('Press Enter to exit...')