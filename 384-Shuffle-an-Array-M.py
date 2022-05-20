"""
https://leetcode.com/problems/shuffle-an-array/

384. Shuffle an Array

Given an integer array nums, design an algorithm to randomly shuffle the array. 
All permutations of the array should be equally likely as a result of the shuffling.

Implement the Solution class:

Solution(int[] nums) Initializes the object with the integer array nums.
int[] reset() Resets the array to its original configuration and returns it.
int[] shuffle() Returns a random shuffling of the array.
 

Example 1:
Input
["Solution", "shuffle", "reset", "shuffle"]
[[[1, 2, 3]], [], [], []]
Output
[null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

Explanation
Solution solution = new Solution([1, 2, 3]);
solution.shuffle();    // Shuffle the array [1,2,3] and return its result.
                       // Any permutation of [1,2,3] must be equally likely to be returned.
                       // Example: return [3, 1, 2]
solution.reset();      // Resets the array back to its original configuration [1,2,3]. Return [1, 2, 3]
solution.shuffle();    // Returns the random shuffling of array [1,2,3]. Example: return [1, 3, 2]
 

Constraints:
1 <= nums.length <= 50
-106 <= nums[i] <= 106
All the elements of nums are unique.
At most 104 calls in total will be made to reset and shuffle.

Method: Fisher-Yates Algorithm. ( or Brute Force Algorithm)

Randomly sets original elements new positions.
On each iteration of the algorithm, we generate a random integer between the current index and 
the last index of the array. Then, we swap the elements at the current index and the chosen index - 
this simulates drawing (and removing) the element from the hat, as the next range 
from which we select a random index will not include the most recently processed one. 
One small, yet important detail is that it is possible to swap an element with itself - 
otherwise, some array permutations would be more likely than others. 

Complexity Analysis:

Time complexity : O(n)
The Fisher-Yates algorithm runs in linear time, 
as generating a random index and swapping two values can be done in constant time.

Space complexity : O(n)
We need linear space for reset, so we have linear space complexity.

"""

class Solution:

    def __init__(self, nums: List[int]):
        self.array = nums
        self.original = list(nums)        

    def reset(self) -> List[int]:
        self.array = self.original
        self.original = list(self.original)
        return self.array        

    def shuffle(self) -> List[int]:
        for i in range(len(self.array)):
            swapIdx = random.randrange(i, len(self.array))
            self.array[i], self.array[swapIdx] = self.array[swapIdx], self.array[i]
        return self.array        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
