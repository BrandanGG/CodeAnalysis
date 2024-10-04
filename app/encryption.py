import bcrypt
########################
### Password Hashing ###
########################

def hash_pw(password:str) -> bytes:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(rounds=15))

def check_pw(password:str, stored_hash:str) -> bool:
    return bcrypt.check_pw(password.encode('utf-8'), stored_hash)
