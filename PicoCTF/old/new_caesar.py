import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def b16_encode(plain):
    enc = ""
    for c in plain:
        binary = "{0:08b}".format(ord(c))
        enc += ALPHABET[int(binary[:4], 2)]
        enc += ALPHABET[int(binary[4:], 2)]
    return enc

def b16_decode(enc):
    plain = ""
    for i in range(0, len(enc), 2):
        binary = "{0:04b}{1:04b}".format(ALPHABET.index(enc[i]), ALPHABET.index(enc[i + 1]))
        plain += chr(int(binary[:8], 2))
    return plain

def shift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 + t2) % len(ALPHABET)]

flag = "redacted"
key = "redacted"
# assert all([k in ALPHABET for k in key])
# assert len(key) == 1

# b16 = b16_encode(flag)
# enc = ""
# for i, c in enumerate(b16):
#     enc += shift(c, key[i % len(key)])
# print(enc)

enc = "kjlijdliljhdjdhfkfkhhjkkhhkihlhnhghekfhmhjhkhfhekfkkkjkghghjhlhghmhhhfkikfkfhm"

e16 = b16_decode(enc)
print(e16)  # should print the flag
