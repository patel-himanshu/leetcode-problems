# Question: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3317/

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        total = 0
        for i in J:
            total += S.count(i)
        return total