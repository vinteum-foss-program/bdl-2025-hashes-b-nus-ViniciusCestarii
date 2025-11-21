import itertools
import sys

def simple_hash(s: str) -> str:
    hash_val = 0
    for char in s:
        hash_val = ((hash_val << 5) - hash_val + ord(char)) & 0xFFFFFFFF
    return f"{hash_val:08x}"

target = "vinicius"
target_hash = simple_hash(target)
chars = [chr(i) for i in range(33, 127)]
length = 8
count = 0

while True:
    for attempt_tuple in itertools.product(chars, repeat=length):
        attempt = "".join(attempt_tuple)
        count += 1

        if count % 500000 == 0:
            print(f"{count}: {attempt}")

        if simple_hash(attempt) == target_hash and attempt != target:
            print(f"Collision found: '{attempt}'")
            sys.exit()
    length += 1