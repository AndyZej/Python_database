import re

def check_dice(text: str) -> bool:
    pattern = r'\b\d*[dD]\d+([+-]\d+)?\b'
    return bool(re.search(pattern, text))

check_dice("8d7+10")                 # True
check_dice("8s7+10")                 # False
check_dice("8D7+10 abcdefghijk")     # True
check_dice("8d-h")                   # False
check_dice("D6")                     # True