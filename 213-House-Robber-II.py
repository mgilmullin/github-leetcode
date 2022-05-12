"""
https://leetcode.com/problems/house-robber-ii/

213. House Robber II

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
 

Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:
Input: nums = [1,2,3]
Output: 3
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000

Methodology: Dynamic Programming. 
But the robber can either rob the first house or last house but not both. 
We will give the two input list. 
One with first house and without the last house. 
The other one with last house and without the first house. 
Then we compare the two input list results.

Time complexity:
We iterate all dp array, it will cost O(n).
We have to input list, that give n+n cost. 
Therefore, Big O is O(n).

"""


class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums: return 0
        def maxMoney(nums):
            nums = [0]+nums
            for i in range(3,len(nums)):
                nums[i]+=max(nums[i-3],nums[i-2])
            return max(nums[-1],nums[-2])
        return max(maxMoney(nums[1:]),maxMoney(nums[:-1])) if len(nums) > 2 else max(nums)               
