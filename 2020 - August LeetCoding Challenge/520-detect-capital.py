# Question: https://leetcode.com/explore/featured/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3409/

"""
Given a word, you need to judge whether the usage of capitals in it is right or not.
We define the usage of capitals in a word to be right when one of the following cases holds:
    (1) All letters in this word are capitals, like "USA".
    (2) All letters in this word are not capitals, like "leetcode".
    (3) Only the first letter in this word is capital, like "Google".

Otherwise, we define that this word doesn't use capitals in a right way.

Example 1:
    Input: "USA"
    Output: True

Example 2:
    Input: "FlaG"
    Output: False

Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
"""

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper(): return True
        elif word.islower(): return True
        elif word[0].isupper() and word[1:].islower(): return True
        return False