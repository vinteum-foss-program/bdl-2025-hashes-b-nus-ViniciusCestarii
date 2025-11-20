import random
import string

def simple_hash(s: str) -> str:
    hash_val = 0
    for char in s:
        hash_val = ((hash_val << 5) - hash_val + ord(char)) & 0xFFFFFFFF
    return f"{hash_val:08x}"

seen = {}
chars = string.ascii_letters + string.digits
i = 0

while True:
    i += 1
    s = "".join(random.choices(chars, k=8))
    h = simple_hash(s)
    
    if h in seen and seen[h] != s:
        print(f"Collision between {h}, {s} in {i} iterations.")
        break
    seen[h] = s