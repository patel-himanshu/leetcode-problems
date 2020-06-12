# Question: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3358/

"""
Design a data structure that supports all following operations in average O(1) time.
    (1) insert(val): Inserts an item val to the set if not already present.
    (2) remove(val): Removes an item val from the set if present.
    (3) getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.

Example:
    // Init an empty set.
    RandomizedSet randomSet = new RandomizedSet();

    // Inserts 1 to the set. Returns true as 1 was inserted successfully.
    randomSet.insert(1);

    // Returns false as 2 does not exist in the set.
    randomSet.remove(2);

    // Inserts 2 to the set, returns true. Set now contains [1,2].
    randomSet.insert(2);

    // getRandom should return either 1 or 2 randomly.
    randomSet.getRandom();

    // Removes 1 from the set, returns true. Set now contains [2].
    randomSet.remove(1);

    // 2 was already in the set, so return false.
    randomSet.insert(2);

    // Since 2 is the only number in the set, getRandom always return 2.
    randomSet.getRandom();
"""

import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.pos = {} # Stores indices of elements
        self.ele = [] # Stores elements
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        
        if val not in self.pos:
            self.ele.append(val)
            self.pos[val] = len(self.ele) - 1
            return True
        return False
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        
        if val in self.ele:
            loc = self.pos[val] # Location of "val" 
            last = self.ele[-1] # Last element's value
            
            self.ele[-1], self.ele[loc] = val, last # Switching "val" to last position
            self.pos[last] = loc # Updating position of last element
            
            self.ele.pop() # Removing val from list
            self.pos.pop(val) # Removing index of val from dictionary
            return True
        return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        # "random.choice(seq)" is better choice than "random.randint(0, len(list)-1)"
        return random.choice(self.ele)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

"""
| S.No. | List Operation | Avg. Time
|   1   |     Append     |   O(1)
|   2   |     Delete     |   O(n)
|   3   | Pop (last ele) |   O(1)
|   4   |      Len       |   O(1)

"k in d" operation for dictionary takes O(1) time, while the same operation in list takes O(n)
"""