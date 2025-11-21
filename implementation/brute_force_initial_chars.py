import itertools
import sys
import hashlib

def sha256(s: str) -> str:
    full_hash = hashlib.sha256(s.encode('utf-8')).hexdigest()
    return full_hash

targets = ["cafe", "faded", "decade"]
chars = [chr(i) for i in range(32, 127)]
length = 1
count = 0

founds = set()

while True:
    for attempt_tuple in itertools.product(chars, repeat=length):
        attempt = "bitcoin" + "".join(attempt_tuple)
        count += 1

        if count % 500000 == 0:
            print(f"{count}: {attempt}")
        hash = sha256(attempt)

        for target in targets:
            if hash.startswith(f"{target}") and target not in founds:
                founds.add(target)
                print(f"Initial chars found: {attempt} for target {target}")
            
            if len(founds) == len(targets):
                sys.exit()
    length += 1