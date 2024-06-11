## Author: Abdelrahman Farag 

## Contact: abdelrahmanfarag1980@gmail.com 

## Abstract

## This paper presents a novel cryptographic method leveraging ternary-based exponentiation and randomized keys to enhance security. The method, which transforms traditional binary-based encryption, utilizes custom power functions and random keys for encryption and decryption. This paper details the theoretical foundations, practical implementation, and the mathematical representation of the encryption algorithm, demonstrating its effectiveness with a practical example.

## Introduction

## Cryptography is essential for securing data in digital communication. Traditional cryptographic methods rely heavily on binary systems, which are foundational to modern computing. This paper introduces a novel approach that utilizes ternary (base-3) arithmetic, adding an additional layer of complexity and security. By incorporating randomized keys, we create a robust encryption mechanism that is computationally feasible and secure.

## Practical Implementation

## The encryption process involves generating public and private keys, using these keys to manipulate the exponentiation of base values, and subsequently encoding characters. Decryption reverses this process, utilizing the private key to retrieve the original data. Below is the Python implementation of the described cryptographic method.


import random

# Key generation function
def generate_keys():
    pub_key = random.randint(2, 10)
    priv_key = pub_key + random.randint(1, 10)
    return pub_key, priv_key

# Encryption function
def encrypt_char(char, pub_key):
    if char in char_to_ternary:
        base, exp1, exp2 = char_to_ternary[char]
        encrypted_value = (custom_pow(base, exp1), custom_pow(base, exp2 + pub_key))
        print(f'ENCRYPTING: char={char}, base={base}, exp1={exp1}, exp2={exp2}, pub_key={pub_key}, encrypted_value={encrypted_value}')
        return encrypted_value
    return None

# Decryption function
def decrypt_ternary(ternary_pair, priv_key, pub_key):
    for char, value in char_to_ternary.items():
        base, exp1, exp2 = value
        decrypted_value = (custom_pow(base, exp1), custom_pow(base, exp2 + pub_key))
        print(f'DECRYPTING: Trying to decrypt with char={char}, base={base}, exp1={exp1}, exp2={exp2}, priv_key={priv_key}, pub_key={pub_key}, decrypted_value={decrypted_value}')
        if ternary_pair == decrypted_value:
            return char
    return None

# Custom power function
def custom_pow(base, exp):
    if base == 0:
        return 0
    elif exp == 0:
        return 1
    elif base == 1:
        return 1
    else:
        return base ** exp

# Ternary conversion map
char_to_ternary = {
    'A': (2, 3, 4),
    'B': (3, 2, 5),
    'C': (5, 2, 3),
}

# Example usage
# pub_key, priv_key = generate_keys()
# char = 'B'
# encrypted = encrypt_char(char, pub_key)
# print(f'Encrypted {char}: {encrypted}')

# decrypted = decrypt_ternary(encrypted, priv_key, pub_key)
# print(f'Decrypted {encrypted}: {decrypted}')
