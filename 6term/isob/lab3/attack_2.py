import socket
from tcp import TCP_segment


def syn_flooding():
    """SYN Flooding"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', 6662))
    for i in range(20):
        port = 10001 + i
        tcp_segment = TCP_segment() \
            .with_source_port(port) \
            .with_destination_port(9792) \
            .with_syn(True)
        print(f"source port: {port}")
        sock.sendto(bytearray(str(tcp_segment), "utf-8"), ('127.0.0.1', 9792))
    sock.close()


if __name__ == "__main__":
    syn_flooding()
