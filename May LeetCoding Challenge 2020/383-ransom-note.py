# Question: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3318/

"""
Given an arbitrary ransom note string and another string containing letters from all the magazines, 
write a function that will return true if the ransom note can be constructed from the magazines; 
otherwise, it will return false. Each letter in the magazine string can only be used once in your ransom note.

Example 1:
    Input: ransomNote = "a", magazine = "b"
    Output: false

Example 2:
    Input: ransomNote = "aa", magazine = "ab"
    Output: false

Example 3:
    Input: ransomNote = "aa", magazine = "aab"
    Output: true

Constraints:
    (1) You may assume that both strings contain only lowercase letters.
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rN = set(ransomNote)
        flag = 1
        for i in rN:
            if magazine.count(i) < ransomNote.count(i):
                flag = 0
                break
        if flag == 0:
            return 0
        else:
            return 1