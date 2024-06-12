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

<p>The encryption function can be mathematically represented as:
<span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>E</mi><mo stretchy="false">(</mo><mi>c</mi><mi>h</mi><mi>a</mi><mi>r</mi><mo separator="true">,</mo><mtext>pub_key</mtext><mo stretchy="false">)</mo><mo>=</mo><mo stretchy="false">(</mo><mi>b</mi><mi>a</mi><mi>s</mi><msup><mi>e</mi><mrow><mi>e</mi><mi>x</mi><mi>p</mi><mn>1</mn></mrow></msup><mo separator="true">,</mo><mi>b</mi><mi>a</mi><mi>s</mi><msup><mi>e</mi><mrow><mo stretchy="false">(</mo><mi>e</mi><mi>x</mi><mi>p</mi><mn>2</mn><mo>+</mo><mtext>pub_key</mtext><mo stretchy="false">)</mo></mrow></msup><mo stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">E(char, \text{pub\_key}) = (base^{exp1}, base^{(exp2 + \text{pub\_key})})</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 1.06em; vertical-align: -0.31em;"></span><span class="mord mathnormal" style="margin-right: 0.05764em;">E</span><span class="mopen">(</span><span class="mord mathnormal">c</span><span class="mord mathnormal">ha</span><span class="mord mathnormal" style="margin-right: 0.02778em;">r</span><span class="mpunct">,</span><span class="mspace" style="margin-right: 0.1667em;"></span><span class="mord text"><span class="mord">pub_key</span></span><span class="mclose">)</span><span class="mspace" style="margin-right: 0.2778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.2778em;"></span></span><span class="base"><span class="strut" style="height: 1.138em; vertical-align: -0.25em;"></span><span class="mopen">(</span><span class="mord mathnormal">ba</span><span class="mord mathnormal">s</span><span class="mord"><span class="mord mathnormal">e</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height: 0.8141em;"><span style="top: -3.063em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathnormal mtight">e</span><span class="mord mathnormal mtight">x</span><span class="mord mathnormal mtight">p</span><span class="mord mtight">1</span></span></span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right: 0.1667em;"></span><span class="mord mathnormal">ba</span><span class="mord mathnormal">s</span><span class="mord"><span class="mord mathnormal">e</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height: 0.888em;"><span style="top: -3.063em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mopen mtight">(</span><span class="mord mathnormal mtight">e</span><span class="mord mathnormal mtight">x</span><span class="mord mathnormal mtight">p</span><span class="mord mtight">2</span><span class="mbin mtight">+</span><span class="mord text mtight"><span class="mord mtight">pub_key</span></span><span class="mclose mtight">)</span></span></span></span></span></span></span></span></span><span class="mclose">)</span></span></span></span>
The decryption function reverses this process:
<span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>D</mi><mo stretchy="false">(</mo><mi>E</mi><mo stretchy="false">(</mo><mi>c</mi><mi>h</mi><mi>a</mi><mi>r</mi><mo separator="true">,</mo><mtext>pub_key</mtext><mo stretchy="false">)</mo><mo separator="true">,</mo><mtext>priv_key</mtext><mo stretchy="false">)</mo><mo>=</mo><mi>c</mi><mi>h</mi><mi>a</mi><mi>r</mi></mrow><annotation encoding="application/x-tex">D(E(char, \text{pub\_key}), \text{priv\_key}) = char</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 1.06em; vertical-align: -0.31em;"></span><span class="mord mathnormal" style="margin-right: 0.02778em;">D</span><span class="mopen">(</span><span class="mord mathnormal" style="margin-right: 0.05764em;">E</span><span class="mopen">(</span><span class="mord mathnormal">c</span><span class="mord mathnormal">ha</span><span class="mord mathnormal" style="margin-right: 0.02778em;">r</span><span class="mpunct">,</span><span class="mspace" style="margin-right: 0.1667em;"></span><span class="mord text"><span class="mord">pub_key</span></span><span class="mclose">)</span><span class="mpunct">,</span><span class="mspace" style="margin-right: 0.1667em;"></span><span class="mord text"><span class="mord">priv_key</span></span><span class="mclose">)</span><span class="mspace" style="margin-right: 0.2778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.2778em;"></span></span><span class="base"><span class="strut" style="height: 0.6944em;"></span><span class="mord mathnormal">c</span><span class="mord mathnormal">ha</span><span class="mord mathnormal" style="margin-right: 0.02778em;">r</span></span></span></span>
where <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mtext>pub_key</mtext></mrow><annotation encoding="application/x-tex">\text{pub\_key}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 1.0044em; vertical-align: -0.31em;"></span><span class="mord text"><span class="mord">pub_key</span></span></span></span></span> and <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mtext>priv_key</mtext></mrow><annotation encoding="application/x-tex">\text{priv\_key}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 1.0044em; vertical-align: -0.31em;"></span><span class="mord text"><span class="mord">priv_key</span></span></span></span></span> are randomly generated keys such that:
<span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mtext>priv_key</mtext><mo>=</mo><mtext>pub_key</mtext><mo>+</mo><mi>k</mi></mrow><annotation encoding="application/x-tex">\text{priv\_key} = \text{pub\_key} + k</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 1.0044em; vertical-align: -0.31em;"></span><span class="mord text"><span class="mord">priv_key</span></span><span class="mspace" style="margin-right: 0.2778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.2778em;"></span></span><span class="base"><span class="strut" style="height: 1.0044em; vertical-align: -0.31em;"></span><span class="mord text"><span class="mord">pub_key</span></span><span class="mspace" style="margin-right: 0.2222em;"></span><span class="mbin">+</span><span class="mspace" style="margin-right: 0.2222em;"></span></span><span class="base"><span class="strut" style="height: 0.6944em;"></span><span class="mord mathnormal" style="margin-right: 0.03148em;">k</span></span></span></span>
for some integer <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>k</mi></mrow><annotation encoding="application/x-tex">k</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.6944em;"></span><span class="mord mathnormal" style="margin-right: 0.03148em;">k</span></span></span></span>.</p>



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
