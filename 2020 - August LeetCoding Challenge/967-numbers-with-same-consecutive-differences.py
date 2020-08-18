# Question: https://leetcode.com/explore/featured/card/august-leetcoding-challenge/551/week-3-august-15th-august-21st/3428/

"""
Return all non-negative integers of length N such that the absolute difference between every two consecutive digits is K.
Note that every number in the answer must not have leading zeros except for the number 0 itself.
For example, 01 has one leading zero and is invalid, but 0 is valid.
You may return the answer in any order.

Example 1:
    Input: N = 3, K = 7
    Output: [181,292,707,818,929]
    Explanation: Note that 070 is not a valid number, because it has leading zeroes.

Example 2:
    Input: N = 2, K = 1
    Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]

Note:
    (1) 1 <= N <= 9
    (2) 0 <= K <= 9
"""

class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        if N == 1: return [0,1,2,3,4,5,6,7,8,9]
        ans = list(range(1,10))
        
        for i in range(N-1):
            new_list = []
            for elem in ans:
                plusK = elem%10 + K
                if plusK <= 9 and elem*10 + plusK not in new_list:
                    new_list.append(elem*10 + plusK)

                minusK = elem%10 - K
                if 0 <= minusK and elem*10 + minusK not in new_list:
                    new_list.append(elem*10 + minusK)
            ans = new_list
            
        return ans