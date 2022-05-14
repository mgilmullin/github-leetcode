"""
https://leetcode.com/problems/arithmetic-slices/

413. Arithmetic Slices

An integer array is called arithmetic 
if it consists of at least three elements and 
if the difference between any two consecutive elements is the same.
For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.

Given an integer array nums, return the number of arithmetic subarrays of nums.

A subarray is a contiguous subsequence of the array.
 

Example 1:
Input: nums = [1,2,3,4]
Output: 3
Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.

Example 2:
Input: nums = [1]
Output: 0
 

Constraints:
1 <= nums.length <= 5000
-1000 <= nums[i] <= 1000

Method: Dynamic Programming (dp)
The question is transformed into the number of arithmetic sub-sequences for an 
arithmetic sequence with elements.
In the arithmetic sequence of n elements, the number of sub-arithmetic sequence is:
(n + 1) + n + … + 1.
Use num to represent the total number of arithmetic series. 
Use consecutive (dp) to represent the length of an arithmetic in array.

Time complexity: O(n)
Space complexity: O(1)

"""


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        consecutive, num = 0 , 0
        for i in range (2,len(nums)):
            if nums[i - 1] - nums[i - 2] == nums[i] - nums[i - 1]:
                consecutive += 1
                num += consecutive
            else:
                consecutive = 0
        return num
