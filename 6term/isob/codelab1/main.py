from caesar import Caesar
from vigener import Vigener

if __name__ == "__main__":
    text = "ATTACKATDAWN"
    key_caesar = 3
    key_vigener = "LEMON"
    encoded_caesar = Caesar.code(text, key_caesar)
    encoded_vigener = Vigener.code(text, key_vigener)
    print("Encoded caesar:", encoded_caesar)
    print("Encoded vigener:", encoded_vigener)
    print("Decoded caesar:", Caesar.code(encoded_caesar, key_caesar))
    print("Decoded vigener:", Vigener.code(encoded_vigener, key_vigener))
