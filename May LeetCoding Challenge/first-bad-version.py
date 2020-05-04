# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
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