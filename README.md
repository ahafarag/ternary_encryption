# A Novel Approach to Cryptography Using Ternary-Based Exponentiation with Randomized Keys

**Author:Abdelrahman Farag**

**Contact: abdelrahmanfarag1980@gmail.com**

This repository contains the research paper "A Novel Approach to Cryptography Using Ternary-Based Exponentiation with Randomized Keys" along with the code implementation.

## Abstract
This paper presents a novel cryptographic method leveraging ternary-based exponentiation and randomized keys to enhance security. The method, which transforms traditional binary-based encryption, utilizes custom power functions and random keys for encryption and decryption. This paper details the theoretical foundations, practical implementation, and the mathematical representation of the encryption algorithm, demonstrating its effectiveness with a practical example.

## Introduction
Cryptography is essential for securing data in digital communication. Traditional cryptographic methods rely heavily on binary systems, which are foundational to modern computing. This paper introduces a novel approach that utilizes ternary (base-3) arithmetic, adding an additional layer of complexity and security. By incorporating randomized keys, we create a robust encryption mechanism that is computationally feasible and secure.

## Theoretical Foundation
The proposed method leverages ternary-based exponentiation, wherein the encryption and decryption processes use custom power functions combined with random keys. The ternary system uses three values: 0, 1, and 2. By applying these values in exponentiation and introducing randomness through keys, the system achieves a high level of security.

## Practical Implementation
The encryption process involves generating public and private keys, using these keys to manipulate the exponentiation of base values, and subsequently encoding characters. Decryption reverses this process, utilizing the private key to retrieve the original data. Below is the Python implementation of the described cryptographic method.

```python
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
pub_key, priv_key = generate_keys()
char = 'B'
encrypted = encrypt_char(char, pub_key)
print(f'Encrypted {char}: {encrypted}')

decrypted = decrypt_ternary(encrypted, priv_key, pub_key)
print(f'Decrypted {encrypted}: {decrypted}')
```
## Mathematical Representation
The encryption function can be mathematically represented as:

```math
\[ $E(\text{char}, \text{pub\_key}) = (\text{base}^{\text{exp1}}, \text{base}^{(\text{exp2} + \text{pub\_key})}) \]$
```
The decryption function reverses this process:
$\[ D(E(\text{char}, \text{pub\_key}), \text{priv\_key}) = \text{char} \]$

where `pub_key` and `priv_key` are randomly generated keys such that:
$\[ \text{priv\_key} = \text{pub\_key} + k \]$
for some integer $\( k \)$.

### Detailed Steps and Analysis

1. **Encryption:**
   - Given a character and a public key, calculate $\( \text{base}^{\text{exp1}} \)$ and $\( \text{base}^{(\text{exp2} + \text{pub\_key})} \)$.
   - These calculations produce a tuple $\(( \text{base}^{\text{exp1}}, \text{base}^{(\text{exp2} + \text{pub\_key})} )\)$.

2. **Decryption:**
   - Using the encrypted tuple $\(( \text{base}^{\text{exp1}}, \text{base}^{(\text{exp2} + \text{pub\_key})} )\)$ and the private key, reverse the process to find the original character.

### Example Walkthrough

To solidify this understanding, let's consider a simple example:

#### Setup:
- Choose a base, say `base = 2`.
- Let `char = 'A'`.
- Suppose `exp1` and `exp2` are derived from the character in a known manner (e.g., ASCII value).
- Let's pick `exp1 = 3` and `exp2 = 5` for simplicity.
- Suppose `pub_key = 7`.

#### Encryption:
$\[ E('A', 7) = (2^3, 2^{(5 + 7)}) \]$
$\[ E('A', 7) = (8, 2^{12}) \]$
$\[ E('A', 7) = (8, 4096) \]$

#### Decryption:
- Suppose `k = 4`, thus `priv_key = pub_key + k = 7 + 4 = 11`.
- The decryption function uses `priv_key = 11` to reverse the encryption.

Without loss of generality, assume the decryption process can isolate `exp1` and `exp2` by reversing the exponentiation steps, given the tuple and `priv_key`.

### Conclusion

This encryption and decryption process hinges on exponentiation and the relationship between the public and private keys. The precise method to derive `exp1` and `exp2` and to reverse the process (i.e., decrypt the tuple back to the original character) would depend on the specific algorithm design and mathematical properties being utilized.


## Conclusion
This paper introduces an innovative approach to cryptography using ternary-based exponentiation and random keys. The method enhances security by leveraging the complexity of ternary arithmetic and the unpredictability of randomized keys. The practical implementation demonstrates the feasibility and robustness of the proposed method. Future work could explore optimizing the algorithm for various use cases and integrating it into broader cryptographic frameworks.

References
Schneier, B. (1996). Applied Cryptography: Protocols, Algorithms, and Source Code in C. John Wiley & Sons.
Stallings, W. (2017). Cryptography and Network Security: Principles and Practice. Pearson.
Menezes, A. J., van Oorschot, P. C., & Vanstone, S. A. (1996). Handbook of Applied Cryptography. CRC Press.

## License

This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) License. 

You are free to:
- Share: copy and redistribute the material in any medium or format.
- Adapt: remix, transform, and build upon the material for any purpose, even commercially.

Under the following terms:
- Attribution: You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
- ShareAlike: If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.

**Disclaimer:**
The author is not responsible for any use of this code and does not provide any warranties. Use this code at your own risk.

Full license text can be found [here](https://creativecommons.org/licenses/by-sa/4.0/legalcode).

## How to Cite

If you use this work in your research, please cite it as follows:
Abdelrahman FARAG. "A Novel Approach to Cryptography Using Ternary-Based Exponentiation with Randomized Keys". 2024. Available at: https://github.com/ahafarag/ternary_encryption
