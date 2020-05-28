# Question: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3343/

"""
Given a non negative integer number num.
For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's 
in their binary representation and return them as an array.

Example 1:
    Input: 2
    Output: [0,1,1]

Example 2:
    Input: 5
    Output: [0,1,1,2,1,2]

Follow up:
    (1) It is very easy to come up with a solution with run time O(n*sizeof(integer)). 
        But can you do it in linear time O(n) /possibly in a single pass?
    (2) Space complexity should be O(n).
    (3) Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
"""

class Solution:
    def countBits(self, num):       # countBits(self, num: int) -> List[int]
        ans = [0]
        for i in range(1, num+1):
            if i&1:
                ans.append(1 + ans[i>>1])
            else:
                ans.append(ans[i>>1])
            # Above 4 statements can also be written as
            # ans.append( ans[i>>1] + (i&1) )
        return ans

"""
[  0,  1,  2,  3 ]  ==>  [ 0, 1, 1, 2 ]
[  4,  5,  6,  7 ]  ==>  [ 1, 2, 2, 3 ]
[  8,  9, 10, 11 ]  ==>  [ 1, 2, 2, 3 ]
[ 12, 13, 14, 15 ]  ==>  [ 2, 3, 3, 4 ]
[ 16, 17, 18, 19 ]  ==>  [ 1, 2, 2, 3 ]
[ 20, 21, 22, 23 ]  ==>  [ 2, 3, 3, 4 ]
[ 24, 25, 26, 27 ]  ==>  [ 2, 3, 3, 4 ]
[ 28, 29, 30, 31 ]  ==>  [ 3, 4, 4, 5 ]
"""

inputs = [2, 5, 13]
outputs = [
    [0,1,1],
    [0,1,1,2,1,2],
    [0,1,1,2,1,2,2,3,1,2,2,3,2,3]
]

S = Solution()
for i in inputs:
    print(S.countBits(i))