"""
https://leetcode.com/problems/house-robber/

198. House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 400

This question solved by Dynamic Programming. 
For this question, you can rob the adjacent house means you have to skip the last step and pick the maximum money between the forth and the third from last.
Start from the forth position and pick the maxmium value between the forth and the third from last. Then sum up to the current value to get the current position’s maximum value

Result Because you can rob the adjacent house, so the final answer should be the mixmium value picked between the last and the second last value.

BigO
It is O(n)
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
            if not nums: return 0
            size=len(nums)
            if size < 3:
                return max(nums)
            dp=[0]*(size+1)
            dp[1]=nums[0]
            dp[2]=nums[1]
            for i in range(2,size):
                dp[i+1]=nums[i]+max(dp[i-2],dp[i-1])
            return max(dp[-2],dp[-1])
