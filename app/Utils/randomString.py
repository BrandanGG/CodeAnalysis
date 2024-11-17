import string
import random
def randString(length:int) -> int:
    char = string.ascii_letters + string.digits
    return ''.join(random.choice(char) for _ in range(length))