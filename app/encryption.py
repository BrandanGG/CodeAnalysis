import bcrypt
import hashlib
import base64
########################
### Password Hashing ###
########################

def hash_pw(password: str) -> bytes:
    # Encode password to bytes, then hash with SHA-256, and base64 encode the result
    sha256_hash = hashlib.sha256(password.encode('utf-8')).digest()
    base64_hash = base64.b64encode(sha256_hash)
    
    # Use bcrypt to hash the base64-encoded SHA-256 result
    return bcrypt.hashpw(base64_hash, bcrypt.gensalt(rounds=15))


def check_pw(password:str, stored_hash:bytes) -> bool:
    # Hash the entered password with SHA-256, then check with bcrypt
    sha256_hash = hashlib.sha256(password.encode('utf-8')).digest()
    base64_hash = base64.b64encode(sha256_hash)
    print(f"SHA-256 base64 hash of entered password: {base64_hash}")  # Debug statement
    return bcrypt.checkpw(base64_hash, stored_hash)