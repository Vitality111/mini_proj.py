# pass generation

import random
import string

def main(lengh = 12):
    character = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(character) for _ in range(lengh + 1))
    
    return password

generete = main(15)
print(generete)

