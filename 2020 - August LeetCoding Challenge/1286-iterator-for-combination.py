# Question: https://leetcode.com/explore/featured/card/august-leetcoding-challenge/550/week-2-august-8th-august-14th/3422/

"""
Design an Iterator class, which has:
    (1) A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
    (2) A function next() that returns the next combination of length combinationLength in lexicographical order.
    (3) A function hasNext() that returns True if and only if there exists a next combination.

Example:
    CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.
    iterator.next(); // returns "ab"
    iterator.hasNext(); // returns true
    iterator.next(); // returns "ac"
    iterator.hasNext(); // returns true
    iterator.next(); // returns "bc"
    iterator.hasNext(); // returns false

Constraints:
    (1) 1 <= combinationLength <= characters.length <= 15
    (2) There will be at most 10^4 function calls per test.
    (3) It's guaranteed that all calls of the function next are valid.
"""

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combinations = list(itertools.combinations(characters, combinationLength))
        self.char_length = len(self.combinations)
        self.pos = 0

    def next(self) -> str:
        self.pos += 1
        return ''.join(self.combinations[self.pos - 1])

    def hasNext(self) -> bool:
        return self.pos < self.char_length        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()