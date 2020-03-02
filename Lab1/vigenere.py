from main_task import alphabet

standart_key = "MNBVTGUHIJKLFKEIUYTFVTRDEWQASZXSSD" \
               "FCVBNMLPOIUYHNMLIUYTFGHJKUYGFCGVHB" \
               "NJMKUYGFRDEXDCFCSXWEDRFGHBJNIMIMKG" \
               "GMFUTQWPMVBCXFGHVBGHDAPLUTYWHGBDNV"

a_len = len(alphabet)
letter_num = {alphabet[index]: index for index in range(a_len)}
vigenere_table = [0] * a_len
for index in range(a_len):
    new_row = [alphabet[(x+index) % a_len] for x in range(a_len)]
    vigenere_table[index] = new_row


def encode(message: str, key: str = standart_key) -> str:
    new_key = key
    while len(new_key) < len(message):
        new_key += key
    key = new_key[:len(message)]

    encoded_msg = "".join([alphabet[(letter_num[letter] + letter_num[key[index]]) % a_len] for index, letter in enumerate(message)])
    return encoded_msg


def decode(message: str, key: str = standart_key) -> str:
    new_key = key
    while len(new_key) < len(message):
        new_key += key
    key = new_key[:len(message)]
    decoded_msg = "".join([alphabet[(letter_num[letter] + a_len - letter_num[key[index]]) % a_len] for index, letter in enumerate(message)])
    return decoded_msg


if __name__ == '__main__':
    print('Vigenere table: ')
    for index in range(a_len):
        print(index, vigenere_table[index])
    msg = 'ALLYOUNEEDISLOVE'
    new_msg = encode(msg, 'LMHSLM')
    print('Test encode:', msg, "->", new_msg)
    print('Test decode:', new_msg, "->", decode(new_msg, 'LMHSLM'))




