#!/usr/bin/python3
"""
A solution to the 'panagram' challenge implemented in Python3.
@author Vitali Tchalov
"""
import sys
import os

#User function Template for python3

class Solution:
    
    #Function to check if a string is Pangram or not.
    def checkIfPangram(self,s):
        #code here
        
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
            "not pangram", \
            "A sentence longer than 26 characters but it is not a pangram.", \
            "The quick brown fox jumps over the lazy dog" \
    ]

    obj = Solution()

    for s in tests:
        print("Checking if string '" + s + "' for being a pangram. String length is ", len(s), ".")

        if (obj.checkIfPangram(s)):
            print("'" + s + "' IS a pangram.")
        else:
            print("'" + s + "' is NOT a pangram.")

if __name__ == '__main__':
    main()
