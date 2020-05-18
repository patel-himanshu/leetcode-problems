# Question: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3333/

'''
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. 
In other words, one of the first string's permutations is the substring of the second string.

Example 1:
    Input: s1 = "ab" s2 = "eidbaooo"
    Output: True
    Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
    Input:s1= "ab" s2 = "eidboaoo"
    Output: False

Note:
    (1) The input strings only contain lower case letters.
    (2) The length of both given strings is in range [1, 10,000].
'''

from collections import Counter

class Solution:
    def checkInclusion(self, s1, s2): # checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) == len(s2):
            return Counter(s1) == Counter(s2)

        s1_counter = Counter(s1)

        for i in range(len(s2)-len(s1)+1):
            if Counter(s2[i:i+len(s1)]) == s1_counter:
                return True
        return False

test_cases = [
    ['ab', 'eidbaooo'],
    ['ab', 'eidboaoo']
]

S = Solution()
for i in test_cases:
    print(S.checkInclusion(i[0], i[1]))