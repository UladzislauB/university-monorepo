class Vigener:
    @staticmethod
    def get_key(text, length):
        temp = text
        while len(temp) < length:
            temp += text
        return temp[:length]

    @staticmethod
    def code_and_dec(text, key, flag):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        password = Vigener.get_key(key, len(text))
        result = ""
        q = len(alphabet)

        index = 0

        for char in text:
            text_index = alphabet.find(char.upper())
            key_index = alphabet.find(password[index].upper())
            if text_index < 0:
                result += char
            else:
                result += alphabet[(q + text_index + flag * key_index) % q]
            index += 1
        return result

    @staticmethod
    def code(text, key):
        return Vigener.code_and_dec(text, key, 1)

    @staticmethod
    def decode(text, key):
        return Vigener.code_and_dec(text, key, -1)
