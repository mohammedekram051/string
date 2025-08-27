# 1. Reverse string
def reverse_string(s):
    return s[::-1]

# 2. Count vowels
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in s if ch in vowels)

# 3. Check anagrams
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

# 4. Word count in sentence
def word_count(sentence):
    words = sentence.split()
    return {word: words.count(word) for word in set(words)}

# 5. Caesar Cipher
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

# 6. Validate email with regex
import re
def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))
