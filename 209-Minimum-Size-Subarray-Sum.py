"""
https://leetcode.com/problems/minimum-size-subarray-sum/

209. Minimum Size Subarray Sum

Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.
 

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:
1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 105

Algorithm
We use two pointers i and j for tracking every subarray, j denotes to the head and i denotes to the tail.

When sum of current subarray is less than target, which means we have to put more item into this subarray, move i to next index so it be more larger.
When sum of current subarray is more then target, which means we have to remove items in this subarray, move j to next index so it be more smaller.
Every time we found sum of current subarray is more then target, recording current length and comparing with minimum length. Once it’s smaller than minimum length, update minimum length to be current length.

Complexity
Because both pointer i and j will iterate array only once, it takes O(n) times if n denotes to length of array. 
Extra space is O(1).

"""


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        j = 0
        total = 0
        n = len(nums)
        minСount = n + 1

        for i in range(n):
            total += nums[i]
            while total >= target:
                newСount = i - j + 1
                if minСount > newСount:
                    minСount = newСount
                total -= nums[j]
                j += 1

        return 0 if minСount > n else minСount
