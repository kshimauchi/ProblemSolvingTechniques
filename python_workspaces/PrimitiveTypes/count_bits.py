# Python 3.8
# Everything in python is a object:
from functools import lru_cache

def count_bits(x: int) -> int:
    """
    Args:
        x (object):
    """
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits
print(count_bits(12))

@lru_cache(maxsize=1028)
def count_vowels(sentence):
    sentence = sentence.casefold()
    return sum(sentence.count(vowel) for vowel in 'aeiou')
print("count vowels: ")
print(count_vowels("All developed computer languages so far are context sensitive "))