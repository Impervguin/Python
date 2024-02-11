PART_LENGTH = 8
DESICION_BIT = PART_LENGTH - 1

def string_to_bits(string):
    bit_str = []
    for char in string:
        bit_str.extend(char_to_bits(char))
    return bit_str


def char_to_bits(char):
    bits = []
    part = [0] * PART_LENGTH
    num_bits = 0
    n_char = ord(char)
    while n_char > 0:
        if num_bits == DESICION_BIT:
            num_bits = 0
            part[DESICION_BIT] = 0
            bits.extend(part)
            part = [0] * PART_LENGTH
        part[num_bits] = n_char % 2
        n_char //= 2
        num_bits += 1
    part[DESICION_BIT] = 1
    bits.extend(part)
    return bits


def bits_to_char(bits):
    bit_mult = 1
    n_char = 0
    for i in range(1, len(bits) + 1):
        if i % PART_LENGTH == 0:
            continue
        n_char += bit_mult * bits[i - 1]
        bit_mult *= 2
    return chr(n_char)



def bits_to_string(bits):
    string = ""
    now_chr_start = 0
    bits = clean_bits_tail(bits)
    for i in range(1, len(bits) + 1):
        if i % PART_LENGTH == 0 and bits[i - 1] == 1:
            string += bits_to_char(bits[now_chr_start:i])
            now_chr_start = i
    string += bits_to_char(bits[now_chr_start:i])
    return string


def clean_bits_tail(bits):
    first_tail_bit = len(bits) - 1
    while bits[first_tail_bit] != 1:
        first_tail_bit -= 1
    return bits[:first_tail_bit + 1]
