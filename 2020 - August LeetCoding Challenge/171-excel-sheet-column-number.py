# Question: https://leetcode.com/explore/featured/card/august-leetcoding-challenge/550/week-2-august-8th-august-14th/3419/

"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...

Example 1:
    Input: "A"
    Output: 1

Example 2:
    Input: "AB"
    Output: 28

Example 3:
    Input: "ZY"
    Output: 701

Constraints:
    (1) 1 <= s.length <= 7
    (2) s consists only of uppercase English letters.
    (3) s is between "A" and "FXSHRXW".
"""

class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = 0
        power = 0
        
        for i in s[::-1]:
            order = ord(i) - ord('A') + 1
            ans += 26**power * order
            power += 1
        
        return ans