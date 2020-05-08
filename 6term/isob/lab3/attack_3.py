import socket
from tcp import TCP_segment


def flood_connection():
    """TCP Full Connection Flooding"""
    for i in range(20):
        port = 10001 + i
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('', port))
        resp = TCP_segment() \
            .with_source_port(port) \
            .with_destination_port(9792) \
            .with_syn(True)
        sock.sendto(bytearray(str(resp), "utf-8"), ('127.0.0.1', 9792))

        message = str(sock.recv(2048), "utf-8")
        tcp_segment = TCP_segment.from_string(message)

        print(f"source port: {port}", end='\t')
        print(f"ack num: {tcp_segment.ack}")

        resp = TCP_segment() \
            .with_source_port(port) \
            .with_destination_port(9792)
        sock.sendto(bytearray(str(resp), "utf-8"), ('127.0.0.1', 9792))
        sock.close()


if __name__ == '__main__':
    flood_connection()
