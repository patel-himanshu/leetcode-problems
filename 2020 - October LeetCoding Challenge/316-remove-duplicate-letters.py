# Question: https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/560/week-2-october-8th-october-14th/3491/

"""
Given a string s, remove duplicate letters so that every letter appears once and only once.
You must make sure your result is the smallest in lexicographical order among all possible results.
Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

Example 1:
    Input: s = "bcabc"
    Output: "abc"

Example 2:
    Input: s = "cbacdcbc"
    Output: "acdb"

Constraints:
    (1) 1 <= s.length <= 104
    (2) s consists of lowercase English letters.
"""

from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        c = Counter(s)
        stack = []
        
        for letter in s:
            c[letter] -= 1
            if letter not in stack:
                while stack and stack[-1] > letter and c[stack[-1]]:
                    stack.pop()
                stack.append(letter)
        
        return ''.join(stack)