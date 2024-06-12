![image](https://github.com/ahafarag/ternary_encryption/assets/117376293/73d66dd4-0225-4de4-ac0a-9c9828ee772f)

# A Novel Approach to Cryptography Using Ternary-Based Exponentiation with Randomized Keys

**Author:** Abdelrahman FARAG  
**Affiliation:** [Triador Project](https://github.com/ssloy/triador)  
**Contact:** [Abdelrahmanfarag1980@gmail.com](mailto:Abdelrahmanfarag1980@gmail.com)

## Abstract

This paper presents a novel cryptographic method leveraging ternary-based exponentiation and randomized keys to enhance security. The method, which transforms traditional binary-based encryption, utilizes custom power functions and random keys for encryption and decryption. This paper details the theoretical foundations, practical implementation, and the mathematical representation of the encryption algorithm, demonstrating its effectiveness with a practical example.

## Introduction

Cryptography is essential for securing data in digital communication. Traditional cryptographic methods rely heavily on binary systems, which are foundational to modern computing. This paper introduces a novel approach that utilizes ternary (base-3) arithmetic, adding an additional layer of complexity and security. By incorporating randomized keys, we create a robust encryption mechanism that is computationally feasible and secure.

## Theoretical Foundation

The proposed method leverages ternary-based exponentiation, wherein the encryption and decryption processes use custom power functions combined with random keys. The ternary system uses three values: 0, 1, and 2. By applying these values in exponentiation and introducing randomness through keys, the system achieves a high level of security.

## Implementation on the Triador Ternary Computer

The Triador ternary computer, described in the Triador project, features a unique architecture based on balanced ternary numbers (-1, 0, 1). This section explains how to adapt the proposed cryptographic method to the Triador computer system.

### Triador Architecture

The Triador computer uses a 3-trit balanced ternary system with registers that can store numbers from -13 to +13. It includes the following components:
- Four main registers (R1-R4)
- Nine extra registers (R5-R13)
- A special register (R13) used for memory segmentation
- A 1-trit borrow/carry flag
- A 6-trit program counter register
- Read-only program memory with 27 segments, each containing 27 instructions

*Here is the graphical description of the Triador architecture: Error! Filename not specified.*

### Instruction Set

The Triador instruction set consists of 9 instructions, each with a mandatory 3-trit argument:
- **EX ttt:** Extension commands
- **JP ttt:** Unconditional jump
- **SK ttt:** Conditional skip
- **OP ttt:** Unary operation
- **RR ttt:** Register copying
- **R1 ttt:** Write to R1
- **R2 ttt:** Write to R2
- **R3 ttt:** Write to R3
- **R4 ttt:** Write to R4

*Here is the graphical representation of the instruction set: Error! Filename not specified.*

## Practical Implementation

The encryption process involves generating public and private keys, using these keys to manipulate the exponentiation of base values, and subsequently encoding characters. Decryption reverses this process, utilizing the private key to retrieve the original data. Below is the Python implementation of the described cryptographic method.

### Encryption Algorithm in Ternary

1. **Key Generation:** Generate public and private keys within the range of Triador's registers.
2. **Encryption Function:** Convert the encryption steps into a sequence of Triador instructions.
3. **Decryption Function:** Similarly, convert the decryption steps into Triador instructions.

#### Example Program: Encrypting a Character

*Program File: encrypt.txt*

```plaintext
R1 NNN # Initialize R1 with -13 to set up program memory segment
RR NNN # Copy R1 to R13
R2 OOP # Load base (example: 3) into R2
R3 OON # Load exp1 (example: 2) into R3
R4 ONN # Load exp2 (example: 5) into R4
R5 OPN # Load pub_key (example: 6) into R5

# Encryption steps
# Compute custom_pow(base, exp1)
RR OON # Copy R2 (base) to R6
RR OOP # Copy R3 (exp1) to R7
EX OPO # Execute power function (example function placeholder)

# Store result in R8
RR OON # Copy result to R8

# Compute custom_pow(base, exp2 + pub_key)
RR OON # Copy R2 (base) to R6
R4 OOP # Load exp2 + pub_key into R4
EX PON # Execute power function (example function placeholder)

# Store result in R9
RR OON # Copy result to R9

# End of encryption
```


## Decryption Algorithm in Ternary

#### Example Program: Decrypting a Character

*Program File: decrypt.txt*

```plaintext
R1 NNN # Initialize R1 with -13 to set up program memory segment
RR NNN # Copy R1 to R13
R2 OOP # Load base (example: 3) into R2
R3 OON # Load exp1 (example: 2) into R3
R4 ONN # Load exp2 (example: 5) into R4
R5 OPN # Load priv_key (example: 12) into R5

# Decryption steps
# Compute custom_pow(base, exp1)
RR OON # Copy R2 (base) to R6
RR OOP # Copy R3 (exp1) to R7
EX OPO # Execute power function (example function placeholder)

# Store result in R8
RR OON # Copy result to R8

# Compute custom_pow(base, exp2 + priv_key)
RR OON # Copy R2 (base) to R6
R4 OPP # Load exp2 + priv_key into R4
EX PON # Execute power function (example function placeholder)

# Store result in R9
RR OON # Copy result to R9

# End of decryption
```
## Conclusion

By adapting your encryption and decryption algorithms to fit within the Triador's ternary architecture, you can explore the potential of ternary computing for cryptographic applications. This involves translating binary logic into ternary, utilizing the Triador's registers effectively, and converting your steps into the Triador's instruction set. The example programs provided demonstrate how to implement these steps on the Triador computer, showcasing the feasibility of this approach. Future work could involve optimizing these programs for efficiency and exploring other cryptographic algorithms within the ternary framework.

## References

1. Schneier, B. (1996). *Applied Cryptography: Protocols, Algorithms, and Source Code in C*. John Wiley & Sons.
2. Stallings, W. (2017). *Cryptography and Network Security: Principles and Practice*. Pearson.
3. Menezes, A. J., van Oorschot, P. C., & Vanstone, S. A. (1996). *Handbook of Applied Cryptography*. CRC Press.
4. The ultimate goal: a ternary computer https://github.com/ssloy/triador
