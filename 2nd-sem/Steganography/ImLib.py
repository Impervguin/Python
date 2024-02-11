from PIL import Image
import StringBits as sb
OK = 0
SMALL_FILE = 1
FILE_NOT_FOUND = 2

def encode_in_image(text, file):
    try:
        im = Image.open(file)
    except FileNotFoundError:
        return (FILE_NOT_FOUND, None)

    size = im.size
    n_pixels = size[0] * size[1]
    max_n_bits = n_pixels * 3
    bits = sb.string_to_bits(text)
    l_bits = len(bits)
    if l_bits > max_n_bits:
        return (SMALL_FILE, None)
    i = 0
    next_bit = bits[i]
    for x in range(size[0]):
        for y in range(size[1]):
            rgb = im.getpixel((x, y))
            new = []
            for col in rgb:
                new.append(col if col % 2 == next_bit else col - 1)
                if i < l_bits - 1:
                    i += 1
                    next_bit = bits[i]
                else:
                    next_bit = 0
            im.putpixel((x, y), tuple(new))
    return (OK, im)

def decode_image(file):
    try:
        im = Image.open(file)
    except FileNotFoundError:
        return (FILE_NOT_FOUND, None)
    bits = []
    size = im.size
    for x in range(size[0]):
        for y in range(size[1]):
            rgb = im.getpixel((x, y))
            bits.extend([i % 2 for i in rgb])
    text = sb.bits_to_string(bits)
    return (OK, text)
