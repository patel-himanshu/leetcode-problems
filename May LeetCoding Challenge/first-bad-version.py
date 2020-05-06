# Question: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3316/

from math import sqrt

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """        
        for i in range(n,-1,-round(sqrt(n))):
            if i<0:
                break
            elif isBadVersion(i)==0:
                while 1:
                    i+=1
                    if isBadVersion(i):
                        return i
        i = 0
        while 1:
            i+=1
            if isBadVersion(i):
                return i