import socket
from tcp import TCP_segment

PORT = 9792

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', PORT))

SYN_RECEIVED = []
CONNECTED = []

SYN_RECEIVED_SIZE = 7
CONNECTED_SIZE = 7


def add_to_syn_received(request):
    response = TCP_segment() \
        .with_source_port(PORT) \
        .with_destination_port(request.source_port) \
        .with_syn(True)
    sock.sendto(bytearray(str(response), "utf-8"), ('127.0.0.1', request.source_port))
    SYN_RECEIVED.append(request.source_port)
    print('SYN_RECEIVED: ', SYN_RECEIVED)
    print('CONNECTED: ', CONNECTED)
    if len(SYN_RECEIVED) > SYN_RECEIVED_SIZE:
        raise Exception("SYN_RECEIVED is overloaded")


def add_to_connected(request):
    CONNECTED.append(request.source_port)
    SYN_RECEIVED.remove(request.source_port)
    print('SYN_RECEIVED: ', SYN_RECEIVED)
    print('CONNECTED: ', CONNECTED)
    if len(CONNECTED) > CONNECTED_SIZE:
        raise Exception("CONNECTED is overloaded")


while True:
    message = str(sock.recv(2048), "utf-8")
    tcp_segment = TCP_segment.from_string(message)
    if tcp_segment.destination_port != PORT:
        continue
    elif tcp_segment.source_port in CONNECTED:
        continue
    elif tcp_segment.source_port in SYN_RECEIVED:
        add_to_connected(tcp_segment)
    elif tcp_segment.source_port not in SYN_RECEIVED and tcp_segment.ack:
        add_to_syn_received(tcp_segment)

sock.close()
