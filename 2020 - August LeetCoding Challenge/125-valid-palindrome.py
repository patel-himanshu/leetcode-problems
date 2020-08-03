# Question: https://leetcode.com/explore/featured/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3411/

"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
    Input: "A man, a plan, a canal: Panama"
    Output: true

Example 2:
    Input: "race a car"
    Output: false

Constraints: s consists only of printable ASCII characters.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        p1, p2 = 0, len(s)-1
        
        while p1 < p2:
            if not s[p1].isalnum(): 
                p1 += 1
                continue
            if not s[p2].isalnum(): 
                p2 -= 1
                continue
            
            if s[p1] == s[p2]:
                p1 += 1
                p2 -= 1
            else:
                return False
        
        return True