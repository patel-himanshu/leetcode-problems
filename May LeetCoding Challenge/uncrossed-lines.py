# Question:

"""
We write the integers of A and B (in the order they are given) on two separate horizontal lines.
Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:
    (1) A[i] == B[j];
    (2) The line we draw does not intersect any other connecting (non-horizontal) line.

Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.
Return the maximum number of connecting lines we can draw in this way.

Example 1:
    Input: A = [1,4,2], B = [1,2,4]
    Output: 2
    Explanation: We can draw 2 uncrossed lines as in the diagram.
                 We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will intersect the line from A[2]=2 to B[1]=2.

Example 2:
    Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]
    Output: 3

Example 3:
    Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]
    Output: 2 

Note:
    (1) 1 <= A.length <= 500
    (2) 1 <= B.length <= 500
    (3) 1 <= A[i], B[i] <= 2000
"""

class Solution:
    def maxUncrossedLines(self, A, B): # maxUncrossedLines(self, A: List[int], B: List[int]) -> int
        storage = {}
        lA, lB = len(A), len(B)

        def checker(i, j):
            if i>=lA or j>=lB:
                return 0
            if (i,j) in storage:
                return storage[i,j]
            if A[i]==B[j]:
                update = 1 + checker(i+1, j+1)
            else:
                update = max(checker(i+1, j), checker(i, j+1))
            
            storage[i,j] = update
            return update
        
        return checker(0,0)

inputs_A = [
    [1,4,2],
    [2,5,1,2,5],
    [1,3,7,1,7,5],
    [1,6,2,3,4,5]
]

inputs_B = [
    [1,2,4],
    [10,5,2,1,5,2],
    [1,9,2,5,1],
    [6,4,5,3,4,5]
]

outputs = [2,3,2,3]

S = Solution()
for i in range(len(outputs)):
    print(S.maxUncrossedLines(inputs_A[i], inputs_B[i]))