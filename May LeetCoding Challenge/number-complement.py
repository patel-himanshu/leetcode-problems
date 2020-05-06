# Question: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3319/

class Solution:
    def findComplement(self, num: int) -> int:
        complement = ''
        for i in format(num, 'b'):
            if i=='0':
                complement += '1'
            else:
                complement += '0'
        return int(complement,2)