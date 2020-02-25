class Caesar:
    @staticmethod
    def code_and_dec(text, key):
        alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        result = ""
        for char in text:
            index = alphabet.find(char.upper())
            if index < 0:
                result += char
            else:
                code_index = (index + key) % len(alphabet)
                if code_index < 0:
                    code_index += len(alphabet)
                if char.islower():
                    result += result[code_index].lower()
                else:
                    result += alphabet[code_index]
        return result

    @staticmethod
    def code(text, key):
        return Caesar.code_and_dec(text, key)

    @staticmethod
    def decode(text, key):
        return Caesar.code_and_dec(text, -key)
