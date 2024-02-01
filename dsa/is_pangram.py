#!/usr/bin/python3
"""
A solution to the 'pangram' challenge implemented in Python3.
Complexity: O(N)
@author Vitali Tchalov
"""

import sys
import os

class Solution:
    
    # A function to check if a string is Pangram or not.
    def checkIfPangram(self, s):
        
        alpha_chars = {}
        
        if len(s) < 26:
            return False
            
        for c in s.lower():
            if ord(c) >= 97 and ord(c) <= 122:
                alpha_chars[c]=c
                
        if len(alpha_chars) == 26:
            return True
        return False

def main():
    tests = [
            "Short not pangram text", \
            "A sentence longer than 26 characters but it is not a pangram.", \
            "1. The quick brown fox jumps over the lazy dog.", \
            "2. Sphinx of black quartz, judge my vow.", \
            "3. Pack my box with five dozen liquor jugs."
    ]

    obj = Solution()

    for s in tests:
        print("Checking a text of length ", len(s))

        if (obj.checkIfPangram(s)):
            print("'" + s + "' IS a pangram.")
        else:
            print("'" + s + "' is NOT a pangram.")

if __name__ == '__main__':
    main()
