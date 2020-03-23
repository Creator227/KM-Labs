from main_task import alphabet
from vigenere import letter_num, a_len

possible_keys = {3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25}

code_dict = {}
decode_dict = {}
current_key = 0


def prepare_encoding(key: int):
    for letter_index in range(0, a_len):
        code_index = (letter_index * key + 2) % a_len
        code_dict[alphabet[letter_index]] = alphabet[code_index]
        global decode_dict
        decode_dict = {x: y for y, x in code_dict.items()}


def encode(message: str, key: int) -> str:
    if key not in possible_keys:
        raise ArithmeticError
    prepare_encoding(key)
    encoded_msg = "".join([code_dict[i] for i in message])
    return encoded_msg


def decode(message: str, key: int) -> str:
    if current_key != key:
        prepare_encoding(key)
    decoded_msg = "".join([decode_dict[i] for i in message])
    return decoded_msg


if __name__ == '__main__':
    test_msg = "ABCDEFGQWERTY"
    print("Affine encoding of {}:".format(test_msg), encode(test_msg, 5))
    print("Decoding:", decode(encode(test_msg, 5), 5))

