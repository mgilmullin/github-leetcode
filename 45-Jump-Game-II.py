"""
https://leetcode.com/problems/jump-game-ii/

45. Jump Game II

Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.
You can assume that you can always reach the last index.
 

Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2
 

Constraints:
1 <= nums.length <= 104
0 <= nums[i] <= 1000


Method:  Greedy Algorithm.
We can visit any index between the current index (i) and i + nums[i]. 
We can iterate through nums while keeping track of the furthest index reachable (maxPos) at any given moment (maxPos = max(maxPos, i + nums[i])). 
We'll know we've found our solution once maxPos reaches or passes the last index (maxPos >= len(nums) - 1).
The difficulty then lies in keeping track of how many jumps it takes to reach that point. 

So in addition to next, we'll also need to keep track of the current jump's endpoint (end) as well as the number of jumps taken so far (steps).

Time Complexity: O(N) where N is the length of nums.
Space Complexity: O(1)

"""

class Solution:
    def jump(self, nums: List[int]) -> int:

        maxPos = 0
        end = 0
        steps = 0
        for i in range(len(nums) - 1):
            maxPos = max(maxPos, i + nums[i])
            if i == end:
                end = maxPos
                steps += 1
        
        return steps
