# Hackerrank: Sherlock and Anagrams
# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem



import math
import os
import random
import re
import sys
from collections import Counter

def sherlockAndAnagrams(s):
    """
    Calculates the number of unordered anagrammatic pairs of substrings in a string.
    """
    n = len(s)
    signatures = {}
    for i in range(n):
        for j in range(i, n):
            sub = s[i:j+1]

            signature = "".join(sorted(sub))

            signatures[signature] = signatures.get(signature, 0) + 1
            
    total_pairs = 0
    for count in signatures.values():
        total_pairs += count * (count - 1) // 2
        
    return total_pairs

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
        q = int(input().strip())
        for q_itr in range(q):
            s = input()
            result = sherlockAndAnagrams(s)
            fptr.write(str(result) + '\n')
        fptr.close()
    except (KeyError, FileNotFoundError):
        q = int(input("Enter number of test cases: ").strip())
        for _ in range(q):
            s = input("Enter string: ")
            result = sherlockAndAnagrams(s)
            print("Result:", result)