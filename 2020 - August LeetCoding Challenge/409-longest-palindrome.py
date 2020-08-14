# Question: https://leetcode.com/explore/featured/card/august-leetcoding-challenge/550/week-2-august-8th-august-14th/3423/

"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
This is case sensitive, for example "Aa" is not considered a palindrome here.
Note: Assume the length of given string will not exceed 1,010.

Example:
    Input: "abccccdd"
    Output: 7
    Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
"""

from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        ans = 0
        any_odd = False
        
        for i in counter:
            if not any_odd and counter[i]&1:
                any_odd = True
                ans += 1
            ans += 2 * (counter[i]//2)
        
        return ans