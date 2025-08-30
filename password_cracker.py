import hashlib

def crack_sha1_hash(hash_to_crack, use_salts=False):
    # Abrimos la lista de passwords
    with open("top-10000-passwords.txt", "r", encoding="utf-8") as f:
        passwords = [line.strip() for line in f]

    if not use_salts:
        # Caso sin salts
        for password in passwords:
            hashed = hashlib.sha1(password.encode()).hexdigest()
            if hashed == hash_to_crack:
                return password
    else:
        # Cargamos las salts
        with open("known-salts.txt", "r", encoding="utf-8") as f:
            salts = [line.strip() for line in f]

        # Probamos todas las combinaciones salt+password y password+salt
        for password in passwords:
            for salt in salts:
                # Salt antes
                hashed1 = hashlib.sha1((salt + password).encode()).hexdigest()
                if hashed1 == hash_to_crack:
                    return password

                # Salt después
                hashed2 = hashlib.sha1((password + salt).encode()).hexdigest()
                if hashed2 == hash_to_crack:
                    return password

    return "PASSWORD NOT IN DATABASE"

#print(crack_sha1_hash("5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8")) #returns password
#print(crack_sha1_hash("53d8b3dc9d39f0184144674e310185e41a87ffd5", use_salts=True)) # returns superman