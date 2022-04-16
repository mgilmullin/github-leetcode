"""
https://leetcode.com/problems/move-zeroes/

283. Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #1st variant:
        #nums[:] = [nz for nz in nums if nz != 0] + [z for z in nums if z == 0]

        #2nd variant:
        #withoutZero = [nz for nz in nums if nz != 0]
        #nums[:] = withoutZero + [0] * (len(nums) - len(withoutZero))
        
        #3rd variant:
        #withoutZero = [nz for nz in nums if nz != 0]
        #nums[:] = withoutZero + [0] * nums.count(0)
        
        #4th variant:
        #nums[:] = list(filter(lambda x: x != 0, nums)) + \
        #          list(filter(lambda x: x == 0, nums))
        
        #5th variant:
        withoutZero = list(filter(lambda x: x != 0, nums))
        withoutZero.extend([0] * nums.count(0))
        nums[:] = withoutZero
