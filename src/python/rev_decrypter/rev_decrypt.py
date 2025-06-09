import os
import random
import argparse

def ror(val, r_bits):
    return ((val & 0xFF) >> r_bits | (val << (8 - r_bits)) & 0xFF) & 0xFF


def process_char(b):
    orig = ror(b, 2)
    for c in range(65, 91):
        if ((-101 - c) | 0x20) & 0xFF == orig:
            return c
    for c in range(97, 123):
        if ((-37 - c) ^ 0x20) & 0xFF == orig:
            return c
    for c in range(48, 58):
        if (105 - c) & 0xFF == orig:
            return c
    return orig

def decrypt_txt_file(data):
    return bytes([process_char(b) for b in data])

def decrypt_docx_file(data):
    decrypted = bytearray()
    for b in data:
        step1 = b ^ 0xC1
        step2 = (step1 + 77) & 0xFF
        step3 = step2 ^ 0x8B
        orig = (step3 - 5) & 0xFF
        decrypted.append(orig)
    return bytes(decrypted)



def decrypt_png_file(data):
    return bytes([((ror(b, 4)) ^ 0x44) for b in data])

def decrypt_jpg_file(data):
    charset = b"AkjsSHwiE27.[$+#"
    char_to_index = {c: i for i, c in enumerate(charset)}

    decrypted = bytearray()
    for i in range(0, len(data), 2):
        high = char_to_index.get(data[i])
        low = char_to_index.get(data[i + 1])
        if high is None or low is None:
            raise ValueError(f"invalid byte : {data[i:i+2]}")
        byte = (high << 4) | low
        decrypted.append(byte)
    return bytes(decrypted)


class Rand:
    def __init__(self, seed):
        self.state = seed

    def rand(self):
        self.state = (self.state * 0x343FD + 0x269EC3) & 0x7FFFFFFF
        return (self.state >> 16) & 0x7FFF


def decrypt_pdf_file(data):
    decrypted = bytearray()
    prng = Rand(len(data))
    prev = 0
    for i in range(len(data)):
        rnd = prng.rand() & 0xFF
        enc = data[i]
        dec = (enc - prev) ^ rnd
        decrypted.append(dec & 0xFF)
        prev = enc
    return bytes(decrypted)




def decrypt(input_file, output_file):
    ext = os.path.splitext(input_file)[1].lower()
    with open(input_file, 'rb') as f:
        data = f.read()

    if ext == '.txt':
        decrypted = decrypt_txt_file(data)
    elif ext == '.docx':
        decrypted = decrypt_docx_file(data)
    elif ext == '.png':
        decrypted = decrypt_png_file(data)
    elif ext == '.pdf':
        decrypted = decrypt_pdf_file(data)
    elif ext == '.jpg':
        decrypted = decrypt_jpg_file(data)
    else:
        decrypted = b"wrong type"

    with open(output_file, 'wb') as f:
        f.write(decrypted)


def main():
    parser = argparse.ArgumentParser(prog='rev_dec')
    parser.add_argument(
        'in_file', help="file to decode", type=str)
    parser.add_argument(
        'out_file', help="output path", type=str)
    args = parser.parse_args()
    decrypt(args.in_file,args.out_file)
    
if __name__ == "__main__":
    main()


