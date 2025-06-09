import argparse

def rol32(value: int, bits: int) -> int:
    return ((value << bits) | (value >> (32 - bits))) & 0xFFFFFFFF

def swap_al_ah(value: int) -> int:
    al = value & 0xFF
    ah = (value >> 8) & 0xFF
    return (value & 0xFFFF0000) | (al << 8) | ah

def process_char(state: int, char: str) -> int:
    state = rol32(state, 5)
    state = swap_al_ah(state)
    state ^= 0xC8FA7B6E
    state = (state + ord(char)) & 0xFFFFFFFF
    return state

def generate(input_string: str) -> int:
    state = 0
    for char in input_string:
        if char == '\0':
            break
        state = process_char(state, char)
    return state


charset = b'aOpWqnRsEhXyCvJt'
index_Array = [
    0x2, 0x3, 0x6, 0xA,
    0x1, 0x4, 0xF, 0xB,
    0x9, 0xE, 0x5, 0xD,
    0x7, 0x8, 0xC, 0x0
]

index_to_char = {val: chr(charset[i]) for i, val in enumerate(index_Array)}

def encode(target_hash):
    value = target_hash
    encoded = []
    for _ in range(8):
        value ^= 0xA
        nibble = value & 0xF
        if nibble not in index_to_char:
            return None
        encoded.append(index_to_char[nibble])
        value >>= 4
    return ''.join(reversed(encoded))




def main():
    parser = argparse.ArgumentParser(prog='keygen')
    parser.add_argument(
        'username', help="User for which to generate password", type=str)
    args = parser.parse_args()
    correct_hash = generate(args.username)
    password = encode(correct_hash)
    print(password,hex(correct_hash))
    
if __name__ == "__main__":
    main()