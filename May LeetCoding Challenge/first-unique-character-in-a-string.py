#Question: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3320/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            if s.count(s[i]) == 1:
                return i
        return -1