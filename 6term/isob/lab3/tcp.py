class TCP_segment():
    def __init__(self):
        self.source_port = 0
        self.destination_port = 0
        self.sequence_number = 0
        self.acknowledgment_number = 0
        self.urg = 0
        self.ack = 0
        self.psh = 0
        self.rst = 0
        self.syn = 0
        self.fin = 0
        self.data = ''

    def with_source_port(self, value):
        self.source_port = value
        return self

    def with_destination_port(self, value):
        self.destination_port = value
        return self

    def with_sequence_number(self, value):
        self.sequence_number = value
        return self

    def with_acknowledgment_number(self, value):
        self.acknowledgment_number = value
        return self

    def with_urg(self, value):
        self.urg = value
        return self

    def with_ack(self, value):
        self.ack = value
        return self

    def with_psh(self, value):
        self.psh = value
        return self

    def with_rst(self, value):
        self.rst = value
        return self

    def with_syn(self, value):
        self.syn = value
        return self

    def with_fin(self, value):
        self.fin = value
        return self

    def with_data(self, value):
        self.data = value
        return self

    def get_string(self):
        array = '{0:016b}'.format(self.source_port) \
                + '{0:016b}'.format(self.destination_port) \
                + '{0:032b}'.format(self.sequence_number) \
                + '{0:032b}'.format(self.acknowledgment_number) \
                + '0' * (4 + 6) \
                + str(int(self.urg)) \
                + str(int(self.ack)) \
                + str(int(self.psh)) \
                + str(int(self.rst)) \
                + str(int(self.syn)) \
                + str(int(self.fin)) \
                + '0' * (16 + 16 + 16) \
                + to_bits(self.data)

        return array

    def __str__(self):
        return self.get_string()

    @staticmethod
    def from_string(_string):
        obj = TCP_segment()

        return obj \
            .with_source_port(int(_string[0:16], 2)) \
            .with_destination_port(int(_string[16:32], 2)) \
            .with_sequence_number(int(_string[32:64], 2)) \
            .with_acknowledgment_number(int(_string[64:96], 2)) \
            .with_urg(bool(_string[106])) \
            .with_ack(bool(_string[107])) \
            .with_psh(bool(_string[108])) \
            .with_rst(bool(_string[109])) \
            .with_syn(bool(_string[110])) \
            .with_fin(bool(_string[111])) \
            .with_data(from_bits(_string[160:]))


def to_bits(s):
    result = ''
    for c in s:
        bits = bin(ord(c))[2:]
        result += '00000000'[len(bits):] + bits
    return result


def from_bits(bits):
    chars = []
    for b in range(int(len(bits) / 8)):
        byte = bits[b * 8:(b + 1) * 8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)

# mes = 'success'
# bits = to_bits(mes)
# print(bits)
# print(from_bits(bits))
