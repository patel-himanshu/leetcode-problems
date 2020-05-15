# Question: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3330/

class Solution:
    def kadane(self, arr):
        lmax, gmax = 0, max(arr)
        for i in range(len(arr)):
            lmax = max(arr[i], arr[i]+lmax)
            if lmax > gmax:
                gmax = lmax
        return gmax

    def maxSubarraySumCircular(self, A):
        if len(A) == 1:
            return A[0]

        B = [-i for i in A]
        total = sum(A)

        a1 = self.kadane(A)
        a2 = total + self.kadane(B[1:])
        a3 = total + self.kadane(B[:-1])
        return max(a1, a2, a3)
 
testcases = [
    [[-2], -2],
    [[1,-1], 1],
    [[1,-2,3,-2],3],
    [[5,-3,5],10],
    [[3,-1,2,-1],4],
    [[3,-2,2,-3],3],
    [[-2,-3,-1],-1],
    [[9,0,-2,9], 18]
]

S = Solution()
for i in testcases:
    print('Test Case ==> {0} : {1}'.format(i[1] == S.maxSubarraySumCircular(i[0]), S.maxSubarraySumCircular(i[0])))