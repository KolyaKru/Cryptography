from email import message
import random
from math import pow

a = random.randint(2, 10)

def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)

def generate_key(q):
    key = random.randint(pow(10, 20), q)

    while gcd(q, key) != 1:
        key = random.randint(pow(10, 20), q)
    return key

def power(a, b, c):
    x = 1

    y = a
    
    while b > 0:
        if b % 2 == 0:
            x = (x * y) % c
        
        y = (y * y) % c

        b = int(b/2)

        return x % c

def encrypt(message, q, h, g):
    encrypt_message = []

    k = generate_key(q)

    s = power(h, k, q)

    p = power(g, k, q)

    for i in range(0, len(message)):
        encrypt_message.append(message[i])
    
    print("\ng^k used:\n" + str(p))

    print("\ng^ak used:\n" + str(s))

    for i in range(0, len(encrypt_message)):
        encrypt_message[i] = s * ord(encrypt_message[i])
    
    return encrypt_message,p


def decrypt(encrypt_message, p, key, q):
    decrypt_message = []

    h = power(p, key, q)

    for i in range(0, len(encrypt_message)):

        decrypt_message.append(chr(int(encrypt_message[i]/h)))
    return decrypt_message

def main():
    message = input("Введите шифруемое выражение: \n")

    q = random.randint(pow(10, 20), pow(10, 50))

    g = random.randint(2, q)
    key = generate_key(q)

    h = power(g, key, q)

    print("\ng used:\n" + str(g))

    print("\ng^a used:\n" + str(h))

    encrypt_message, p = encrypt(message, q, h, g)

    decrypt_message = decrypt(encrypt_message, p, key, q)

    dmessage = "".join(decrypt_message)

    print("\nРасшифрованное выражение:\n" + str(dmessage))

if __name__ == "__main__":
    main()


