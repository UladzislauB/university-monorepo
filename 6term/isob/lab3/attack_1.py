import socket
from tcp import TCP_segment


def passive_scan():
    """Passive scan"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', 6661))

    target_port = 9792

    tcp_segment = TCP_segment() \
        .with_source_port(6661) \
        .with_destination_port(target_port) \
        .with_syn(True)
    sock.sendto(bytearray(str(tcp_segment), "utf-8"), ('127.0.0.1', target_port))

    message = str(sock.recv(2048), "utf-8")
    tcp_segment = TCP_segment.from_string(message)

    print(f"scanning port: {target_port}", end=' ')
    print(f"ack num: {tcp_segment.ack}")

    sock.close()


if __name__ == "__main__":
    passive_scan()
