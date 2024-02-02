#!/usr/bin/python3
"""
A solution to the 'Longest Distinct Sequential Characters in a text' challenge implemented in Python3.
Complexity: O(N)
@author Vitali Tchalov https://github.com/VitaliTch
"""

import sys
import os

class Solution:
    
    # A function to check if a string is Pangram or not.
    def longestSubstrDistinctChars(self, s):
        
        max_len = 0
        longest_str = ''
        sub_str = ''
        prev_chars = {} # a dictionary for keeping track of distinct characters

        # Assuming 'distinct' does not extend to lower and upper case, i.e. 'a' and 'A' are not considered distinct.
        for c in s.lower():
            # if the char is already in the dictionary, then check if the current segment is longer 
            # than the previous one and then reset the dictionary to start over: 
            if prev_chars.get(c) != None:
                if len(prev_chars) > max_len:
                    max_len = len(prev_chars)
                    longest_str = sub_str
                    sub_str = ''
                prev_chars = {}

            prev_chars[c]=c
            sub_str += c

        # Check the last segment (substring) to see if it's the longest
        if len(prev_chars) > max_len:
            max_len = len(prev_chars)
            longest_str = sub_str

        print("The longest substring of distinct chars is\n'" + longest_str + "'")
        return max_len

def main():
    tests = [
            ["aewergrththy", 3], \ # The geeks claim the correct number is 4, but is it really? aew|erg|rth|thy
            ["", 0], \
            ["A", 1], \
            ["geeks", 3], \
            ["geEks", 3], \
            ["geeksforgeeks", 7], \
            ["abc", 3], \
            ["ab abc bqwerty", 7], \
            ["geeksforgeeks and a much longer sequence of 'abcdefg_1234567890, ok!' distinct chars, 21 actually", 21] \
    ]

    obj = Solution()

    for s in tests:
        print("Checking for a longest substring of distinct characters in the text:\n", "'" + s[0] + "'")

        longest_distinct = obj.longestSubstrDistinctChars(s[0])

        print("Length of longest substring of distinct chars is: " + str(longest_distinct))

if __name__ == '__main__':
    main()
