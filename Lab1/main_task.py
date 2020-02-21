import random

alphabet = (
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
    'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
    'S', 'T', 'U', 'V', "W", 'X', 'Y', 'Z')
tokens = (' ', ':', ';', '/', '.', '!', '&', '?', '#', '@')

transposition = list(alphabet)

for _ in range(26):
    index = random.randint(0, 25)
    transposition[index], transposition[-index] = transposition[-index], transposition[index]

encode_transposition = {alphabet[i]: transposition[i] for i in range(26)}

decode_transposition = {transposition[i]: alphabet[i] for i in range(26)}


def encode(message: str) -> str:
    encode_msg = ""
    for i in message:
        if i not in tokens:
            encode_msg += encode_transposition[i]
        else:
            encode_msg += i
    return encode_msg


def decode(message: str) -> str:
    decode_msg = ""
    for i in message:
        if i not in tokens:
            decode_msg += encode_transposition[i]
        else:
            decode_msg += i
    return decode_msg


if __name__ == '__main__':
    print("Alphabet for encode: ", alphabet)
    print("Encoding key: ", transposition)
    print("Encode transposition: ", encode_transposition)
    print("Decode transposition: ", decode_transposition)
    print("Code of ABCDEFG", encode("ABCDEFG"))
