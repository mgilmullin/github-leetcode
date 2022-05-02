"""
https://leetcode.com/problems/search-in-rotated-sorted-array/

33. Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1

Constraints:
1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104

Analysis
This problem is an extension of the binary search.
First we can find the index from where it is sorted.
We can perform binary search to find the index where the array is rotated.
Array will be divided into two halves by the pivot index.
Once we have found that index, then we can  determine in which half of the array the target lies.
Notice, the two halves are themselves will be sorted.
We can then perform binary search once again in the determined half to find the index of the target element.

Time Complexity
Since we are discarding one half of the array after every iteration, the time complexity will be O(log n).

Space Complexity
We are not using any data structure for intermediate calculations, hence the space complexity would be O(1).

"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if nums is None or len(nums) == 0:
            return -1
        left, right = 0, len(nums) - 1
        while left < right:
            middle = left + (right - left) // 2
            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle

        pivot = left
        left, right = 0, len(nums) - 1

        if nums[pivot] <= target <= nums[right]:
            left = pivot
        else:
            right = pivot

        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return -1
        