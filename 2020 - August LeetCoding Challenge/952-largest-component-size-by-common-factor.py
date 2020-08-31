# Question: https://leetcode.com/explore/featured/card/august-leetcoding-challenge/553/week-5-august-29th-august-31st/3442/

"""
Given a non-empty array of unique positive integers A, consider the following graph:
    (1) There are A.length nodes, labelled A[0] to A[A.length - 1];
    (2) There is an edge between A[i] and A[j] if and only if A[i] and A[j] share a common factor greater than 1.
Return the size of the largest connected component in the graph.

Example 1:
    Input: [4,6,15,35]
    Output: 4

Example 2:
    Input: [20,50,9,63]
    Output: 2

Example 3:
    Input: [2,3,6,7,4,12,21,39]
    Output: 8

Note:
    (1) 1 <= A.length <= 20000
    (2) 1 <= A[i] <= 100000
"""

from collections import defaultdict, Counter

class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        primes = []
        for x in range(2, int(max(A)**0.5)+1):
            for y in primes:
                if x % y == 0:
                    break
            else:
                primes.append(x)
    
        factors = defaultdict(list)
        for num in A:
            elem = num
            for prime in primes:
                if prime ** 2 > elem:
                    break
                if elem % prime == 0:
                    factors[num].append(prime)
                    while elem % prime == 0:
                        elem = elem // prime
            if elem > 1:
                primes.append(elem)
                factors[num].append(elem)
                
        primes = list(set(primes))
        parent = list(range(len(primes)))
        p2i = {p:i for i,p in enumerate(primes)}
        
        def find(i):
            if i != parent[i]:
                parent[i] = find(parent[i])
            return parent[i]
        
        def union(i,j):
            pi, pj = find(i), find(j)
            if pi != pj:
                parent[pi] = pj
            
        for a in A:
            if factors[a]:
                pf0 = factors[a][0]
                for pf in factors[a][1:]:
                    union(p2i[pf0], p2i[pf])
                
        count = Counter(find(p2i[factors[a][0]]) for a in A if factors[a])
        return max(count.values())