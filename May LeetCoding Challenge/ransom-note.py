# Question: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3318/

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